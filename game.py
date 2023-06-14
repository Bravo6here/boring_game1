import pygame
import random
pygame.init()
height = 300
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
fps = 60
lets_continue = True
score = 0
font = pygame.font.SysFont("impact", 20)
text = font.render(f"Score: {score}", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.centerx = width // 2
text_rect.centery = 25

plimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\man.png")
plimg_rect = plimg.get_rect()
plimg_rect.center = (width / 2, height / 2)

stimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\star.png")
stimg_rect = stimg.get_rect()
stimg_rect.center = (width // 2, height // 2)

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        key = pygame.key.get_pressed()
        if (key[pygame.K_UP] or key[pygame.K_w]) and plimg_rect.centery > 80:
            plimg_rect.centery -= 10
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and plimg_rect.centery < height - 40:
            plimg_rect.centery += 10
        elif (key[pygame.K_LEFT] or key[pygame.K_a]) and plimg_rect.centerx > 20:
            plimg_rect.centerx -= 10
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and plimg_rect.centerx < width - 30:
            plimg_rect.centerx += 10
    if plimg_rect.colliderect(stimg_rect):
        stimg_rect.x = random.randrange(30, 280, 10)
        stimg_rect.y = random.randrange(80, 280, 10)
        score += 1
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 50), (width, 50))
    screen.blit(plimg, plimg_rect)
    screen.blit(stimg, stimg_rect)
    screen.blit(text, text_rect)
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()