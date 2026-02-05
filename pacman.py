import pygame
import sys

pygame.init()

WIDTH = 600;
HEIGHT = 600;
FPS = 30;

# Colors
BLACK = (0, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Creating the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")
clock = pygame.time.Clock()

# Position of player (starts in middle)
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_size = 20
player_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)


# Lives

# Pellets
pellets = []
for x in range(50, WIDTH - 50, 80):
    for y in range(50, HEIGHT - 50, 80):
        pellets.append([x ,y])


# Ghosts

# Game loop
running = True;
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed  

    # Keep player on screen
    player_x = max(0, min(player_x, WIDTH - player_size))
    player_y = max(0, min(player_y, HEIGHT - player_size))

    pellets_to_collect = []
    for pellet in pellets:
        pellet_x, pellet_y = pellet
        # finding distanace between player and pellet
        # y = 
        distance = ((player_x - pellet_x) ** 2 + (player_y - pellet_y) ** 2) ** 0.5
        # if player is close enough to pellet, collect it
        if distance < player_size + 5: # "+5" to account for pellet radius
            pellets_to_collect.append(pellet)
            score += 10  

    # Remove collected pellets
    for pellet in pellets_to_collect:
        pellets.remove(pellet)  

    # Screen background
    screen.fill(BLACK)

    # Spawn pellets
    for pellet in pellets:
        pygame.draw.circle(screen, (WHITE), pellet, 5)

    pygame.draw.circle(screen, YELLOW, (player_x, player_y), player_size)

    score_text = font.render(f"Score: {score}", True, (WHITE))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()


pygame.quit()
sys.exit()
