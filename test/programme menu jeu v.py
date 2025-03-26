import pyxel
import time
 
pyxel.init(128, 128, title="Super jeu")
pyxel.load("4.pyxres")  # Assure-toi que ce fichier est bien chargé et accessible
perso_x = 20
perso_y = 20
sur_perso = False
pyxel.mouse(True)

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

    

def update():
    global perso_x, perso_y
    perso_x, perso_y = deplacer_perso(perso_x, perso_y)
    

def draw():
    pyxel.cls(0)
    
    # les personnages fix du menu
    pyxel.blt(20, 50, 1, 0, 0, 20, 30, 5)  # Personnage gauche
    pyxel.blt(55, 50, 1, 21, 0, 20, 30, 5)  # Personnage centre
    pyxel.blt(90, 50, 1, 41, 0, 20, 30, 5)  # Personnage droit
    pyxel.blt(perso_x, perso_y, 1, 0, 0, 8, 11, 5) # Dessiner le personnage principal
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 3, 3, 10)  # Curseur comme un petit rectangle jaune
    pyxel.text( 30, 20,"select your player",10)
    
    #si le curseur est sur l'un des personnages
    if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 80:
        pyxel.rectb(20, 50, 20, 30, 8)  # Contour rouge si souris sur le personnage à la position (20, 50)
        sur_perso = True
        
    elif 55 <= pyxel.mouse_x <= 75 and 50 <= pyxel.mouse_y <= 80:
        pyxel.rectb(55, 50, 20, 30, 8)# Contour rouge si souris sur le personnage à la position (55, 50)
        sur_perso = True
        
    elif 90 <= pyxel.mouse_x <= 110 and 50 <= pyxel.mouse_y <= 80:
        pyxel.rectb(90, 50, 20, 30, 8)# Contour rouge si souris sur le personnage à la position (90, 50)
        sur_perso = True
        

pyxel.run(update, draw)