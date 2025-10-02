import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

zowo = pygame.image.load("zowo.png")
zowo = pygame.transform.scale(zowo, 
                              (zowo.get_width() / 5,
                               zowo.get_height() / 5))

running = True
x = 0
clock = pygame.time.Clock()

delta_time = 0.1

font = pygame.font.Font(None, size=30)

while running:
    screen.fill((255, 255, 255))

    screen.blit(zowo, (x, 30))

    x += 50 * delta_time

    text = font.render('Hello World', True, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()