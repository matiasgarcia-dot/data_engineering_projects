import pygame
import os
# Constantes para configuración
SCREEN_WIDTH = 800
PLAYER_SIZE = (70, 70)
PLAYER_SPEED = 7
SHOOT_COOLDOWN_FRAMES = 20
MAX_HEALTH = 3

class Player:
    """
    Clase que representa al jugador en el juego.

    Atributos:
        image (pygame.Surface): Imagen del jugador.
        rect (pygame.Rect): Rectángulo que representa la posición y tamaño del jugador.
        shoot_sound (pygame.mixer.Sound): Sonido que se reproduce al disparar.
        speed (int): Velocidad de movimiento del jugador.
        shoot_cooldown (int): Tiempo de espera entre disparos.
        max_health (int): Salud máxima del jugador.
        health (int): Salud actual del jugador.
    """
    

    def __init__(self, screen, position=(400, 550), size=PLAYER_SIZE, speed=PLAYER_SPEED, max_health=MAX_HEALTH, skin_name="player0.png"):
        self.screen = screen
        self.skin_name = skin_name if skin_name else "player0.png"

        """
        Inicializa el jugador con imagen, sonido, posición, velocidad y salud.

        Args:
            position (tuple): Posición inicial del jugador.
            size (tuple): Tamaño de la imagen del jugador.
            speed (int): Velocidad de movimiento.
            max_health (int): Salud máxima.
        """
        
        try:
            base_path = os.path.dirname(__file__)
            # Cargar imagen
            img_path = os.path.abspath(os.path.join(base_path, '..', '..', 'assets', 'images', skin_name))
            self.image = pygame.image.load(img_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
            position = (screen.get_width() // 2, screen.get_height() - 20)
            self.rect = self.image.get_rect(midbottom=position)
            print(f"Skin cargada exitosamente(player): {skin_name}")
            explosion_folder = os.path.abspath(os.path.join(base_path, '..', '..', 'assets', 'images'))
            self.explosion_images = [
                pygame.transform.scale(
                    pygame.image.load(os.path.join(explosion_folder, f'explo{i}.png')).convert_alpha(),
                    PLAYER_SIZE
                )
                for i in range(1, 7)  # 6 imagenes
            ]
        except Exception as e:
            print(f"Error cargando skin (player) {skin_name}: {e}")
            # Cargar skin por defecto si hay error
        
        # Cargar sonido
        sound_path = os.path.abspath(os.path.join(base_path, '..', '..', 'assets', 'sounds', 'shoot.wav'))
        try:
            self.shoot_sound = pygame.mixer.Sound(sound_path)
            self.shoot_sound.set_volume(0.2)
        except pygame.error as e:
            print(f"No se pudo cargar el sonido: {e}")
            self.shoot_sound = pygame.mixer.Sound(buffer=bytes([128] * 1000))

        self.speed = speed
        self.shoot_cooldown = 0
        self.max_health = max_health
        self.health = max_health

    def handle_movement(self, keys):
        """
        Maneja el movimiento del jugador según las teclas presionadas.

        Args:
            keys (pygame.key.get_pressed): Estado de las teclas.
        """
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Limitar dentro de la pantalla
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

    def update(self, keys):
        """
        Actualiza el estado del jugador (movimiento y cooldown de disparo).

        Args:
            keys (pygame.key.get_pressed): Estado de las teclas.
        """
        self.handle_movement(keys)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def can_shoot(self):
        """
        Verifica si el jugador puede disparar.

        Returns:
            bool: True si puede disparar, False si está en cooldown.
        """
        return self.shoot_cooldown == 0

    def shoot(self):
        """
        Ejecuta el disparo si no está en cooldown.

        Returns:
            bool: True si disparó, False si no.
        """
        if self.can_shoot():
            self.shoot_sound.play()
            self.reset_shoot_cooldown()
            return True
        return False

    def reset_shoot_cooldown(self):
        """Reinicia el cooldown de disparo."""
        self.shoot_cooldown = SHOOT_COOLDOWN_FRAMES

    def take_damage(self, amount=1):
        """
        Reduce la salud del jugador.

        Args:
            amount (int): Cantidad de daño recibido.
        """
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            for img in self.explosion_images:
                self.screen.fill((0, 0, 0))  # limpia la pantalla
                self.screen.blit(img, self.rect.topleft)
                pygame.display.flip()
                pygame.time.delay(200)  # Tiempo entre frames 
            self.on_death()

    def on_death(self):
        """Lógica que se ejecuta cuando el jugador muere."""
        print("¡El jugador ha muerto!")
        # Aquí podrías reiniciar el juego, mostrar Game Over, etc.

    def draw(self, screen):
        """
        Dibuja al jugador y su barra de salud en la pantalla.

        Args:
            screen (pygame.Surface): Superficie donde se dibuja.
        """
        screen.blit(self.image, self.rect)

        # Barra de salud
        bar_width = self.rect.width
        bar_height = 5
        bar_x = self.rect.x
        bar_y = self.rect.y + 70
        fill = (self.health / self.max_health) * bar_width

        # Fondo rojo
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        # Parte verde proporcional a la salud
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, fill, bar_height))
