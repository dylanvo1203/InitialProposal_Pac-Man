import pygame

pygame.init()

WIDTH = 600;
HEIGHT = 600;
FPS = 30;

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")

running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
