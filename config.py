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
PLAYER_SPEED = 0.8

# Item Settings
GOOD_ITEM_IMAGE = "img/good_food.png"
BAD_ITEM_IMAGE = "img/bad_food.png"
GOLDEN_FRUIT_IMAGE = "img/golden_fruit.png"

GOOD_ITEM_SPEED = 4
BAD_ITEM_SPEED = 5
GOLDEN_FRUIT_SPEED = 3

ITEM_WIDTH = 40
ITEM_HEIGHT = 40

# Reading/Writing Files:
STATE_FILE = "game_state.txt"

# ----- Heart/Lives -----
STARTING_LIVES = 3
HEART_IMAGE = "img/Heart.png"

# ----- Score -----
SCORE_FONT = "freesansbold.ttf"
SCORE_TO_WIN = 20
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

SAVE_FILE_PATH = "data/save_data.txt"  # for score saving
