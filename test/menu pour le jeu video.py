import pyxel
import random

pyxel.init(128, 128, title="Super jeu")
pyxel.load("4.pyxres")  

# États du jeu
ETAT_MENU = 0
ETAT_SELECTION = 1
ETAT_JEU = 2
ETAT_PAUSE = 3
etat_actuel = ETAT_MENU

# Position initiale du personnage
perso_x = 20
perso_y = 20
sur_perso = 0
pyxel.mouse(True)
tirs_liste = []
pyxel.play(0, 0, loop=True)
couleur_aleatoire = 7

def deplacer_perso(x, y):
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x -= 3
    if pyxel.btn(pyxel.KEY_RIGHT) and x <= 120:
        x += 3
    if pyxel.btn(pyxel.KEY_DOWN) and y <= 120:
        y += 3
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y -= 3
    return x, y

def tirs_creation(x, y, tirs_liste):
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x + 13, y + 12])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[0] += 2
        if tir[0] > 128:
            tirs_liste.remove(tir)
    return tirs_liste

def update():
    global perso_x, perso_y, tirs_liste, sur_perso, etat_actuel, couleur_aleatoire
    
    if etat_actuel == ETAT_MENU:
        if 40 <= pyxel.mouse_x <= 90 and 60 <= pyxel.mouse_y <= 80 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            etat_actuel = ETAT_SELECTION
    
    elif etat_actuel == ETAT_SELECTION:
        if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 80 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            sur_perso = 1  
            etat_actuel = ETAT_JEU
        elif 55 <= pyxel.mouse_x <= 75 and 50 <= pyxel.mouse_y <= 80 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            sur_perso = 2  
            etat_actuel = ETAT_JEU
        elif 90 <= pyxel.mouse_x <= 110 and 50 <= pyxel.mouse_y <= 80 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            sur_perso = 3  
            etat_actuel = ETAT_JEU
    
    elif etat_actuel == ETAT_JEU:
        if pyxel.btnp(pyxel.KEY_A):  # Pause
            etat_actuel = ETAT_PAUSE
        perso_x, perso_y = deplacer_perso(perso_x, perso_y)
        tirs_liste = tirs_creation(perso_x, perso_y, tirs_liste)
        tirs_liste = tirs_deplacement(tirs_liste)
        
    elif etat_actuel == ETAT_PAUSE:
        if 20 <= pyxel.mouse_x <= 110 and 30 <= pyxel.mouse_y <= 45 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            etat_actuel = ETAT_JEU  # Resume
        elif 20 <= pyxel.mouse_x <= 110 and 55 <= pyxel.mouse_y <= 70 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            perso_x, perso_y = 20, 20  # Restart
            tirs_liste = []
            etat_actuel = ETAT_JEU
        elif 20 <= pyxel.mouse_x <= 110 and 80 <= pyxel.mouse_y <= 95 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            etat_actuel = ETAT_MENU  # Home

    if pyxel.frame_count % 20 == 0:
        couleur_aleatoire = random.randint(1, 15)

def draw():
    pyxel.cls(0)
    
    if etat_actuel == ETAT_MENU:
        pyxel.text(30, 30, "The Darkness Lord", 7)
        pyxel.rect(40, 60, 50, 20, 5)
        pyxel.text(57, 67, "Play", 7)
        
        if 40 <= pyxel.mouse_x <= 90 and 60 <= pyxel.mouse_y <= 80:
            pyxel.rectb(40, 60, 50, 20, 8)

    elif etat_actuel == ETAT_SELECTION:
        pyxel.text(30, 20, "Select Your Player", couleur_aleatoire)
        pyxel.blt(20, 50, 1, 0, 0, 20, 30, 2)
        pyxel.blt(55, 50, 1, 21, 0, 20, 30, 11)
        pyxel.blt(90, 50, 1, 41, 0, 20, 30, 6)
        
        if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 80:
            pyxel.rectb(20, 50, 20, 30, 8)
        elif 55 <= pyxel.mouse_x <= 75 and 50 <= pyxel.mouse_y <= 80:
            pyxel.rectb(55, 50, 20, 30, 8)
        elif 90 <= pyxel.mouse_x <= 110 and 50 <= pyxel.mouse_y <= 80:
            pyxel.rectb(90, 50, 20, 30, 8)

    elif etat_actuel == ETAT_JEU:
        pyxel.blt(perso_x, perso_y, 1, (sur_perso - 1) * 21, 0, 20, 30, 6)
        for tir in tirs_liste:
            pyxel.blt(tir[0], tir[1], 1, 76, 12, 15, 12, 1)

    elif etat_actuel == ETAT_PAUSE:
        pyxel.rect(20, 30, 90, 15, 3)
        pyxel.text(52, 35, "Resume", 7)
        pyxel.rect(20, 55, 90, 15,5)
        pyxel.text(50, 60, "Restart", 7)
        pyxel.rect(20, 80, 90, 15, 10)
        pyxel.text(56, 85, "Home", 7)

        if 20 <= pyxel.mouse_x <= 110 and 30 <= pyxel.mouse_y <= 45:
            pyxel.rectb(20, 30, 90, 15, 8)
        elif 20 <= pyxel.mouse_x <= 110 and 55 <= pyxel.mouse_y <= 70:
            pyxel.rectb(20, 55, 90, 15, 8)
        elif 20 <= pyxel.mouse_x <= 110 and 80 <= pyxel.mouse_y <= 95:
            pyxel.rectb(20, 80, 90, 15, 8)


pyxel.run(update, draw)
