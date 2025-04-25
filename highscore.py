import config
import os

def read_high_score():
    if os.path.exists(config.HIGH_SCORE_FILE):
        with open(config.HIGH_SCORE_FILE, 'r') as f:
            content = f.read().strip()
            if content.startswith("High Score:"):
                score_part = content.split(":")[-1].strip()
                if score_part.isdigit():
                    return int(score_part)
    return 0

def update_high_score(new_score):
    high_score = read_high_score()
    if new_score > high_score:
        new_score = min(new_score, 25)
        with open(config.HIGH_SCORE_FILE, 'w') as f:
            f.write(f"High Score:{new_score}")
