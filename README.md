# HeadSportFootball
import random
import math
import pygame as pg
import pygamebg

(sirina, visina) = (600, 400)
prozor = pygamebg.open_window(sirina, visina, "Head Sport Football")  #otvara se prozor

pg.key.set_repeat(10, 10) #podešavanje događaja tastature

(igrac_x, igrac_y) = (120, visina - 60)
(igrac_2_x, igrac_2_y) = (sirina - 120, visina - 60)
(lopta_x, lopta_y) = (sirina / 2, 50)
r = 5
g = 9.81
vx = random.randint(0, 15)

def sudar_igrac_igrac():
    if math.sqrt((igrac_x - igrac_2_x)**2 + (igrac_y - igrac_2_y)**2):

def sudar_igrac_lopta():
    if math.sqrt((igrac_x - lopta_x)**2 + (igrac_y - lopta_y)**2):

def sudar_igrac_2_lopta():    
    if math.sqrt((igrac_2_x - lopta_x)**2 + (igrac_2_y - lopta_y)**2):
        
def novi_frejm():
    vy = vy + g / 20
    lopta_x += vx / 20
    lopta_y += vy / 20
    if lopta_x - r < 0 or lopta_x + r > sirina:
        vx = -vx * 0.75
    if lopta_y - r < 0 or lopta_y + r > visina:
        vy = -vy * 0.75

def crtaj():
    prozor.fill(pg.Color("skyblue"))  #nebo
    pg.draw.rect(pg.Color("green"), (0, visina - 50, sirina, 50)      #trava
    pg.draw.circle(pg.Color("black"), (igrac_x, igrac_y), r * 2)      #prvi igrač
    pg.draw.circle(pg.Color("white"), (igrac_2_x, igrac_2_y), r * 2)       #drugi igrač
    pg.draw.circle(pg.Color("red"), (lopta_x, lopta_y), r)      #lopta
    
def obradi_dogadjaj():
    global igrac_x
    global igrac_y
    global igrac_2_x
    global igrac_2_y
    if dogadjaj.type == pg.KEYDWON:   # pritisnut je taster na tastaturi
        if  dogadjaj.key == pg.LEFT:
            igrac_x -= 2                    # obrađujemo kretanje igrača levo - desno
        elif dogadjaj.key == pg.RIGHT:
            igrac_x += 2
        elif dogadjaj.key == pg.K_a:
            igrac_2_x -= 2
        elif dogadjaj.key == pg.K_d:
            igrac_2_x += 2
            return True




sat = pg.time.Clock()
kraj = False
while not kraj:
    crtaj()
    pg.display.update()
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
    sat.tick(50)
    novi_frejm()
pg.quit()
        
