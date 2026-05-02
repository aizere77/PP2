import pygame

def draw_pencil(surface, color, pos, size):
    pygame.draw.circle(surface, color, pos, size)

def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_rectangle(surface, color, start, end, size):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, color, start, end, size):
    radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, size)

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if px < 0 or py < 0 or px >= surface.get_width() or py >= surface.get_height():
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        stack.extend([(px+1, py), (px-1, py), (px, py+1), (px, py-1)])

def render_text(surface, text, pos, font, color):
    img = font.render(text, True, color)
    surface.blit(img, pos)