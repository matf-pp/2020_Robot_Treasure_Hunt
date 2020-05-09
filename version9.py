import pygame
import random
import math
import numpy
import time


    
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
nadjeno_blago=False
izgubio=False
pocetna_slika=(15,15)
dis= (sirina_ekrana-45) // br_kolona
pomeren=False

ekran = pygame.display.set_mode((sirina_ekrana, visina_ekrana))
pygame.display.set_caption('ROBOT TREASURE HUNT')
clock = pygame.time.Clock()

class Prepreke():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = img_bomb
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

class Uragan():
    def __init__(self):
        self.x = 0
        self.y = 0

class Igrac():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.zivoti = 3
        self.image = img_robot
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


class Blago():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image = img_treasure
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        matrica[x][y]=1
    def nacrtajBlago(self): 
        ekran.blit(img_treasure,(pocetna_slika[0] + dis * self.x,pocetna_slika[1] + dis * self.y))


img_robot=pygame.image.load("robot.png")
img_tragovi = pygame.image.load("tragovi.png")
img_bomb=pygame.image.load("bomb.png")
img_treasure=pygame.image.load("treasure1.png")
img_live = pygame.image.load("heart.png")
img_live.set_colorkey(black)
img_hurricane = pygame.image.load("hurricane.png")

def pomeri_levo_igraca(igrac,blago,zivoti):
    b_x=blago.x
    b_y=blago.y

    x_staro=igrac.x
    y_staro=igrac.y
    
    if igrac.x > 1:
        igrac.x=igrac.x-1
    
    x=igrac.x
    y=igrac.y
    matrica[x][y] = 1
     
    if b_x == x and b_y==y:
        nadjeno_blago = True
        krajnjiEkran()
        igra()
    for u in lista_uragana:
        if u.x == x and u.y == y:
            pomeri_desno_igraca(igrac, blago, zivoti)
            ekran.blit(img_hurricane,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
            pygame.display.flip()
           
            
    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                prikaziBombe()
                krajnjiEkran1()
                igra()
            else:
                igrac.zivoti -= 1
                ekran.blit(img_bomb,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
                pygame.display.flip()
            
                 

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
        igra()
    for u in lista_uragana:
        if u.x == x and u.y == y:
            pomeri_levo_igraca(igrac, blago, zivoti)
            ekran.blit(img_hurricane,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
            pygame.display.flip()
   
    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                prikaziBombe()
                krajnjiEkran1()
                igra()
            else:
                igrac.zivoti -= 1
                ekran.blit(img_bomb,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
                pygame.display.flip()
                
        
    
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
        igra()
    for u in lista_uragana:
        if u.x == x and u.y == y:
           
            pomeri_dole_igraca(igrac, blago, zivoti)
            ekran.blit(img_hurricane,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
            pygame.display.flip()
           
    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                prikaziBombe()
                krajnjiEkran1()
                igra()
            else:
                igrac.zivoti -= 1
                ekran.blit(img_bomb,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
                pygame.display.flip()
               

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
        igra()
    for u in lista_uragana:
        if u.x == x and u.y == y:
            pomeri_gore_igraca(igrac, blago, zivoti)
            ekran.blit(img_hurricane,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
            pygame.display.flip()
           

    for i in lista_prepreka:
        if i.x == x and i.y == y:
            if igrac.zivoti == 1:
                izgubio = True
                prikaziBombe()
                krajnjiEkran1()
                igra()
            else:
                ekran.blit(img_bomb,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))
                pygame.display.flip()
                igrac.zivoti -= 1
        

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
    for i in range(18):
        prepr=Prepreke()
        random_koordinate_prepreke(prepr)

        lista_prepreka.append(prepr)

def NacrtajPrepreke(lista_prepreka):
    for p in lista_prepreka:
        ekran.blit(img_bomb,(pocetna_slika[0] + dis * p.x,pocetna_slika[1] + dis * p.y))
        #pygame.draw.circle(ekran, red, (nep.x,nep.y), nep.r)


def zauzeto_uragan(x,y):
    if matrica[x][y]==1:
        return True
    else:
        return False

def random_koordinate_uragane(uragani):
    uragani.x,uragani.y=random_koordinate(uragani.x,uragani.y)

    while zauzeto_uragan(uragani.x,uragani.y):
        uragani.x,uragani.y=random_koordinate(uragani.x,uragani.y)

    matrica[uragani.x][uragani.y]=1

def napravi_random_uragane(lista_uragana):
    for i in range(7):
        urag=Uragan()
        random_koordinate_uragane(urag)

        lista_uragana.append(urag)

def nije_prepreka(i,j,prepreke,uragani):
    for p in prepreke:
        if p.x==i and p.y==j:
            return 1

    for u in uragani:
        if u.x==i and u.y==j:
            return 2

    return 0

def NacrtajUragan(lista_uragana):
    for u in lista_uragana:
        ekran.blit(img_hurricane,(pocetna_slika[0] + dis * u.x,pocetna_slika[1] + dis * u.y))

def nacrtajTragove(x,y): 
        ekran.blit(img_tragovi,(pocetna_slika[0] + dis * x,pocetna_slika[1] + dis * y))

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
    

def igra():
    kraj=False 

    global matrica
    matrica=numpy.zeros((br_kolona+1,br_redova+1))

    b_x=0
    b_y=0

    b_x,b_y=random_koordinate(b_x,b_y)
    blago=Blago(b_x,b_y)

    global lista_prepreka, lista_uragana
    lista_prepreka=[]
    lista_uragana = []
    napravi_random_uragane(lista_uragana)

    napravi_random_prepreke(lista_prepreka)

    b_x,b_y=random_koordinate(b_x,b_y)
    while zauzeto(b_x,b_y):
        b_x,b_y=random_koordinate(b_x,b_y)

    igrac=Igrac(b_x,b_y)


    while not kraj:
        
        ekran.fill(white)
        nacrtajMrezu(sirina_ekrana,br_kolona,ekran)
        nacrtajIgraca(igrac)
        blago.nacrtajBlago()
        nacrtajZivote(ekran, sirina_ekrana-100, 5, igrac.zivoti,img_live)
        
        for i in range(1,10):
            for j in range(1,10):
                if matrica[i][j]==1 and (i!=blago.x or j!=blago.y) and (i!=igrac.x or j!=igrac.y):
                    if nije_prepreka(i,j,lista_prepreka,lista_uragana)==0:
                        nacrtajTragove(i,j)
                    elif nije_prepreka(i,j,lista_prepreka,lista_uragana)==1 and igrac.x==i and igrac.y==j:
                        ekran.blit(img_bomb,(pocetna_slika[0] + dis * i,pocetna_slika[1] + dis * j))
                    
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pomeri_levo_igraca(igrac,blago,igrac.zivoti)
                if event.key==pygame.K_RIGHT:
                    pomeri_desno_igraca(igrac,blago,igrac.zivoti)
                if event.key==pygame.K_UP:
                    pomeri_gore_igraca(igrac,blago,igrac.zivoti)
                if event.key==pygame.K_DOWN:
                    pomeri_dole_igraca(igrac,blago,igrac.zivoti)

                   

                

def prikaziBombe():

    i = 0
    

    while i < 3:
        NacrtajPrepreke(lista_prepreka)
        NacrtajUragan(lista_uragana)
        i+=1
        pygame.display.flip()
    time.sleep(1)


    

def pocetniEkran():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 20)
    label = font2.render("Try to take the treasure!", 1, black)
    label1= font2.render("Instructions: Use up, down, left and right arrows to move .",1,black)
    label2= font2.render("Also, there are many hidden obstacles.",1,black)
    label3= font2.render("Tip: Be careful, you have only 3 lives. GOOD LUCK!",1,black)
    label4=font2.render("Press [ENTER] to start!",1,black)
    label5 =font2.render("- When you step on this obstacle you will lose one life!",1,black)
    label6 =font2.render("- You can't step on the field where this obstacle is!",1,black)

    lista_labeli=[label1,label2,label3]

    while not kraj:

        ekran.fill(grey)
        i=0
        ekran.blit(label, (sirina_ekrana / 2 - label.get_width() / 2, 30))
        ekran.blit(img_bomb,(sirina_ekrana / 2 - label.get_width() / 2-120, 300) )
        ekran.blit(img_hurricane,(sirina_ekrana / 2 - label.get_width() / 2-120, 400) )
        ekran.blit(label5, (sirina_ekrana / 2 - label.get_width() / 2 -40, 315))
        ekran.blit(label6, (sirina_ekrana / 2 - label.get_width() / 2 -40, 410))
        for labela in lista_labeli:
            ekran.blit(labela, (sirina_ekrana / 2 - labela.get_width() / 2, 150+50*i))
            i+=1
        ekran.blit(label4, (sirina_ekrana / 2 - label4.get_width() / 2, 550))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False


def krajnjiEkran():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 30)


    label1= font2.render("Congratulations, you won!",1,(88,88,88))
   
    label2=font2.render("Press [ENTER] to play a new game!",1,black)
    
    while not kraj:

        ekran.fill(white)
       
        ekran.blit(label1, (sirina_ekrana / 2 - label1.get_width() / 2, 250))
        ekran.blit(label2, (sirina_ekrana / 2 - label2.get_width() / 2, 550))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False

def krajnjiEkran1():
    kraj=False
    # font slova na pocetnom ekranu i stil
    font2 = pygame.font.SysFont("arial", 30)

    
    label1= font2.render("GAME OVER!",1,(88,88,88))
    label2=font2.render("Press [ENTER] to play a new game!",1,black)
    
    while not kraj:

        ekran.fill(white)
       
        ekran.blit(label1, (sirina_ekrana / 2 - label1.get_width() / 2, 250))
        ekran.blit(label2, (sirina_ekrana / 2 - label2.get_width() / 2, 550))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return False
kraj=pocetniEkran()
while not kraj:
    igra()
    kraj = True
