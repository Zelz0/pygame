# SoundManager.py

import pygame
from config import *

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.catch_good = pygame.mixer.Sound(SOUND_GOOD_CATCH)
        self.hit_bad = pygame.mixer.Sound(SOUND_BAD_CATCH)
        self.golden_fruit = pygame.mixer.Sound(SOUND_GOLDEN_APPLE)
        self.game_over = pygame.mixer.Sound(SOUND_GAME_OVER)
        self.sprite_spawn = pygame.mixer.Sound(SPRITE_SPAWN_SOUND)
    def play_catch_good(self):
        self.catch_good.play()

    def play_hit_bad(self):
        self.hit_bad.play()

    def play_golden_fruit(self):
        self.golden_fruit.play()

    def play_game_over(self):
        self.game_over.play()

    def play_sprite_spawn(self):
        self.sprite_spawn.play()