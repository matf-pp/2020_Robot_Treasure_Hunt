import pygame
import random
import numpy
import math

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
    


def nacrtajIgraca(igrac):
    ekran.blit(img_robot,(pocetna_slika[0] + dis * igrac.x,pocetna_slika[1] + dis * igrac.y))


def nacrtajBlago(blago):
    ekran.blit(img_treasure,(pocetna_slika[0] + dis * blago.x,pocetna_slika[1] + dis * blago.y))

def random_koordinate_prepreke(prepreka):
    prepreka.x,prepreka.y=random_koordinate(prepreka.x,prepreka.y)

    while zauzeto(prepreka.x,prepreka.y):
        prepreka.x,prepreka.y=random_koordinate(prepreka.x,prepreka.y)

    matrica[prepreka.x][prepreka.y]=1

def napravi_random_prepreke(lista_prepreka):
    for i in range(10):
        prepr=Prepreke()
        random_koordinate_prepreke(prepr)

        lista_prepreka.append(prepr)

def NacrtajPrepreke(lista_prepreka):
    for p in lista_prepreka:
        ekran.blit(img_bomb,(pocetna_slika[0] + dis * p.x,pocetna_slika[1] + dis * p.y))
       



img_robot=pygame.image.load("robot.png")
img_tragovi = pygame.image.load("tragovi.png")
img_bomb=pygame.image.load("bomb.png")
img_treasure=pygame.image.load("treasure1.png")
img_live = pygame.image.load("heart.png")
img_live.set_colorkey(black)
img_hurricane = pygame.image.load("hurricane.png")




def igra():
    kraj=False
    zivoti=3
    global matrica
    matrica=numpy.zeros((br_kolona+1,br_kolona+1))

    b_x=0
    b_y=0

    b_x,b_y=random_koordinate(b_x,b_y)
    blago=Blago(b_x,b_y)

    lista_prepreka=[]

    napravi_random_prepreke(lista_prepreka)

    b_x,b_y=random_koordinate(b_x,b_y)
    while zauzeto(b_x,b_y):
        b_x,b_y=random_koordinate(b_x,b_y)

    igrac=Igrac(b_x,b_y)

    while not kraj:
        
        ekran.fill(white)
        nacrtajMrezu(sirina_ekrana,br_kolona,ekran)
        nacrtajIgraca(igrac)
        NacrtajPrepreke(lista_prepreka)
        nacrtajBlago(blago)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                kraj=True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pomeri_levo_igraca(igrac,blago,zivoti)
                if event.key==pygame.K_RIGHT:
                    pomeri_desno_igraca(igrac,blago,zivoti)
                if event.key==pygame.K_UP:
                    pomeri_gore_igraca(igrac,blago,zivoti)
                if event.key==pygame.K_DOWN:
                    pomeri_dole_igraca(igrac,blago,zivoti)
                
        if izgubio or nadjeno_blago:
            kraj=True





