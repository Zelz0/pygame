import pygame
import config
import random
from SoundManager import SoundManager
from sprites import Sprite
import Welcome
import highscore
import reset

pygame.init()
pygame.mixer.init()

sound_manager = SoundManager()
game_screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
font = pygame.font.SysFont(None, 30)

high_score = highscore.read_high_score()

# Main game loop
while True:
    Welcome.run_welcome_screen(game_screen, font)

    player, sprites = reset.reset_game()
    pygame.time.set_timer(config.MY_CUSTOM_EVENT, 1000)

    lives = config.STARTING_LIVES
    score = 0
    heart_image = pygame.image.load(config.HEART_IMAGE).convert_alpha()
    heart_image = pygame.transform.scale(heart_image, (30, 30))

    game_over = False
    while not game_over:
        game_screen.fill((0, 0, 0))
        ground = pygame.Surface((config.GROUND_WIDTH, config.GROUND_HEIGHT))
        ground.fill((80, 140, 250))
        game_screen.blit(ground, (0, 760))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == config.MY_CUSTOM_EVENT:
                sprite = Sprite()
                sprites.append(sprite)
                sound_manager.play_sprite_spawn()
                pygame.time.set_timer(config.MY_CUSTOM_EVENT, random.randint(800, 1500))

        keys = pygame.key.get_pressed()
        if player.alive:
            player.move(keys)
            player.draw(game_screen)

        for sprite in sprites[:]:
            sprite.fall()
            sprite.draw(game_screen)

            if sprite.rect.bottom > config.SCREEN_HEIGHT:
                if sprite.type in ["F1", "F2", "F3", "F4", "F5", "F6"]:
                    sound_manager.play_hit_bad()
                    lives -= 1
                sprites.remove(sprite)

            if sprite.rect.colliderect(player.rect) and player.alive:
                if sprite.type in ["F1", "F2", "F3", "F4", "F5", "F6"]:
                    sound_manager.play_catch_good()
                    score += 1
                    sprites.remove(sprite)
                elif sprite.type == "GA":
                    sound_manager.play_golden_fruit()
                    score += 3
                    sprites.remove(sprite)
                elif sprite.type in ["T1", "T2", "T3"]:
                    sound_manager.play_hit_bad()
                    lives -= 1
                    sprites.remove(sprite)

        for i in range(lives):
            heart_x = config.SCREEN_WIDTH - (i + 1) * 40
            heart_y = 10
            game_screen.blit(heart_image, (heart_x, heart_y))

        score_text = font.render(f"Score: {score}", True, config.WHITE)
        game_screen.blit(score_text, (10, 10))

        if score >= 25:
            game_over = True

        if lives <= 0:
            game_over = True

        pygame.display.flip()
        pygame.time.Clock().tick(config.FPS)

    high_score = max(high_score, score)
    highscore.update_high_score(high_score)

    game_screen.fill(config.BLACK)

# Endgame message
    with open(config.ENDGAME_FILE, "r") as file:
        endgame_message = file.read()
    lines = endgame_message.split('\n')
    for i, line in enumerate(lines):
        rendered_line = font.render(line, True, config.WHITE)
        text_rect = rendered_line.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 80 + i * 30))
        game_screen.blit(rendered_line, text_rect)

    final_score_text = font.render(f"Final Score: {score}", True, config.WHITE)
    final_rect = final_score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
    game_screen.blit(final_score_text, final_rect)

    high_score_text = font.render(f"High Score: {high_score}", True, config.WHITE)
    high_rect = high_score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 40))
    game_screen.blit(high_score_text, high_rect)

    restart_text = font.render("Press R to play again", True, config.WHITE)
    restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 100))
    game_screen.blit(restart_text, restart_rect)

    pygame.display.flip()

# Restart Code
    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting_for_restart = False
        pygame.time.Clock().tick(60)
