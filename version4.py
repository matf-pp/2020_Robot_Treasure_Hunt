import pygame
import random



white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,128,0)
grey=(220,220,220)

pygame.init()


sirina_ekrana=700
visina_ekrana=720

sirina_polja=50
visina_polja=50


br_redova=10
br_kolona=10

#globalne promenljive
margine=1
pocetna_slika=(15,15)
dis= (sirina_ekrana-45) // br_kolona


ekran = pygame.display.set_mode((sirina_ekrana, visina_ekrana))
pygame.display.set_caption('ROBOT TREASURE HUNT')
clock = pygame.time.Clock()

class Igrac():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.zivoti = 3
        self.image = img_robot
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


class Prepreke():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = img_bomb
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()



def random_koordinate(x,y):
    x=random.randint(0,9)
    y=random.randint(0,9)

    return x,y

def zauzeto(x,y):
    if matrica[x][y]==1:
        return True
    else:
        return False


def nacrtajMrezu(sirina,kolona,ekran):
    #sirina nam je ista kao duzina pa koristimo jednu promenljivu
    razmak= sirina // kolona
    x=0
    y=0

    for l in range(kolona):
        x=x+razmak
        y=y+razmak
        pygame.draw.line(ekran,black,(x,0),(x,sirina))
        pygame.draw.line(ekran,black,(0,y),(sirina,y))
    

img_robot=pygame.image.load("robot.png")
img_tragovi = pygame.image.load("tragovi.png")
img_bomb=pygame.image.load("bomb.png")
img_treasure=pygame.image.load("treasure1.png")
img_live = pygame.image.load("heart.png")
img_live.set_colorkey(black)
img_hurricane = pygame.image.load("hurricane.png")

