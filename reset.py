import pygame
import config
from player import Player

def reset_game():
    return Player(), []

def wait_for_restart(game_screen, font, score, high_score):
    # Show the restart options
    game_screen.fill(config.BLACK)

    restart_text = font.render("Press R to play again", True, config.WHITE)
    game_screen.blit(restart_text, (config.SCREEN_WIDTH // 2 - 120, config.SCREEN_HEIGHT // 2 + 80))

    instructions_text = font.render("Press P for Instructions", True, config.WHITE)
    game_screen.blit(instructions_text, (config.SCREEN_WIDTH // 2 - 120, config.SCREEN_HEIGHT // 2 + 120))

    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart the game
                if event.key == pygame.K_p:  # Show instructions if "P" is pressed
                    instructions_text = font.render("Player Instructions: Use left and right arrows to move.", True, config.WHITE)
                    game_screen.fill(config.BLACK)  # Clear screen before showing instructions
                    game_screen.blit(instructions_text, (config.SCREEN_WIDTH // 2 - 150, config.SCREEN_HEIGHT // 2))
                    pygame.display.flip()

    return False  # Exit the game if no restart
