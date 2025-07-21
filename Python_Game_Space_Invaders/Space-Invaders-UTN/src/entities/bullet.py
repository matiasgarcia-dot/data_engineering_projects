import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, image, speed=5, from_player=True):
        super().__init__()
        self.image = pygame.transform.scale(image, (5, 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.direction = direction  # -1 hacia arriba, 1 hacia abajo
        self.from_player = from_player

    def update(self):
        self.rect.y += self.speed * self.direction
        # Eliminar la bala si sale de pantalla
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
