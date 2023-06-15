import pygame
import random
pygame.init()
# Initialize
height = 300
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
fps = 60
lets_continue = True
score = 0
collision = pygame.mixer.Sound(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\Untitled.mp3")
is_ai = False
is_x = False
is_y = False
# Player image
plimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\man.png")
plimg_rect = plimg.get_rect()
plimg_rect.center = (width / 2, height / 2)
# Starcoin image
stimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\game1\boring_game1\star.png")
stimg_rect = stimg.get_rect()
stimg_rect.center = (width // 2 - 100, height // 2)
    
# Main loop
while lets_continue:
    # Checking for quiting and key pressing
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
    elif key[pygame.K_q]:
        if is_ai == True:
            is_ai = False
            is_x = False
            is_y = False
        else:
            is_ai = True
    # AI algorithm
    if is_ai == True:
        if is_x == False:
            if plimg_rect.centerx > stimg_rect.centerx + 10:
                plimg_rect.centerx -= 10
            elif plimg_rect.centerx < stimg_rect.centerx - 10:
                plimg_rect.centerx += 10
            else:
                is_x = True
        if is_y == False and is_x == True:
            if plimg_rect.centery > stimg_rect.centery + 10:
                plimg_rect.centery -= 10
            elif plimg_rect.centery < stimg_rect.centery - 10:
                plimg_rect.centery += 10
            else:
                is_y = True

    # Collision with starcoin
    if plimg_rect.colliderect(stimg_rect):
        continue_coll_func = True
        while continue_coll_func:
            stimg_rect.x = random.randrange(30, 580, 10)
            stimg_rect.y = random.randrange(80, 280, 10)
            if abs(stimg_rect.centerx - plimg_rect.centerx) > 30 and abs(stimg_rect.centery - plimg_rect.centery) > 30:
                continue_coll_func = False        
        score += 1
        collision.play()
        is_x = False
        is_y = False
    # Getting everything on screen
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 50), (width, 50))
    font = pygame.font.SysFont("impact", 20)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = width // 2
    text_rect.centery = 25
    screen.blit(plimg, plimg_rect)
    screen.blit(stimg, stimg_rect)
    screen.blit(text, text_rect)
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()