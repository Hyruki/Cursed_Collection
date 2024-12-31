import pyxel

pyxel.init(128,128,title="Super jeu")
pyxel.load("1.pyxres")
perso_x = 20
perso_y = 85
message= "press enter to start" #pyxel.text(30,30,'press enter to start',10)
message2=""
message3=""
personnage_vy = 0  # Vitesse verticale
gravite = 0.5  # Force de gravité
saut_force = -10  # Force du saut (vers le haut)
sol_y = 100
personnage_x = 50  # Position horizontale
personnage_y = 100

def deplacer_perso(x,y):
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x = x - 3
        
    if pyxel.btn(pyxel.KEY_RIGHT) and x <= 118:
        x = x + 3
        
    #if pyxel.btn(pyxel.KEY_UP) and y >86 :
        #y = y - 3
        
    if pyxel.btn(pyxel.KEY_DOWN) and y < 31:
        y = y + 3
    return x,y

def update():
    global perso_x , perso_y
    perso_x, perso_y = deplacer_perso(perso_x , perso_y)
    
    global message
    if pyxel.btnp(pyxel.KEY_RETURN):  # Si la touche Entrée est pressée
        message = ""  # Supprime le texte
        
    global message2
    if pyxel.btnp(pyxel.KEY_CTRL):  # Si la touche Entrée est pressée
        message2 = "press enter to resume"
    if pyxel.btnp(pyxel.KEY_RETURN):  # Si la touche Entrée est pressée
        message2 =""  # Supprime le text
       
    global message3
    if pyxel.btnp(pyxel.KEY_CTRL):  # Si la touche Entrée est pressée
        message3 = "PAUSE"
    if pyxel.btnp(pyxel.KEY_RETURN):  # Si la touche Entrée est pressée
        message3=""
        
    global personnage_y, personnage_vy

    # Appliquer la gravité
    personnage_vy += gravite

    # Mettre à jour la position verticale
    personnage_y += personnage_vy

    # Détection de collision avec le sol
    if personnage_y > sol_y:
        personnage_y = sol_y  # Empêche de passer à travers le sol
        personnage_vy = 0  # Annule la vitesse verticale au contact

    # Déclencher le saut si on appuie sur ESPACE et qu'on est au sol
    if pyxel.btnp(pyxel.KEY_SPACE) and personnage_y == sol_y:
        personnage_vy = saut_force  # Appliquer une force vers le haut

        

        
def draw():
    pyxel.rect(0,0,128,128,0)# le fond orange
    pyxel.blt(perso_x, perso_y,0,0,0,8,11,5)
    pyxel.text(20, 50, message, 10)
    pyxel.text(20, 50, message2, 10)
    pyxel.text(55, 35, message3, 10)
    pyxel.blt(0, 97, 0, 0, 0, 31, 31)
    pyxel.blt(31, 97, 0, 0, 0, 31, 31)
    pyxel.blt(62, 97, 0, 0, 0, 31, 31)
    pyxel.blt(93, 97, 0, 0, 0, 31, 31)
    pyxel.blt(124, 97, 0, 0, 0, 31, 31)

#programmer princippal
pyxel.run(update, draw)    