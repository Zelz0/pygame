import pygame
import config

def run_welcome_screen(game_screen, font):
    running = True
    while running:
        game_screen.fill(config.BLACK)

        # Hearts
        heart_image = pygame.image.load(config.HEART_IMAGE).convert_alpha()
        heart_image = pygame.transform.scale(heart_image, (40, 40))
        heart_x = (config.SCREEN_WIDTH // 2 - 80)
        heart_y = (config.SCREEN_HEIGHT // 2 - 150)

        for i in range(3):
            game_screen.blit(heart_image, (heart_x + i * 60, heart_y))

        # Welcome Text
        title_text = font.render("Welcome to Food Fall Frenzy!", True, config.WHITE)
        start_text = font.render("Press SPACE to start", True, config.WHITE)
        instructions_text = font.render("Press I for Instructions", True, config.WHITE)
        player_text = font.render("Press P for Player Stats", True, config.WHITE)
        game_screen.blit(player_text, (config.SCREEN_WIDTH // 2 - 120, config.SCREEN_HEIGHT // 2 + 120))
        game_state_text = font.render("Press G for Game State", True, config.WHITE)
        game_screen.blit(game_state_text, (config.SCREEN_WIDTH // 2 - 120, config.SCREEN_HEIGHT // 2 + 70))

        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 60))
        start_rect = start_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        instructions_rect = instructions_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 40))

        game_screen.blit(title_text, title_rect)
        game_screen.blit(start_text, start_rect)
        game_screen.blit(instructions_text, instructions_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Start the game
                    with open(config.STATE_FILE, 'w') as f:
                        f.write("started")
                    running = False  # Exit the welcome screen

                elif event.key == pygame.K_i:
                    # Show the instructions screen when 'I' is pressed
                    show_instructions_screen(game_screen, font)
                elif event.key == pygame.K_p:
                    show_player_stats_screen(game_screen, font)
                elif event.key == pygame.K_g:
                    show_game_state_screen(game_screen, font)
def show_instructions_screen(game_screen, font):
    viewing = True
    while viewing:
        game_screen.fill(config.BLACK)

        # Read instructions from file
        with open(config.INSTRUCTIONS_FILE, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            text = font.render(line.strip(), True, config.WHITE)
            rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, 200 + i * 40))
            game_screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    viewing = False
def show_player_stats_screen(game_screen, font):
    viewing = True
    while viewing:
        game_screen.fill(config.BLACK)

        with open(config.PLAYER_DATA_FILE, "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            text = font.render(line.strip(), True, config.WHITE)
            rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, 200 + i * 40))
            game_screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    viewing = False

def show_game_state_screen(game_screen, font):
    viewing = True
    while viewing:
        game_screen.fill(config.BLACK)

        with open(config.STATE_FILE, "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            text = font.render(line.strip(), True, config.WHITE)
            rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, 200 + i * 40))
            game_screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    viewing = False