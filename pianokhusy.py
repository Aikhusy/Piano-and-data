import pygame
import time
y0=900
x0=360
pygame.init()
gamedisplay=pygame.display.set_mode((y0,x0))
pygame.display.set_caption("PIANO CUKK!!!!!!!!!!!")
clock = pygame.time.Clock()
pygame.mixer.pre_init(999999999,-999999999,2,999999999)

notea = pygame.mixer.Sound("a4.mp3")
noteas = pygame.mixer.Sound("as4.mp3")
noteb = pygame.mixer.Sound("b4.mp3")
notec4 = pygame.mixer.Sound("c4.mp3")
notecs4 = pygame.mixer.Sound("cs4.mp3")
noted = pygame.mixer.Sound("d4.mp3")
noteds4 = pygame.mixer.Sound("ds4.mp3")
notee4 = pygame.mixer.Sound("e4.mp3")
notef4 = pygame.mixer.Sound("f4.mp3")
noteafs4 = pygame.mixer.Sound("fs4.mp3")
noteg4 = pygame.mixer.Sound("g4.mp3")
notecgs4 = pygame.mixer.Sound("gs4.mp3")
notec5 = pygame.mixer.Sound("c5.mp3")
notecs5 = pygame.mixer.Sound("cs5.mp3")
noted5 = pygame.mixer.Sound("d5.mp3")
noteds5 = pygame.mixer.Sound("ds5.mp3")
notee5 = pygame.mixer.Sound("e5.mp3")
piano = pygame.image.load('piano.png')
aa=(235, 141, 141)
ab=(235, 168, 141)
ac=(235, 197, 141)
ad=(235, 232, 141)
ae=(213, 235, 141)
af=(182, 235, 141)
ag=(141, 235, 232)
ah= (141, 196, 235)
ai= (219, 141, 235)
aj= (235, 141, 215)
ak= (235, 141, 190)
al= (235, 141, 152)
red=(225,225,225)
bru=(225,225,225)
line=(0,0,0)
lines=(59, 59, 59)
w=30
h=30
jalan = True
total_peng=0
total_peng1=0
target_peng=32
target_peng1=200
panjang_bal1=0
panjang_bal=0
cr=[]
var=[]
r=255
g=255
b=255

while total_peng != target_peng:
    total_peng= total_peng +1
    panjang_bal=panjang_bal+30
    var.append(panjang_bal)
while total_peng1 != target_peng1:
    total_peng1= total_peng1 +1
    panjang_bal1=panjang_bal1+15
    cr.append(panjang_bal1)
#print(var)


pygame.draw.rect(gamedisplay, bru,(0,0,900,360))
def garis(jar):
    pygame.draw.rect(gamedisplay, line,(jar,0,2,180))
    pygame.draw.rect(gamedisplay, line,(jar+60,0,2,180))
    pygame.draw.rect(gamedisplay, line,(jar,180,62,2))
    pygame.draw.rect(gamedisplay, line,(jar+30,180,2,180))
garis(cr[3])
garis(cr[9])

pygame.draw.rect(gamedisplay, line,(var[11]-90,0,2,360))
garis(cr[21])
garis(cr[27])
garis(cr[33])
pygame.draw.rect(gamedisplay, line,(var[23]-90,0,2,364))
garis(cr[45])
garis(cr[51])
#pygame.draw.rect(gamedisplay, aa,(var[6]+2,0,var[1]-2,180+2))
#pygame.draw.rect(gamedisplay, aa,(var[5]+2,364/2,90-2,360))

def butt(x,y,wa,wt,w,h,note,k1,k2):
    if x+w-k1>kursor[0]>x and y+h-4>kursor[1]>y or k2+k1>kursor[0]>k2 and h/2+h-4>kursor[1]>h/2:
        pygame.draw.rect(gamedisplay, wt,(x,y,w-k1,h-4))
        pygame.draw.rect(gamedisplay, wt,(k2,h/2,k1,h-4))
        pygame.display.update()
        if mouse[0]== 1:
            pygame.mixer.Sound.play(note)
        if mouse[2]== 1:
            pygame.mixer.Sound.play(note)
    else:
        pygame.draw.rect(gamedisplay, wa,(x,y,w-k1,h-4))
        pygame.draw.rect(gamedisplay, wa,(k2,h/2,k1,h-4))

def butt2(y,wa,wt,w,h,note,k1,k2,k3):
    if k3+2+k1-2>kursor[0]>k3+2 and y+h+2>kursor[1]>y or k2+2+w-2>kursor[0]>k2+2 and 364/2+2>kursor[1]>h:
        pygame.draw.rect(gamedisplay, wt,(k3+2,y,k1-2,h+2))
        pygame.draw.rect(gamedisplay, wt,(k2+2,364/2,w-2,h))
        pygame.display.update()
        if mouse[0]== 1:
            pygame.mixer.Sound.play(note)
        if mouse[2]== 1:
            pygame.mixer.Sound.play(note)
    else:
        pygame.draw.rect(gamedisplay, wa,(k3+2,y,k1-2,h+2))
        pygame.draw.rect(gamedisplay, wa,(k2+2,364/2,w-2,h))

def butt3(y,wa,wt,w,h,note,k1,k2,k3):
    if k3+k1>kursor[0]>k3 and y+180+2>kursor[1]>y or k2+w>kursor[0]>k2+2 and 364/2+h>kursor[1]>364/2:
        pygame.draw.rect(gamedisplay, wt,(k3+2,y,k1-2,h/2+2))
        pygame.draw.rect(gamedisplay, wt,(k2+2,364/2,w-2,h))
        pygame.display.update()
        if mouse[0]== 1:
            pygame.mixer.Sound.play(note)
        if mouse[2]== 1:
            pygame.mixer.Sound.play(note)
    else:
        pygame.draw.rect(gamedisplay, wa,(k3+2,y,k1-2,h/2+2))
        pygame.draw.rect(gamedisplay, wa,(k2+2,364/2,w-2,h))

def sharp(x,y,wa,wt,w,h,note):
    kursor= pygame.mouse.get_pos()
    if x+w>kursor[0]>x and y+h>kursor[1]>y:
        pygame.draw.rect(gamedisplay, wt,(x+2,y,w,h))
        pygame.display.update()
        if mouse[0]== 1:
            pygame.mixer.Sound.play(note)
        if mouse[2]== 1:
            pygame.mixer.Sound.play(note)
    else:
        pygame.draw.rect(gamedisplay, wa,(x+2,y,w,h))
pygame.draw.rect(gamedisplay, ab,(cr[3]+2,0,58,180))
while jalan:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan=False
    kursor= pygame.mouse.get_pos()
    #print = (kursor)
    mouse= pygame.mouse.get_pressed()

    butt(0,0,red,aa,90,364,notec4,30,cr[3])
    butt2(0,red,ac,90,360,noted,30,90,120)
    butt3(0,red,ad,90,360,notee4,var[1],var[5],var[6])

    
    butt(272,0,red,ae,90-2,364,notef4,30,330)
    butt2(0,red,af,90,360,noteg4,var[0],var[11],var[12])
    butt2(0,red,ag,90,360,notea,var[0],var[14],var[15])
    butt3(0,red,ah,90,360,noteb,var[1],var[17],var[18])

    butt(632,0,red,ai,90-2,364,notec5,30,690)
    butt2(0,red,aj,90,360,noted5,var[0],var[23],var[24])
    butt3(0,red,ak,90,360,notee5,var[1],var[26],var[27])
    
    # #bagian sharp
    sharp(cr[3],0,red,lines,58,180,notecs4)
    sharp(cr[9],0,red,lines,58,180,noteds4)
    

    sharp(cr[21],0,red,lines,58,180,noteafs4)
    sharp(cr[27],0,red,lines,58,180,notecgs4)
    sharp(cr[33],0,red,lines,58,180,noteas)

    sharp(cr[45],0,red,lines,58,180,notecs5)
    sharp(cr[51],0,red,lines,58,180,noteds5)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()