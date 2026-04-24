import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 5
    mode = 'draw'   # draw / rect / circle / erase
    color = (0, 0, 255)
    
    drawing = False
    start_pos = None
    last_pos = None

    screen.fill((0, 0, 0))
    
    while True:
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                # 🎨 COLOR SELECTION
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                
                # 🧰 TOOL SELECTION
                elif event.key == pygame.K_l:
                    mode = 'draw'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rect'
                elif event.key == pygame.K_e:
                    mode = 'erase'

            # 🖱️ START DRAWING
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

            # 🖱️ STOP DRAWING
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

                end_pos = event.pos

                # 🔵 DRAW SHAPES
                if mode == 'rect':
                    rect = pygame.Rect(start_pos, 
                                       (end_pos[0] - start_pos[0],
                                        end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)

                elif mode == 'circle':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, 2)

            # 🖱️ DRAW WHILE MOVING
            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw':
                    pygame.draw.line(screen, color, last_pos, event.pos, radius)
                    last_pos = event.pos

                elif mode == 'erase':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, 10)

        pygame.display.flip()
        clock.tick(60)


main()