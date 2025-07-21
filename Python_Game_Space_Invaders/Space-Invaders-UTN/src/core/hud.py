import os
import pygame
from settings import WIDTH, WHITE, BLACK
from systems.progress import Progress
from systems.inventory import Inventory

def draw_hud(screen, score, lives, level):
    font_name = "Courier"
    # Fuente predeterminada del sistema
    font = pygame.font.SysFont(font_name, 24, bold=True)

    # Texto a mostrar con score, vidas y nivel
    text = font.render(f"Score: {score}   Vidas: {lives}   Nivel: {level}", True, WHITE)

    # Dibuja el texto en la esquina superior izquierda
    screen.blit(text, (10, 10))

def draw_score_table(screen, scores):
    font = pygame.font.SysFont("Courier", 28, bold=True)
    title = font.render("TOP 5 SCORES", True, (255, 255, 0))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
    y = 170
    for idx, entry in enumerate(scores):
        text = font.render(f"{idx+1:2d}. {entry['name'][:10]:10s}  {entry['score']:5d}", True, (255,255,255))
        screen.blit(text, (WIDTH // 2 - 180, y))
        y += 32

def show_hub(screen, progress):
    font_name = "Courier"
    font_title = pygame.font.SysFont(font_name, 48, bold=True)
    font_option = pygame.font.SysFont(font_name, 36, bold=True)
    font_score = pygame.font.SysFont(font_name, 28)
    
    title = font_title.render("Space Invaders - UTN", True, WHITE)
    start = font_option.render("Presiona ENTER para jugar", True, WHITE)
    
    # Cargar y mostrar tabla de scores
    scores = progress.load_scores(limit=5)
    
    input_active = True
    name = ""
    input_font = pygame.font.SysFont(font_name, 32, bold=True)
    input_rect = pygame.Rect(WIDTH//2-160, 420, 320, 40)
    color = pygame.Color('white')
    
    clock = pygame.time.Clock()
    cursor_blink = True
    cursor_timer = 0
    cursor_interval = 400  # ms para el cursor
    # Calcular el máximo de caracteres que caben en el input
    max_input_width = input_rect.w - 30  # margen para 'Nombre: ' y el cursor
    max_chars = 20  # valor inicial alto
    for i in range(1, 30):
        test_str = 'W' * i
        test_surface = input_font.render(f"Nombre: {test_str}|", True, color)
        if test_surface.get_width() > max_input_width:
            max_chars = i - 1
            break
    while True:
        screen.fill(BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
        draw_score_table(screen, scores)
        # Input box (arriba del texto de enter)
        display_name = name
        # Cursor parpadeante
        if input_active and cursor_blink:
            display_name += "|"
        txt_surface = input_font.render(f"Nombre: {display_name}", True, color)
        screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, color, input_rect, 2)
        # Texto SIEMPRE visible
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 480))
        pygame.display.flip()
        # Blink logic para el cursor
        cursor_timer += clock.get_time()
        if cursor_timer >= cursor_interval:
            cursor_blink = not cursor_blink
            cursor_timer = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, None, None
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if name.strip():
                            return True, name.strip()[:max_chars] 
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < max_chars and event.unicode.isprintable():
                        # Solo agregar si no se excede el ancho
                        test_surface = input_font.render(f"Nombre: {name + event.unicode}|", True, color)
                        if test_surface.get_width() <= max_input_width:
                            name += event.unicode
        clock.tick(30)

def show_game_over(screen, score):
    font_name = "Courier"
    font_title = pygame.font.SysFont(font_name, 64, bold=True)
    font_score = pygame.font.SysFont(font_name, 36, bold=True)
    font_msg = pygame.font.SysFont(font_name, 28)
    
    title = font_title.render("GAME OVER", True, (255, 0, 0))
    score_text = font_score.render(f"Tu puntaje: {score}", True, (255, 255, 0))
    msg = font_msg.render("Presiona ENTER para volver al menú", True, (255, 255, 255))
    
    clock = pygame.time.Clock()
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 180))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 280))
        screen.blit(msg, (screen.get_width() // 2 - msg.get_width() // 2, 380))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
        clock.tick(30)

def show_scores_menu(screen, progress):
    font_name = "Courier"
    font_title = pygame.font.SysFont(font_name, 48, bold=True)
    font_option = pygame.font.SysFont(font_name, 36, bold=True)
    
    title = font_title.render("Tabla de Puntajes", True, (255, 255, 0))
    volver_render = font_option.render("Volver", True, (255, 255, 0))
    clock = pygame.time.Clock()
    scores = progress.load_scores(limit=5)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 40))
        draw_score_table(screen, scores)
        screen.blit(volver_render, (screen.get_width() // 2 - volver_render.get_width() // 2, 480))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_SPACE]:
                    return False  # Volver al menú principal
        clock.tick(30)

def show_main_menu(screen, progress, current_skin):
    
    font_name = "Courier"
    font_title = pygame.font.SysFont(font_name, 48, bold=True)
    font_option = pygame.font.SysFont(font_name, 36, bold=True)
    
    title = font_title.render("Space Invaders - UTN", True, (255, 255, 0))
    options = ["Jugar","Seleccionar Nave", "Tabla de posiciones", "Salir"]
    selected = 0
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 80))
        for i, opt in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            opt_render = font_option.render(opt, True, color)
            screen.blit(opt_render, (screen.get_width() // 2 - opt_render.get_width() // 2, 220 + i * 70))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 3  # Salir
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w]:
                    selected = (selected - 1) % 4
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    selected = (selected + 1) % 4
                elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if selected == 1: # Seleccionar Nave
                        new_skin = show_skin_selector(screen, current_skin)
                        if new_skin != current_skin: #Solo actualiza si cambio
                            current_skin = new_skin
                            progress.save_selected_skin(current_skin)
                            print(f"Skin seleccionada y guardada(hud): {current_skin}")
                        return selected
                    elif selected == 2:
                        show_scores_menu(screen, progress)
                        continue
                    else:
                        return selected
        clock.tick(30)

def show_skin_selector(screen, current_skin):
    font_title = pygame.font.SysFont("Courier", 42, bold=True)
    font_option = pygame.font.SysFont("Courier", 28)

    inventory = Inventory()
    unlocked_skins = inventory.get_unlocked_skins()
    if "player0.png" not in unlocked_skins:
        unlocked_skins.insert(0, "player0.png")

    selected = 0
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))

        title = font_title.render("Selecciona tu Nave", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

        skin_name = unlocked_skins[selected]
        skin_number = ''.join(filter(str.isdigit, skin_name)) or "0"
        skin_path = os.path.abspath(os.path.join("..", "assets", "images", skin_name))

        try:
            skin_img = pygame.image.load(skin_path).convert_alpha()
        except:
            skin_img = pygame.Surface((100, 100))
            skin_img.fill((255, 0, 0))

        skin_img = pygame.transform.scale(skin_img, (120, 120))
        screen.blit(skin_img, (WIDTH // 2 - 60, 150))

        label = font_option.render(f"Nave {skin_number}", True, WHITE)
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 290))

        instr1 = font_option.render("← → para elegir", True, WHITE)
        instr2 = font_option.render("ENTER para confirmar", True, WHITE)
        instr3 = font_option.render("ESC para volver", True, WHITE)

        screen.blit(instr1, (WIDTH // 2 - instr1.get_width() // 2, 370))
        screen.blit(instr2, (WIDTH // 2 - instr2.get_width() // 2, 410))
        screen.blit(instr3, (WIDTH // 2 - instr3.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return current_skin
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(unlocked_skins)
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(unlocked_skins)
                elif event.key == pygame.K_RETURN: 
                    return unlocked_skins[selected]
                elif event.key == pygame.K_ESCAPE:
                     return current_skin  # Mantener la actual
        clock.tick(30)
