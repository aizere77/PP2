# ================= IMPORTS =================
import pygame, sys
from pygame.locals import *
import random, time

# ================= INIT =================
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# ================= COLORS =================
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ================= SCREEN =================
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# ================= GAME VARIABLES =================
SPEED = 5
SCORE = 0
COINS = 0

# ================= FONTS =================
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# ================= BACKGROUND =================
background = pygame.image.load("track.png")

# ================= COIN TYPES =================
# Different weights and sizes
COIN_TYPES = [
    {"value": 1, "size": (40, 50)},
    {"value": 2, "size": (50, 60)},
    {"value": 3, "size": (60, 70)}
]

# ================= ENEMY =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("opposite.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE

        # Move enemy down
        self.rect.move_ip(0, SPEED)

        # If enemy leaves screen → reset position
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

        # Move left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Move right
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 🔹 Choose random coin type
        self.type = random.choice(COIN_TYPES)

        coin_img = pygame.image.load("coin.png").convert_alpha()

        # 🔹 Resize depending on weight
        self.image = pygame.transform.scale(coin_img, self.type["size"]).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        # Move coin down
        self.rect.move_ip(0, SPEED)

        # If coin leaves screen → respawn
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

# ================= OBJECTS =================
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# ================= SPEED EVENT =================
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2   # gradual increase

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))

    # Draw score
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # Draw coins counter
    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # Draw and move objects
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # ================= COLLISION ENEMY =================
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    # ================= COLLISION COINS =================
    collected = pygame.sprite.spritecollide(P1, coins, True)

    if collected:
        for coin in collected:
            # 🔹 Add value depending on coin type
            COINS += coin.type["value"]

        # 🔹 Increase difficulty every 5 coins
        if COINS % 5 == 0:
            SPEED += 1   # enemy speed increases

        # 🔹 Spawn new coin
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)