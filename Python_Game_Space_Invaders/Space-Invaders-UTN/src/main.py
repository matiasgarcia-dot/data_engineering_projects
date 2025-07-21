import sys
import os
import pygame
from settings import *           # Importa constantes de configuración (pantalla, FPS, etc.)
from core.game import Game       # Importa la clase principal del juego
from core.hud import show_hub, show_game_over, show_scores_menu, show_main_menu
from systems.progress import Progress

def add_project_root_to_path():
    """
    Agrega la raíz del proyecto a sys.path para permitir importaciones relativas.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if base_path not in sys.path:
        sys.path.append(base_path)

def initialize_pygame():
    """
    Inicializa Pygame y su mixer, manejando posibles errores.
    """
    try:
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    except pygame.error as e:
        print(f"Error al iniciar Pygame: {e}")
        sys.exit(1)

def run_game_loop(game, clock):
    """
    Ejecuta el loop principal del juego, manejando eventos y actualizando la pantalla.

    Args:
        game (Game): Instancia del juego principal.
        clock (pygame.time.Clock): Reloj para controlar los FPS.
    """
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        game.update()
        game.draw()
        pygame.display.flip()
        if game.is_game_over:
            running = False
    return game.last_score if game.last_score != 0 else game.score

def main():
    """
    Función principal que inicializa el juego y ejecuta el loop principal.
    """
    add_project_root_to_path()
    initialize_pygame()

    # Crea la ventana del juego con tamaño definido en settings.py
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders - UTN")

    # Instanciar Progress una sola vez
    progress = Progress()

    # Seleccionar skin por defecto
    current_skin = progress.get_selected_skin() or "player0.png"

    # Mostrar HUB antes de iniciar el juego (pantalla de inicio con opciones)
    clock = pygame.time.Clock()
    while True:
        menu_option = show_main_menu(screen, progress, current_skin)
        if menu_option == 0:  # Jugar
            start, player_name = show_hub(screen, progress)
            if not start:
                continue
            print(f"skin(main): {current_skin}")
            game = Game(screen, progress, current_skin)
            final_score = run_game_loop(game, clock)
            if player_name:
                progress.save_score(player_name, final_score)
            show_game_over(screen, final_score)
            play_again = show_scores_menu(screen, progress)
            if play_again:
                continue  # vuelve a pedir nombre y jugar
            else:
                continue  # vuelve al menú principal
        elif menu_option == 1:  # Tabla de posiciones
            show_scores_menu(screen, progress)
            continue
        else:  # Salir
            break

    # Cerrar conexión de Progress
    progress.conn.close()
    pygame.quit()

# Llama a main solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
