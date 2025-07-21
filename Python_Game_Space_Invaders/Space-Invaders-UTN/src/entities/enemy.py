import pygame
import os
import random
from entities.bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=2, health=4):
        super().__init__()
        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, '..', '..', 'assets', 'images', 'enemy.png')
        img_path = os.path.abspath(img_path)

        # Cargar imagen base y escalarla
        self.base_image = pygame.image.load(img_path).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (60, 60))
        self.image = self.base_image.copy()

        # Obtener rectángulo desde imagen y ubicar en (x, y)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = speed
        self.health = health
        self.max_health = health
        self.direction = 1  # 1: derecha, -1: izquierda
        self.bounce_count = 0  # Cuenta los rebotes para saltos crecientes

        # Shooting mechanics
        self.shoot_cooldown = 0
        self.shoot_delay = random.randint(60, 180)  # Random delay between 1-3 seconds at 60 FPS
        self.shoot_chance = 0.005  # 0.5% chance per frame to shoot

        self.update_tint()

    def update_tint(self):
        # Define tint colors for different health levels
        if self.health >= self.max_health * 0.75:
            tint_color = (0, 255, 0)  # Green
        elif self.health >= self.max_health * 0.5:
            tint_color = (255, 255, 0)  # Yellow
        elif self.health >= self.max_health * 0.25:
            tint_color = (255, 140, 0)  # Orange
        else:
            tint_color = (255, 0, 0)  # Red

        # Create a tinted copy of the base image
        self.image = self.base_image.copy()

        # Apply tint pixel by pixel (slower but more precise)
        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                pixel = self.image.get_at((x, y))
                if pixel.a > 0:  # If pixel is not transparent
                    # Blend the tint color with the original pixel
                    new_r = min(pixel.r + tint_color[0] // 1.5, 255)
                    new_g = min(pixel.g + tint_color[1] // 1.5, 255)
                    new_b = min(pixel.b + tint_color[2] // 1.5, 255)
                    self.image.set_at((x, y), (new_r, new_g, new_b, pixel.a))

    def update(self):
        # Movimiento horizontal
        self.rect.x += self.speed * self.direction

        # Cambio de dirección al llegar al borde de la pantalla
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direction *= -1
            self.bounce_count += 1
            self.rect.y += 10 + 3 * self.bounce_count  # Salto más grande cada vez

        # Update shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def can_shoot(self):
        """Check if enemy can shoot (cooldown finished and random chance)"""
        return self.shoot_cooldown == 0 and random.random() < self.shoot_chance

    def shoot(self, bullet_image):
        """Create and return an enemy bullet"""
        if self.can_shoot():
            self.shoot_cooldown = self.shoot_delay
            return Bullet(self.rect.centerx, self.rect.bottom, 1, bullet_image, speed=4, from_player=False)
        return None

    def draw(self, screen):
        # Dibujar imagen en la posición actual
        screen.blit(self.image, self.rect)

    def take_damage(self):
        self.health -= 1
        self.update_tint()
        if self.health <= 0:
            # Reproducir sonido ANTES de kill()
            base_path = os.path.dirname(__file__)
            sound_path = os.path.join(base_path, '..', '..', 'assets', 'sounds', 'invaderkilled.wav')
            sound_path = os.path.abspath(sound_path)

            try:
                death_sound = pygame.mixer.Sound(sound_path)
                death_sound.set_volume(0.2)
                death_sound.play()  # ¡Aquí está lo que faltaba!
            except Exception as e:
                print(f"No se pudo cargar/reproducir el sonido: {e}")
                # Sonido de emergencia
                fallback_sound = pygame.mixer.Sound(buffer=bytes([128] * 1000))
                fallback_sound.play()

            self.kill()  # Ahora eliminamos al enemigo después del sonido
