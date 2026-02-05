import pygame

pygame.init()

WIDTH = 600;
HEIGHT = 600;
FPS = 30;

BLACK = (0, 0 ,0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")
clock = pygame.time.Clock()


player_x = WIDTH // 2
player_y = HEIGHT // 2
player_size = 20
player_speed = 5




running = True;
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed       

    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (player_x, player_y), player_size)

    pygame.display.flip()


pygame.quit()
