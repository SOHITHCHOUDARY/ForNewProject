import pygame
import random
import math
import pygame.gfxdraw


pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls Around Circle")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_COLOR = (255, 100, 100)

# Circle settings
CIRCLE_RADIUS = 150
CIRCLE_POS = (WIDTH // 2, HEIGHT // 2)
CIRCLE_THICKNESS = 3

# Ball settings
BALL_RADIUS = 10
INITIAL_SPEED = 2
ROTATE_TIME = 40  # frames to rotate around circle after touch

# Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        angle = random.uniform(0, math.pi * 2)
        self.dx = math.cos(angle) * INITIAL_SPEED
        self.dy = math.sin(angle) * INITIAL_SPEED
        self.speed = INITIAL_SPEED
        self.rotating = 0  # frames left to rotate
        self.angle_around = 0  # angle around circle for rotation

    def move(self):
        if self.rotating > 0:
            self.angle_around += 0.1
            self.x = CIRCLE_POS[0] + math.cos(self.angle_around) * (CIRCLE_RADIUS + BALL_RADIUS)
            self.y = CIRCLE_POS[1] + math.sin(self.angle_around) * (CIRCLE_RADIUS + BALL_RADIUS)
            self.rotating -= 1
        else:
            self.x += self.dx
            self.y += self.dy

            # Check for circle collision
            dist = math.hypot(self.x - CIRCLE_POS[0], self.y - CIRCLE_POS[1])
            if abs(dist - CIRCLE_RADIUS) <= BALL_RADIUS:
                # Bounce
                nx = (self.x - CIRCLE_POS[0]) / dist
                ny = (self.y - CIRCLE_POS[1]) / dist
                dot = self.dx * nx + self.dy * ny
                self.dx -= 2 * dot * nx
                self.dy -= 2 * dot * ny

                # Start rotating
                self.rotating = ROTATE_TIME
                self.angle_around = math.atan2(self.y - CIRCLE_POS[1], self.x - CIRCLE_POS[0])

                return True  # touched circle

            # Bounce on screen edges
            if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
                self.dx *= -1
            if self.y - BALL_RADIUS < 0 or self.y + BALL_RADIUS > HEIGHT:
                self.dy *= -1

        return False

    def draw(self):
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)


# Initialize balls
balls = [Ball()]

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Draw smooth circle
    pygame.gfxdraw.aacircle(screen, CIRCLE_POS[0], CIRCLE_POS[1], CIRCLE_RADIUS, WHITE)
    pygame.gfxdraw.aacircle(screen, CIRCLE_POS[0], CIRCLE_POS[1], CIRCLE_RADIUS - 1, WHITE)
    pygame.gfxdraw.aacircle(screen, CIRCLE_POS[0], CIRCLE_POS[1], CIRCLE_RADIUS - 2, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw balls
    new_balls = []
    for ball in balls:
        touched = ball.move()
        ball.draw()
        if touched:
            new_balls.append(Ball())  # Add new ball
            for b in balls:  # Increase speed of all balls
                b.dx *= 1.1
                b.dy *= 1.1

    balls.extend(new_balls)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
