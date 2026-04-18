import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

bg = pygame.image.load("images/mainclock.png")
bg = pygame.transform.scale(bg, (1200,800))

left = pygame.image.load("images/leftarm.png").convert_alpha()
right = pygame.image.load("images/rightarm.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    angle_min = -(minutes * 6)
    angle_sec = -(seconds * 6)

    center = (600, 400)


    r_img = pygame.transform.rotate(right, angle_min)
    l_img = pygame.transform.rotate(left, angle_sec)

    screen.blit(r_img, r_img.get_rect(center=center))
    screen.blit(l_img, l_img.get_rect(center=center))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()