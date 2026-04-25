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
BLACK = (0, 0, 0)

# Food colors (different types)
FOOD_TYPES = [
    {"color": (255, 0, 0), "value": 1},   # small
    {"color": (255, 165, 0), "value": 2}, # medium
    {"color": (255, 255, 0), "value": 3}  # big
]

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 20)

# Snake initial position
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL, 0)

# Game variables
score = 0
level = 1
speed = 7

# Food variables
food = None
food_type = None
food_spawn_time = 0
FOOD_LIFETIME = 5000  # milliseconds (5 seconds)


# Generate food (with random type and safe position)
def generate_food():
    global food_type, food_spawn_time

    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        if (x, y) not in snake:
            food_type = random.choice(FOOD_TYPES)  # choose random type
            food_spawn_time = pygame.time.get_ticks()  # start timer
            return (x, y)


food = generate_food()


# Main game loop
while True:
    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()

    # ⏱ If food expired → generate new one
    if current_time - food_spawn_time > FOOD_LIFETIME:
        food = generate_food()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    # Border collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Hit wall")
        pygame.quit()
        sys.exit()

    # Self collision
    if new_head in snake:
        print("Game Over! Hit itself")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += food_type["value"]  # add based on weight

        # Level system
        if score % 5 == 0:
            level += 1
            speed += 1

        food = generate_food()
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # Draw food (color depends on type)
    pygame.draw.rect(screen, food_type["color"], (*food, CELL, CELL))

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.update()
    clock.tick(speed)