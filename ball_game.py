import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Movement Game with Increasing Difficulty")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Player ball
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5

# Target
target_radius = 20
target_x = random.randint(50, WIDTH - 50)
target_y = random.randint(50, HEIGHT - 50)

# Obstacles
obstacles = []
obstacle_speed = 3
spawn_rate = 60  # frames between spawns

# Score
score = 0
start_time = time.time()

running = True
frame_count = 0
last_difficulty_time = 0  # track last difficulty increase

while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
        ball_x += ball_speed
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
        ball_y += ball_speed

    # Draw target
    pygame.draw.circle(screen, GREEN, (target_x, target_y), target_radius)

    # Draw player
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Check collision with target
    if ((ball_x - target_x) ** 2 + (ball_y - target_y) ** 2) ** 0.5 < ball_radius + target_radius:
        score += 1
        target_x = random.randint(50, WIDTH - 50)
        target_y = random.randint(50, HEIGHT - 50)

    # Spawn obstacles
    frame_count += 1
    if frame_count % spawn_rate == 0:
        obs_x = random.choice([0, WIDTH])
        obs_y = random.randint(0, HEIGHT)
        direction = 1 if obs_x == 0 else -1
        obstacles.append([obs_x, obs_y, direction])

    # Move obstacles
    for obs in obstacles:
        obs[0] += obstacle_speed * obs[2]
        pygame.draw.circle(screen, RED, (obs[0], obs[1]), 10)

        # Collision with player
        if ((ball_x - obs[0]) ** 2 + (ball_y - obs[1]) ** 2) ** 0.5 < ball_radius + 10:
            print(f"Game Over! Your score: {score}")
            running = False

    # Increase difficulty every 10 seconds
    elapsed_time = int(time.time() - start_time)
    if elapsed_time - last_difficulty_time >= 10:
        obstacle_speed += 1
        if spawn_rate > 20:
            spawn_rate -= 5
        last_difficulty_time = elapsed_time

    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score} | Time: {elapsed_time}s", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
