import pygame

pygame.init()

width = 600
height = 600
radius = 25
step = 20
x = width // 2
y = height // 2

window = pygame.display.set_mode((width, height))
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            break
        elif e.type == pygame.KEYDOWN:
            dx, dy = x, y
            if e.key == pygame.K_UP:
                dy -= step
            elif e.key == pygame.K_DOWN:
                dy += step
            elif e.key == pygame.K_LEFT:
                dx -= step
            elif e.key == pygame.K_RIGHT:
                dx += step
            
            if dx - radius < 0 or dx + radius > width:
                dx = x
            if dy - radius < 0 or dy + radius > height:
                dy = y

            x, y = dx, dy

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (255, 0, 0), (x, y), radius)
    pygame.display.flip()

pygame.quit()