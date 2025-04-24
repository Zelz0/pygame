import pygame
import random
import config


class Sprite:
    def __init__(self):
        self.type = random.choice(["F1", "F2", "F3", "F4", "F5", "F6", "GF", "T1", "T2","T3"])
        self.speed = config.SPRITE_SPEEDS[self.type]
        self.sprite = pygame.image.load(random.choice(config.SPRITE_PATHS[self.type])).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (random.randint(0, config.SCREEN_WIDTH - self.rect.width), 0)
        #self.spawn_sound = pygame.mixer.Sound(random.choice(config.SPRITE_SPAWN_SOUNDS))

    def fall(self):
        self.rect.move_ip(0, self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
