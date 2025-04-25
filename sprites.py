import pygame
import random
import config


class Sprite:
    def __init__(self):
        self.type = random.choice(["F1", "F2", "F3", "F4", "F5", "F6", "GA", "T1", "T2", "T3"])
        self.speed = config.SPRITE_SPEEDS[self.type]
        image_path = random.choice(config.SPRITE_PATHS[self.type])
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (config.ITEM_WIDTH, config.ITEM_HEIGHT))
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (random.randint(0, config.SCREEN_WIDTH - self.rect.width), 0)
        self.spawn_sound = pygame.mixer.Sound(config.SPRITE_SPAWN_SOUND)

    def fall(self):
        self.rect.move_ip(0, self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
