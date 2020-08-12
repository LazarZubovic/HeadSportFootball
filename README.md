# HeadSportFootball
import random
import pygame as pg
import pygamebg

(sirina, visina) = (600, 400)
prozor = pygamebg.open_window(sirina, visina, "Head Sport Football")  #otvara se prozor

pg.key.set_repeat(10, 10) #podešavanje događaja tastature

(igrac_x, igrac_y) = (120, visina - 60)
(igrac_2_x, igrac_2_y) = (sirina - 120, visina - 60)
(lopta_x, lopta_y) = (sirina / 2, 50)
r = 10

def crtaj():
    prozor.fill(pg.Color("skyblue"))  #nebo
    pg.draw.rect(pg.Color("green"), (0, visina - 50, sirina, 50)  #trava
    pg.draw.circle(pg.Color("black"), (igrac_x, igrac_y), r)      #prvi igrač
    pg.draw.circle(pg.Color("white"), (igrac_2_x, igrac_2_y), r)       #drugi igrač
    pg.draw.circle(pg.Color("red"), (lopta_x, lopta_y), r / 2)      #lopta
    
def obradi_dogadjaj():
    global igrac_x, igrac_y, igrac_2_x, igrac_2_y
    if dogadjaj.type == pg.KEYDWON:   # pritisnut je taster na tastaturi
        if  dogadjaj.key == pg.LEFT:
            igrac_x -= 3                    # obrađujemo kretanje igrača levo - desno
        elif dogadjaj.key == pg.RIGHT:
            igrac_x += 3
        elif dogadjaj.key == pg.K_a:
            igrac_2_x -= 3
        elif dogadjaj.key == pg.K_d:
            igrac_2_x += 3
            return True











pygamebg.event_loop(crtaj, obradi_događaj)
