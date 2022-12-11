import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Window')
FPS = 30
x1 = 100
y1 = 100
x2 = 400
y2 = 400
width = 50
height = 50
speed = 10
play = True
clock = pygame.time.Clock()
while play:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if x2 >= x1 and x2 <= x1 + width and y2 >= y1 and y2 <= y1 + height:
            play = False
        if x2 + width >= x1 and x2 <= x1 + width and y2 + height >= y1 and y2 <= y1 + height:
            play = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x1 += speed
    if keys[pygame.K_LEFT]:
        x1 -= speed
    if keys[pygame.K_UP]:
        y1 -= speed
    if keys[pygame.K_DOWN]:
        y1 += speed

    if keys[pygame.K_d]:
        x2 += speed
    if keys[pygame.K_a]:
        x2 -= speed
    if keys[pygame.K_w]:
        y2 -= speed
    if keys[pygame.K_s]:
        y2 += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x1, y1, width, height))
    pygame.draw.rect(win, (0, 0, 255), (x2, y2, width, height))
    pygame.display.update()
