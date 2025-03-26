import pyxel
import time
 
pyxel.init(128,128,title="Super jeu")
pyxel.load("4.pyxres")
perso_x = 20
perso_y = 85
perso1_x = 15
perso1_y = 15
#couleur_rectangle = 8
message = ""
en_mouvement = False
restart_game = False
message2=""
compteur = 0
w = 30
h = 30
c = 0

def deplacer_perso(x,y):
    en_mouvement = False
    
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x = x - 3
        en_mouvement = True
        
    if pyxel.btn(pyxel.KEY_RIGHT) and x <= 118:
        x = x + 3
        en_mouvement = True
        
    #if pyxel.btn(pyxel.KEY_UP) and y >86 :
        #y = y - 3
        
    if pyxel.btn(pyxel.KEY_DOWN) and y < 31:
        y = y + 3
        en_mouvement = True
    
    return x,y,en_mouvement
       

def update():
    
    global perso_x , perso_y,en_mouvement, couleur_rectangle,restart_game,message,w,h,c
    
    if pyxel.frame_count % 90 == 0:
        if c == 0:  # Première étape
            w, h, c = 32, 31, 32 #rouge
        elif c == 32:  # Deuxième étape
            w, h, c = 32, 31, 0# vert
        else:
            w, h, c = 32, 31, 0  # Réinitialisation
    
        #couleur_rectangle = 11 if couleur_rectangle == 8 else 8  # Rouge ou Vert
        
    # Mise à jour des positions du personnage et voir si il est en mouvement
    perso_x, perso_y,en_mouvement = deplacer_perso(perso_x, perso_y)
    
    if en_mouvement and h ==31 and w== 32 and c== 32:#rouge
        restart_game = True
        message = "GAME OVER!"# Afficher le message
        perso_x, perso_y = 20, 85
        restart_game = False
        
        #compteur= 0 if couleur_rectangle ==11 else compteur
        #message = ""
        #if couleur_rectangle == 8:  # Si rouge
            #if pyxel.frame_count - dernier_changement > 30:  # Affiche un nombre toutes les 30 frames
                #compteur = compteur + 1
                #dernier_changement = pyxel.frame_count  # Met à jour le dernier changement
                #if compteur == 4:  # Si compteur atteint 4, on affiche "Soleil"
                    # affichage_message = "Soleil!"
                    # compteur = 0  # Redémarre le compteur
                #else:
                     #affichage_message = str(compteur)
    
    #global message2
    #if pyxel.btn(pyxel.KEY_SPACE):#test space enleve game over
            #message2 = message
            #message2=""

def draw():
    pyxel.cls(0)
    pyxel.blt(perso_x, perso_y, 0, 0, 0, 8, 8, 5)
    pyxel.blt(perso1_x, perso1_y,0,c,0,h,w,0) # Dessine le personnage
    #pyxel.rect(55, 55, 18, 18, couleur_rectangle)  # Dessine le carré
    pyxel.text(40, 60, message, 10)  # Afficher le message "GAME OVER"

pyxel.run(update, draw)