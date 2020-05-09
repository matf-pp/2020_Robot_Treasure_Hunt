import pygame
import random
import math
import numpy
    
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,128,0)
tr=(70,70,70)

pygame.init()


sirina_ekrana=700
visina_ekrana=720

sirina_polja=50
visina_polja=50
all_sprites = pygame.sprite.Group()
prepreke = pygame.sprite.Group()

br_redova=10
br_kolona=10




#globalne promenljive
margine=1
nadjeno_blago=False
izgubio=False
pocetna_slika=(15,15)
dis= (sirina_ekrana-45) // br_kolona

ekran = pygame.display.set_mode((sirina_ekrana, visina_ekrana))
pygame.display.set_caption('ROBOT TREASURE HUNT')
clock = pygame.time.Clock()

class Prepreke(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = img_bomb
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()



class Igrac(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.zivoti = 3
        self.image = img_robot
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()



class Blago(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.image = img_treasure
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        matrica[x][y]=1
    def nacrtajBlago(self): 
        ekran.blit(img_treasure,(pocetna_slika[0] + dis * self.x,pocetna_slika[1] + dis * self.y))



img_robot=pygame.image.load("robot.png")
img_bomb=pygame.image.load("bomb.png")
img_treasure=pygame.image.load("treasure.png")
img_robot_mini = pygame.transform.scale(img_robot, (45, 39))
img_robot_mini.set_colorkey(black)




def random_koordinate(x,y):
    x=random.randint(1,9)
    y=random.randint(1,9)

    return x,y


def zauzeto(x,y):
    if matrica[x][y]==1:
        return True
    else:
        return False

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
        #pygame.draw.circle(ekran, red, (nep.x,nep.y), nep.r)

def nacrtajZivote(ekran, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x -90+i*50
        img_rect.y = y
        ekran.blit(img, img_rect)

def nacrtajIgraca(igrac):
    ekran.blit(img_robot,(pocetna_slika[0] + dis * igrac.x,pocetna_slika[1] + dis * igrac.y))

def nacrtajMrezu(sirina,kolona,ekran):
    #sirina nam je ista kao duzina pa koristimo jednu promenljivu
    razmak= (sirina-40) // kolona
    x=0
    y=0

    for l in range(kolona):
        x=x+razmak
        y=y+razmak
        pygame.draw.line(ekran,black,(x,66),(x,sirina-40))
        pygame.draw.line(ekran,black,(66,y),(sirina-40,y))



def pomeri_levo_igraca(igrac,blago,zivoti):
    b_x=blago.x
    b_y=blago.y
    
    if igrac.x > 1:
        igrac.x=igrac.x-1

    x=igrac.x
    y=igrac.y
#broj kolona i redova je isti pa je svejedno koju promenljivu koristimo
    if x < 0:
        igrac.x = 0
    elif x > br_kolona - 1:
        igrac.x = br_kolona - 1
    
    x=igrac.x
    y=igrac.y
    matrica[x][y] = 1
    
    
    if b_x == x and b_y==y:
        nadjeno_blago = True
        krajnjiEkran()

    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                krajnjiEkran1()
            else:
                igrac.zivoti -= 1
        
       
                 

def pomeri_desno_igraca(igrac,blago,zivoti):
    b_x=blago.x
    b_y=blago.y

    igrac.x=igrac.x+1

    x=igrac.x
    y=igrac.y
#broj kolona i redova je isti pa je svejedno koju promenljivu koristimo
    if x < 0:
        igrac.x=0
    elif x > br_kolona - 1:
        igrac.x= br_kolona - 1
    
    x=igrac.x
    y=igrac.y
    matrica[x][y] = 1
    
    
    if b_x == x and b_y==y:
        nadjeno_blago=True
        krajnjiEkran()
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                krajnjiEkran1()
            else:
                igrac.zivoti -= 1
        
    
def pomeri_gore_igraca(igrac,blago,zivoti):
    b_x=blago.x
    b_y=blago.y
    if igrac.y > 1:
        igrac.y=igrac.y-1

    x=igrac.x
    y=igrac.y
#broj kolona i redova je isti pa je svejedno koju promenljivu koristimo

    if y < 0:
        igrac.y=0
    elif y > br_kolona - 1:
        igrac.y= br_kolona - 1
    x=igrac.x
    y=igrac.y
    matrica[x][y] = 1
    
    
    if b_x == x and b_y==y:
        nadjeno_blago=True
        krajnjiEkran()

        
    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                krajnjiEkran1()
            else:
                igrac.zivoti -= 1
        
        
            
 
def pomeri_dole_igraca(igrac,blago,zivoti):
    b_x=blago.x
    b_y=blago.y
   

    x=igrac.x
    if igrac.y > sirina_ekrana - 40:
        igra.y = sirina_ekrana - 40
    igrac.y=igrac.y+1
    y=igrac.y
#broj kolona i redova je isti pa je svejedno koju promenljivu koristimo
    
    if y < 0:
        igrac.y=0
    elif y > br_kolona - 1:
        igrac.y= br_kolona - 1
    
    x=igrac.x
    y=igrac.y
    matrica[x][y] = 1
    
    
    if b_x == x and b_y==y:
        nadjeno_blago=True
        krajnjiEkran()
    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                krajnjiEkran1()
            else:
                igrac.zivoti -= 1
        

    

def igra():
    kraj=False 
    zivoti=3
    global matrica
    matrica=numpy.zeros((br_kolona+1,br_redova+1))

    b_x=0
    b_y=0

    b_x,b_y=random_koordinate(b_x,b_y)
    blago=Blago(b_x,b_y)

    global lista_prepreka
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
        blago.nacrtajBlago()
        nacrtajZivote(ekran, sirina_ekrana-100, 5, igrac.zivoti,img_robot_mini)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                kraj=True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pomeri_levo_igraca(igrac,blago,igrac.zivoti)
    
                if event.key==pygame.K_RIGHT:
                    pomeri_desno_igraca(igrac,blago,igrac.zivoti)
                    
                if event.key==pygame.K_UP:
                    pomeri_gore_igraca(igrac,blago,igrac.zivoti)
                   
                if event.key==pygame.K_DOWN:
                    pomeri_dole_igraca(igrac,blago,igrac.zivoti)
                   

                
def krajnjiEkra():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 30)

    if nadjeno_blago: 
        label1= font2.render("Congratulations, you win!",1,(88,88,88))
    else:
        label1= font2.render("You lose!",1,(88,88,88))
    
    label2=font2.render("Press [ENTER] to play a new game!",1,black)
    
    while not kraj:

        ekran.fill(white)
       
        ekran.blit(label1, (sirina_ekrana / 2 - label1.get_width() / 2, 250))
        ekran.blit(label2, (sirina_ekrana / 2 - label2.get_width() / 2, 550))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False
def krajnjiEkran():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 30)


    label1= font2.render("Congratulations, you win!",1,(88,88,88))
    
    label2=font2.render("Press [ENTER] to play a new game!",1,black)
    
    while not kraj:

        ekran.fill(white)
       
        ekran.blit(label1, (sirina_ekrana / 2 - label1.get_width() / 2, 250))
        ekran.blit(label2, (sirina_ekrana / 2 - label2.get_width() / 2, 550))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False

def krajnjiEkran1():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 30)


    label1= font2.render("You lose!",1,(88,88,88))
    label2=font2.render("Press [ENTER] to play a new game!",1,black)
    
    while not kraj:

        ekran.fill(white)
       
        ekran.blit(label1, (sirina_ekrana / 2 - label1.get_width() / 2, 250))
        ekran.blit(label2, (sirina_ekrana / 2 - label2.get_width() / 2, 550))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False
kraj=pocetniEkran()
while not kraj:
    igra()
    kraj = True
