import pygame as pg
import random
import math

pg.init()

# --- PROZOR ---
sirina, visina = 800, 500
prozor = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Head Sport Football")

# --- IGRAČI ---
igrac_r = 25

igrac_x, igrac_y = 150, visina - 75
igrac_2_x, igrac_2_y = sirina - 150, visina - 75

igrac_vy = 0
igrac_2_vy = 0

# --- LOPTA ---
lopta_r = 15
lopta_x, lopta_y = sirina // 2, 100
vx = random.choice([-6, 6])
vy = 0

g = 0.5

# --- GOLOVI ---
gol_levo = 0
gol_desno = 0

# --- POMOĆNE FUNKCIJE ---
def sudar(x1, y1, r1, x2, y2, r2):
    dist = math.hypot(x1 - x2, y1 - y2)
    return dist < r1 + r2

def reset_lopte():
    global lopta_x, lopta_y, vx, vy
    lopta_x, lopta_y = sirina // 2, 100
    vx = random.choice([-6, 6])
    vy = 0

# --- GAME LOOP ---
sat = pg.time.Clock()
running = True

while running:
    # --- EVENTI ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # --- KRETANJE ---
    if keys[pg.K_LEFT]:
        igrac_x -= 5
    if keys[pg.K_RIGHT]:
        igrac_x += 5
    if keys[pg.K_UP] and igrac_y >= visina - 75:
        igrac_vy = -10

    if keys[pg.K_a]:
        igrac_2_x -= 5
    if keys[pg.K_d]:
        igrac_2_x += 5
    if keys[pg.K_w] and igrac_2_y >= visina - 75:
        igrac_2_vy = -10

    # --- GRAVITACIJA ---
    igrac_vy += g
    igrac_y += igrac_vy

    igrac_2_vy += g
    igrac_2_y += igrac_2_vy

    # --- POD ---
    if igrac_y > visina - 75:
        igrac_y = visina - 75
        igrac_vy = 0

    if igrac_2_y > visina - 75:
        igrac_2_y = visina - 75
        igrac_2_vy = 0

    # --- LOPTA ---
    vy += g
    lopta_x += vx
    lopta_y += vy

    # zidovi
    if lopta_x - lopta_r < 0 or lopta_x + lopta_r > sirina:
        vx *= -0.9

    if lopta_y - lopta_r < 0:
        vy *= -0.9

    if lopta_y + lopta_r > visina - 50:
        lopta_y = visina - 50 - lopta_r
        vy *= -0.8

    # --- SUDARI ---
    if sudar(igrac_x, igrac_y, igrac_r, lopta_x, lopta_y, lopta_r):
        vx = (lopta_x - igrac_x) * 0.2
        vy = -8

    if sudar(igrac_2_x, igrac_2_y, igrac_r, lopta_x, lopta_y, lopta_r):
        vx = (lopta_x - igrac_2_x) * 0.2
        vy = -8

    # --- GOLOVI ---
    if lopta_x < 20 and lopta_y > visina - 100:
        gol_desno += 1
        reset_lopte()

    if lopta_x > sirina - 20 and lopta_y > visina - 100:
        gol_levo += 1
        reset_lopte()

    # --- CRTANJE ---
    prozor.fill((135, 206, 235))  # nebo

    # trava
    pg.draw.rect(prozor, (0, 150, 0), (0, visina - 50, sirina, 50))

    # golovi
    pg.draw.rect(prozor, (255,255,255), (0, visina-100, 20, 50))
    pg.draw.rect(prozor, (255,255,255), (sirina-20, visina-100, 20, 50))

    # igrači
    pg.draw.circle(prozor, (0,0,0), (int(igrac_x), int(igrac_y)), igrac_r)
    pg.draw.circle(prozor, (255,255,255), (int(igrac_2_x), int(igrac_2_y)), igrac_r)

    # lopta
    pg.draw.circle(prozor, (255,0,0), (int(lopta_x), int(lopta_y)), lopta_r)

    # score
    font = pg.font.SysFont(None, 40)
    tekst = font.render(f"{gol_levo} : {gol_desno}", True, (0,0,0))
    prozor.blit(tekst, (sirina//2 - 30, 20))

    pg.display.update()
    sat.tick(60)

pg.quit()