import pygame
pygame.init()

#  Window Settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Food Fall Frenzy"
GROUND_HEIGHT = 50
GROUND_WIDTH = 600
FPS = 60

#  Player Settings
PLAYER_SPEED = 10

# Item Speed
SPRITE_SPEEDS = {"F1": 10,"F2": 11,"F3": 12,"F4": 12, "F5": 10,"F6": 11,"GA": 12,"T1": 12,"T2": 12,"T3": 12}

# Item Images
SPRITE_PATHS = {"F1": ["img/F1.png"],
                "F2": ["img/F2.png"],
                "F3": ["img/F3.png"],
                "F4": ["img/F4.png"],
                "F5": ["img/F5.png"],
                "F6": ["img/F6.png"],
                "GA": ["img/GA.png"],
                "T1": ["img/T1.png"],
                "T2": ["img/T2.png"],
                "T3": ["img/T3.png"]
                }

ITEM_WIDTH = 40
ITEM_HEIGHT = 40

# Reading/Writing Files:
STATE_FILE = "ReadWriteFiles/game_state.txt"
HIGH_SCORE_FILE = "ReadWriteFiles/high_scores.txt"
PLAYER_DATA_FILE = "ReadWriteFiles/player_data.txt"
INSTRUCTIONS_FILE = "ReadWriteFiles/instructions.txt"

# ----- Heart/Lives -----
STARTING_LIVES = 3
HEART_IMAGE = "img/Heart.png"

# ----- Score -----
SCORE_FONT = "freesansbold.ttf"
SCORE_TO_WIN = 25
SCORE_COLOR = (255, 255, 255)

# ----- Colors -----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)

# ----- File Paths -----
SOUND_GOOD_CATCH = "audio/play_good_catch.wav.wav"
SOUND_BAD_CATCH = "audio/play_bad_catch.wav.wav"
SOUND_GOLDEN_FRUIT = "audio/play_golden_fruit.wav.wav"
SOUND_GAME_OVER = "audio/play_game_over.wav.wav"