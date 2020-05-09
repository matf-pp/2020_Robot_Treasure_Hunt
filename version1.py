import pygame
import random




WIDTH = 69
HEIGHT = 69
MARGIN = 1
W = 700
H= 700
FPS = 60 #speed, frame per second


GREY = (70, 70, 70)
GREY_1 = (30, 30, 30)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (90, 200, 50)
BLUE = (0,0, 255)
YELLOW = (255, 255, 0)

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

pygame.init()


WINDOW_SIZE = [700, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Robot treasure hunt")


clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-90
        self.rect = self.image.get_rect()
        self.radius = 25
        self.radius = int(self.rect.width*.9 / 2)
        self.speedx = 0
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


player_img = pygame.image.load("robot.png").convert()
bomb_img = pygame.image.load("bomb.png").convert()
treasure_img = pygame.image.load("treasure.png").convert()
player_img_mini = pygame.transform.scale(player_img, (25, 19))
player_img_mini.set_colorkey(BLACK)


pygame.display.flip()

pygame.quit() 

