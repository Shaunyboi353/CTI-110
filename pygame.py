import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30
CAR_WIDTH, CAR_HEIGHT = 40, 70
TRACK_COLOR = (50, 50, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crazy Racers")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.quit()