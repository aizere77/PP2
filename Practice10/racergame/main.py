# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing pygame
pygame.init()

# FPS settings
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COINS = 0   # <-- счетчик монет

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background
background = pygame.image.load("track.png")

# Create screen
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")

# ================= ENEMY =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("opposite.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # Если враг ушёл вниз — увеличиваем счёт
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # Движение влево
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Движение вправо
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin = pygame.image.load("coin.png").convert_alpha()  # картинка монеты
        self.image = pygame.transform.scale(coin, (60, 70))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        # если монета ушла вниз — появится снова
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()   # <-- группа монет
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Event for speed increase
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))

    # Draw score (left top)
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # Draw coins (right top)
    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # Draw and move all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # ===== COLLISION WITH ENEMY =====
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    # ===== COLLISION WITH COIN =====
    collected = pygame.sprite.spritecollide(P1, coins, True)
    if collected:
        COINS += 1

        # создаём новую монету после сбора
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)