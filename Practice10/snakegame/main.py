import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 20)

# Snake initial position
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL, 0)

# Food
food = None

# Game variables
score = 0
level = 1
speed = 7


# Function to generate food (not on snake)
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)


food = generate_food()


# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Control snake direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            if event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            if event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # Border collision (game over)
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Hit wall")
        pygame.quit()
        sys.exit()

    # Self collision
    if new_head in snake:
        print("Game Over! Hit itself")
        pygame.quit()
        sys.exit()

    # Add new head
    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1

        # Increase level every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2  # increase speed

        food = generate_food()
    else:
        snake.pop()  # remove tail if not eating

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    # Draw score & level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.update()
    clock.tick(speed)