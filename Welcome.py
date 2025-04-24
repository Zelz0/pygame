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
                    with open(config.STATE_FILE, 'w') as f:
                        f.write("started")
                    running = False

                elif event.key == pygame.K_i:
                    show_instructions_screen(game_screen, font)

def show_instructions_screen(game_screen, font):
    viewing = True
    while viewing:
        game_screen.fill(config.BLACK)

        # Instructions
        lines = [
            "How to Play:",
            "- Use A/D keys to move the cart left/right.",
            "- Catch food to earn points, avoid trash to stay alive!",
            "- Golden fruits give extra points!",
            "- The goal is to earn 25 points without dying.",
            "Press B to go back."
        ]

        for i, line in enumerate(lines):
            text = font.render(line, True, config.WHITE)
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
