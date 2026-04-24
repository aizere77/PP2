import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 5
    mode = 'draw'   # draw / rect / circle / erase / square / rtriangle / etriangle / rhombus
    color = (0, 0, 255)
    
    drawing = False
    start_pos = None
    last_pos = None

    screen.fill((0, 0, 0))
    
    while True:
        for event in pygame.event.get():
            
            # Exit conditions
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                # COLOR SELECTION
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                
                # TOOL SELECTION
                elif event.key == pygame.K_l:
                    mode = 'draw'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rect'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                
                # NEW SHAPES
                elif event.key == pygame.K_q:
                    mode = 'square'
                elif event.key == pygame.K_y:
                    mode = 'rtriangle'
                elif event.key == pygame.K_u:
                    mode = 'etriangle'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'

            # START DRAW
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

            # STOP DRAW
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos

                # RECTANGLE
                if mode == 'rect':
                    rect = pygame.Rect(start_pos, 
                                       (end_pos[0] - start_pos[0],
                                        end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)

                # SQUARE (equal sides)
                elif mode == 'square':
                    side = min(abs(end_pos[0] - start_pos[0]),
                               abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(start_pos, (side, side))
                    pygame.draw.rect(screen, color, rect, 2)

                # CIRCLE
                elif mode == 'circle':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    r = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, r, 2)

                # RIGHT TRIANGLE
                elif mode == 'rtriangle':
                    points = [
                        start_pos,
                        (start_pos[0], end_pos[1]),
                        end_pos
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                # EQUILATERAL TRIANGLE
                elif mode == 'etriangle':
                    side = abs(end_pos[0] - start_pos[0])
                    height = int((math.sqrt(3)/2) * side)

                    p1 = (start_pos[0], start_pos[1])
                    p2 = (start_pos[0] + side, start_pos[1])
                    p3 = (start_pos[0] + side//2, start_pos[1] - height)

                    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

                # RHOMBUS
                elif mode == 'rhombus':
                    cx = (start_pos[0] + end_pos[0]) // 2
                    cy = (start_pos[1] + end_pos[1]) // 2

                    points = [
                        (cx, start_pos[1]),
                        (end_pos[0], cy),
                        (cx, end_pos[1]),
                        (start_pos[0], cy)
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

            # DRAW WHILE MOVING
            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw':
                    pygame.draw.line(screen, color, last_pos, event.pos, radius)
                    last_pos = event.pos

                # ERASER
                elif mode == 'erase':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, 10)

        pygame.display.flip()
        clock.tick(60)


main()