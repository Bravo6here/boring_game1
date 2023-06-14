import pygame

pygame.init()
height = 300
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

lets_continue = True

sqx = width // 2
sqy = height // 2
plimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\man.png")
plimg_rect = plimg.get_rect()
plimg_rect.center = (sqx, sqy)

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        key = pygame.key.get_pressed()
        if (key[pygame.K_UP] or key[pygame.K_w]) and sqy > 0:
            sqy -= 10
        if (key[pygame.K_DOWN] or key[pygame.K_s]) and sqy > 0:
            sqy += 10
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and sqx > 0:
            sqx -= 10
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and sqx > 0:
            sqx += 10
    
    #screen.fill((0, 0, 0))
    screen.blit(plimg, plimg_rect)

    #pygame.display.update()
pygame.quit()