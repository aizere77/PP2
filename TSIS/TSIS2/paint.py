import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

# --- SETTINGS ---
WIDTH, HEIGHT = 900, 600
TOOLBAR_HEIGHT = 100   # теперь 2 строки

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

color = (0, 0, 0)
brush_size = 2
tool = "pencil"

drawing = False
start_pos = None

# text
font = pygame.font.SysFont(None, 24)
text_input = ""
text_pos = None
typing = False

clock = pygame.time.Clock()

# --- TOOLS ---
tools_list = ["pencil", "line", "rect", "circle", "fill", "text"]
tool_buttons = []

button_width = WIDTH // len(tools_list)

for i, t in enumerate(tools_list):
    rect = pygame.Rect(i * button_width, 0, button_width, 50)
    tool_buttons.append((rect, t))

# --- COLORS (SECOND ROW) ---
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 255, 255)
]

color_buttons = []
color_size = 40

for i, c in enumerate(colors):
    rect = pygame.Rect(i * color_size + 5, 55, color_size - 5, color_size - 5)
    color_buttons.append((rect, c))

# --- MAIN LOOP ---
while True:
    screen.fill((200, 200, 200))

    # canvas
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- KEYBOARD ---
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("image_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            if typing:
                if event.key == pygame.K_RETURN:
                    render_text(canvas, text_input, text_pos, font, color)
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        # --- MOUSE ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # toolbar (две строки)
            if y < TOOLBAR_HEIGHT:

                # COLORS FIRST
                for rect, c in color_buttons:
                    if rect.collidepoint(x, y):
                        color = c
                        break
                else:
                    # TOOLS
                    for rect, t in tool_buttons:
                        if rect.collidepoint(x, y):
                            tool = t

                continue

            y -= TOOLBAR_HEIGHT

            if tool == "fill":
                flood_fill(canvas, x, y, color)

            elif tool == "text":
                text_pos = (x, y)
                typing = True
                text_input = ""

            else:
                drawing = True
                start_pos = (x, y)

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            y -= TOOLBAR_HEIGHT

            if tool == "line" and start_pos:
                draw_line(canvas, color, start_pos, (x, y), brush_size)

            drawing = False
            start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                x, y = event.pos
                y -= TOOLBAR_HEIGHT
                draw_pencil(canvas, color, (x, y), brush_size)

    # --- LINE PREVIEW ---
    if drawing and tool == "line" and start_pos:
        mx, my = pygame.mouse.get_pos()
        my -= TOOLBAR_HEIGHT

        draw_line(
            screen,
            color,
            (start_pos[0], start_pos[1] + TOOLBAR_HEIGHT),
            (mx, my + TOOLBAR_HEIGHT),
            brush_size
        )

    # --- TEXT PREVIEW ---
    if typing and text_pos:
        img = font.render(text_input, True, color)
        screen.blit(img, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

    # --- TOOLBAR DRAW ---
    # линия разделения
    pygame.draw.line(screen, (0, 0, 0), (0, 50), (WIDTH, 50), 2)

    # tools (верх)
    for rect, t in tool_buttons:
        if t == tool:
            pygame.draw.rect(screen, (150, 150, 255), rect)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rect)

        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        txt = font.render(t, True, (0, 0, 0))
        screen.blit(txt, (rect.x + 10, rect.y + 10))

    # colors (низ)
    for rect, c in color_buttons:
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        if c == color:
            pygame.draw.rect(screen, (255, 255, 255), rect, 3)

    pygame.display.flip()
    clock.tick(60)