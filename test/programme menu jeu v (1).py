import pyxel
import random

pyxel.init(128, 128, title="Super jeu")
pyxel.load("4 (1).pyxres")  
perso_x = 20
perso_y = 20
sur_perso = 0
pyxel.mouse(True)
tirs_liste = []
pyxel.play(0, 0, loop=True)

def deplacer_perso(x, y):
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x = x - 3
    if pyxel.btn(pyxel.KEY_RIGHT) and x <= 120:
        x = x + 3
    if pyxel.btn(pyxel.KEY_DOWN) and y <= 120:
        y = y + 3
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y = y - 3
    return x, y

def tirs_creation(x, y, tirs_liste):
    # Création d'un tir avec la barre d'espace
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x + 13, y + 12])  # Ajuste la position de départ
    return tirs_liste

def tirs_deplacement(tirs_liste):
    # Déplacement des tirs vers la droite et suppression s'ils sortent du cadre
    for tir in tirs_liste:
        tir[0] = tir[0] + 2  # Déplace le tir vers la droite
        if tir[0] > 128:  # Si le tir sort de l'écran
            tirs_liste.remove(tir)
    return tirs_liste

def update():
    global perso_x, perso_y, tirs_liste
    
    perso_x, perso_y = deplacer_perso(perso_x, perso_y)
    tirs_liste = tirs_creation(perso_x, perso_y, tirs_liste)
    tirs_liste = tirs_deplacement(tirs_liste)

    global sur_perso
    if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 80:#c'est les limite qui permet de voir si la souris survol un des 3 perso
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):  
            sur_perso = 1  
    elif 55 <= pyxel.mouse_x <= 75 and 50 <= pyxel.mouse_y <= 80:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):  
            sur_perso = 2  
    elif 90 <= pyxel.mouse_x <= 110 and 50 <= pyxel.mouse_y <= 80:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): 
            sur_perso = 3
            
    global couleur_aleatoire
            
    if pyxel.frame_count % 7 == 0:
        couleur_aleatoire = random.randint(1, 15)

def draw():
    
    couleur = random.randint(1, 15)
    global perso_x, perso_y, sur_perso
    pyxel.cls(0)

    pyxel.blt(20, 50, 1, 0, 0, 20, 30, 2)
    pyxel.blt(55, 50, 1, 21, 0, 20, 30, 11)#les perso sont blt pour faire le menu
    pyxel.blt(90, 50, 1, 41, 0, 20, 30, 6)
    pyxel.text(30, 20, "select your player",couleur_aleatoire)

    if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 80:#les trois truc donne le contour quand la souris survol un personnage
        pyxel.rectb(20, 50, 20, 30, 8)
    elif 55 <= pyxel.mouse_x <= 75 and 50 <= pyxel.mouse_y <= 80:
        pyxel.rectb(55, 50, 20, 30, 8)
    elif 90 <= pyxel.mouse_x <= 110 and 50 <= pyxel.mouse_y <= 80:
        pyxel.rectb(90, 50, 20, 30, 8)

    if sur_perso == 1:
        pyxel.rect(0, 0, 128, 128, 0)
        pyxel.mouse(False)
        pyxel.blt(perso_x, perso_y, 1, 0, 0, 16, 20, 1)#la sa blt le bon perso pour commencer a jouer
        for tir in tirs_liste:#je blt le chevalier
            pyxel.blt(tir[0], tir[1], 1, 77, 0, 15, 12, 1)#je blt le tir dans le fichier 4.pyxres
            
            
    elif sur_perso == 2:
        pyxel.rect(0, 0, 128, 128, 0)
        pyxel.mouse(False)
        pyxel.blt(perso_x, perso_y, 1, 21, 0, 20, 30, 11)
        for tir in tirs_liste:
            pyxel.rect(tir[0], tir[1], 3,3,couleur)#magicien avec le tir boule de magie 
    elif sur_perso == 3:
        pyxel.rect(0, 0, 128, 128, 0)
        pyxel.mouse(False)
        pyxel.blt(perso_x, perso_y, 1, 41, 0, 20, 30, 6)#arché avec blt des fleche
        for tir in tirs_liste:
            pyxel.blt(tir[0], tir[1], 1, 76, 12, 15, 12, 1)
            

pyxel.run(update, draw)