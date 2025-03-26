#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
import game_management
import joueur
import game_management
from utils import *
import time
import loot
import hud
from random import randint

enemies_coord = [[-30, 124+32, 1, 17, 137, 12, 14, 7, 3*game_management.mode_de_jeu, 0, [],0,0]]

TEMP=0
limite_ennemis=2

boost_degat_ennemi=1
boost_degat_joueur=1

mariline_rouge=[32,160]
mariline_mid=[0,192]
TEMP_boss=0
boss_choix=0
bossatk1=[120,154-(82-32),1,128,56,16,16,7]
bossatk2=[120,154-(82-32),1,144,56,16,16,7]
boss_info=[[0,112,154-(82-32),1,96,56,32,72,7,bossatk1,bossatk2,0,0,15],[0,112,102+32,0,0,160,32,32,13,mariline_rouge,mariline_mid,0,0,17],[0,235,30,1,120,0,16,48,11,120,104,10,0,1000]]
boss_ennemi_coord=[]

nombre_ennemi=0
perso1_x = 821

perso1_y = 10

message = ""

en_mouvement = False

restart_game = False

compteur = 0

hidden=0
stun=0

w = 32

h = 32

c = 0

vitesse = 0.6
vitesse_chasse = 1.1

enemie_spawn_cooldown = 0

# TESSST
activation = False
    
def mariline_monro():
    global perso_x , perso_y,en_mouvement, couleur_rectangle,restart_game,message,w,h,c

    pyxel.blt(perso1_x, perso1_y,0,c,160,h,w,0) # Dessine le personnage

    if pyxel.frame_count % 90 == 0 and activation:
        if c == 0:  # Première étape
            w, h, c = 32, 31, 32 #rouge
        elif c == 32:  # Deuxième étape
            w, h, c = 32, 31, 0# vert
        else:
            w, h, c = 32, 31, 0  # Réinitialisation
    
        #couleur_rectangle = 11 if couleur_rectangle == 8 else 8  # Rouge ou Vert
        
    
    if en_mouvement and c== 32 and activation:#rouge
        game_management.game_over()

def affichages_enemies():
    for elem in enemies_coord:
            pyxel.blt(elem[0],elem[1],elem[2],elem[3],elem[4],elem[5],elem[6],elem[7])

# Fonction de la création de l'intelligence des enenemis
def ennemis_cells():
    for elem in enemies_coord:
        if not elem[11]:
            if not elem[12]:
                if elem[0]<=23:
                    elem[0]+=vitesse-0.2
                if elem[0]>=256-23:
                    elem[0]-=vitesse-0.2
                if elem[0]>23 and elem[0]<256-23:
                    elem[12]=1
            
            
                 # Système de chasse
            if joueur.y >= elem[1] - 34 and not hidden:
                if joueur.x > elem[0]:
                    elem[0] += vitesse_chasse
                else:
                    elem[0] -= vitesse_chasse
            else :
                if elem[9] == 0:
                    elem[0] += vitesse
                    if elem[0]>256-25:
                        elem[9] = 1
                else:
                    elem[0] -= vitesse
                    if elem[0]<25:
                        elem[9] = 0

# Fonction de l'affichage de Mona Lisa
# [coord X , coord Y, calque, coord X calque, coord Y calque, couleur transparente, vie, direction(0:droite / 1:gauche) ,[projectilles]]
def mona_lisa(x, y):
    return [x, y, 1, 17, 137, 12, 14, 7, 3*game_management.mode_de_jeu, 0, [],0,0]

def picasso(x, y):
    return [x, y, 1, 17, 155, 14, 12, 1, 3*game_management.mode_de_jeu, 0, [],0,0]

# La Jeune fille à la perle
def vinci_JFALP(x, y):
    return [x, y, 1, 33, 137, 12, 14, 1, 3*game_management.mode_de_jeu, 0, [],0,0]

# La Grande Vague
def lagrandevague(x, y):
    return [x, y+5, 1, 33, 155, 14, 12, 1, 3*game_management.mode_de_jeu, 0, [],0,0]

# La Nuit Etoilée
def lanuitetoile(x, y):
    return [x, y+5, 1, 49, 139, 14, 12, 1, 3*game_management.mode_de_jeu, 0, [],0,0]

# Les Tournesols
def lestournesols(x, y):
    return [x, y, 1, 49, 153, 12, 14, 1, 3*game_management.mode_de_jeu, 0, [],0,0]


def alea_enemis(x, y):
    alea = randint(0,5)
    
    if alea == 0:
        return mona_lisa(x,y)
    elif alea == 1:
        return picasso(x,y + 5)
    elif alea == 2:
        return vinci_JFALP(x,y)
    elif alea == 3:
        return lagrandevague(x,y)
    elif alea == 4:
        return lanuitetoile(x,y)
    elif alea == 5:
        return lestournesols(x,y)




def place_alea_coord():
    rand = randint(0,1)

    if rand == 0: return 267, 124+32
    if rand == 1: return -30, 124+32
def nombre_ennemi_par_round():
    global limite_ennemis,TEMP,boss_choix,TEMP_boss,boss_info
    
    while game_management.round_game%3==0 and TEMP==0 :
        limite_ennemis+=1
        TEMP+=1
    if game_management.round_game%3==1 :
        TEMP=0
    if game_management.round_game%5==0 and TEMP_boss==0:
        boss_choix=randint(0,2)
        TEMP_boss+=1
        boss_info[boss_choix][0]=1
        
    if not game_management.round_game%5==0:
        TEMP_boss=0
    
def place_enemis(n_enemies:int):
    global enemies_coord,nombre_ennemi,limite_ennemis,boss_choix,boss_info
    
    if pyxel.frame_count % 40 == 0 and nombre_ennemi <= limite_ennemis and game_management.place_enemie:
        coord = place_alea_coord()
        enemies_coord.append(alea_enemis(coord[0],coord[1]))
        nombre_ennemi+=1
    
    
    if limite_ennemis-nombre_ennemi==0 :
        game_management.place_enemie = False
        nombre_ennemi=0
    

  
def boss():
    global boss_choix,boss_info
    if boss_info[boss_choix][0]:
        pyxel.blt(boss_info[boss_choix][1],boss_info[boss_choix][2],boss_info[boss_choix][3],boss_info[boss_choix][4],boss_info[boss_choix][5],boss_info[boss_choix][6],boss_info[boss_choix][7],boss_info[boss_choix][8],)    
    
def atk_boss():
    global boss_info,boss_choix,boost_degat_ennemi,boost_degat_joueur,boss_ennemi_coord,stun,hidden
    if boss_info[boss_choix][0]:
        if boss_ennemi_coord==[] and boss_choix!=2:
            boss_ennemi_coord=[boss_info[boss_choix][1],boss_info[boss_choix][2],boss_info[boss_choix][6],boss_info[boss_choix][7],boss_info[boss_choix][13]*game_management.round_game*game_management.mode_de_jeu]
        if boss_choix==0:
            if boss_info[boss_choix][12]>=300:
                boss_info[boss_choix][11]=randint(1,2)
                if boss_info[boss_choix][11]==2:
                    boost_degat_joueur-=0.05
                if boss_info[boss_choix][11]==1:
                    boost_degat_ennemi+=0.1
                boss_info[boss_choix][12]=0
            if boss_info[boss_choix][12]<300:
                boss_info[boss_choix][12]+=1  
            if boss_info[boss_choix][11]==2:
                pyxel.blt(boss_info[boss_choix][10][0],boss_info[boss_choix][10][1],boss_info[boss_choix][10][2],boss_info[boss_choix][10][3],boss_info[boss_choix][10][4],boss_info[boss_choix][10][5],boss_info[boss_choix][10][6],boss_info[boss_choix][10][7])
            if boss_info[boss_choix][11]==1:
                pyxel.blt(boss_info[boss_choix][9][0],boss_info[boss_choix][9][1],boss_info[boss_choix][9][2],boss_info[boss_choix][9][3],boss_info[boss_choix][9][4],boss_info[boss_choix][9][5],boss_info[boss_choix][9][6],boss_info[boss_choix][9][7])

        # Marilline Monro    
        if boss_choix==1:
            if  boss_info[boss_choix][12] >=180:
                pyxel.blt(boss_info[boss_choix][1],boss_info[boss_choix][2],boss_info[boss_choix][3],boss_info[boss_choix][9][0],boss_info[boss_choix][9][1],boss_info[boss_choix][6],boss_info[boss_choix][7],boss_info[boss_choix][8])
                if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_SPACE):
                    hud.degats_subi -= 1*game_management.round_game*boost_degat_ennemi*((150-hud.stats[0])/150)
                if pyxel.btnr(pyxel.KEY_E) or pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                    hud.degats_subi -= 0.08*game_management.round_game*boost_degat_ennemi*((150-hud.stats[0])/150)
            if boss_info[boss_choix][12]<=179 and boss_info[boss_choix][12]>=121:
                pyxel.blt(boss_info[boss_choix][1],boss_info[boss_choix][2],boss_info[boss_choix][3],boss_info[boss_choix][10][0],boss_info[boss_choix][10][1],boss_info[boss_choix][6],boss_info[boss_choix][7],boss_info[boss_choix][8])
            if boss_info[boss_choix][12] >=301:
                boss_info[boss_choix][12]=0
            boss_info[boss_choix][12]+=1

        if boss_choix==2:
            if boss_info[boss_choix][1]<=joueur.x and not stun and not hidden:
                boss_info[boss_choix][4]=boss_info[boss_choix][10]
                boss_info[boss_choix][1]+=0.5
            if boss_info[boss_choix][1]>joueur.x and not stun and not hidden:
                boss_info[boss_choix][4]=boss_info[boss_choix][9]
                boss_info[boss_choix][1]-=0.5
            if boss_info[boss_choix][2]<joueur.y-joueur.h and not stun and not hidden:
                boss_info[boss_choix][2]+=0.32
            if boss_info[boss_choix][2]>joueur.y-joueur.h and not stun and not hidden:
                boss_info[boss_choix][2]-=0.32
            boss_info[boss_choix][12]+=1
            if boss_info[boss_choix][12]>=480+boss_info[boss_choix][11]*game_management.round_game*2:
                boss_info[boss_choix][0]=0
            if collision(boss_info[boss_choix][1],boss_info[boss_choix][2],boss_info[boss_choix][7],boss_info[boss_choix][6], joueur.x, joueur.y, joueur.h, joueur.l):
                        boss_info[boss_choix][1]=235
                        boss_info[boss_choix][2]=30
                        hud.degats_subi -= 2.5*game_management.round_game*boost_degat_ennemi*((150-hud.stats[0])/150)
            if hidden:
                boss_info[boss_choix][1]=235
                boss_info[boss_choix][2]=30

            
    if not boss_info[boss_choix][0] and joueur.conserve==0 :
        boost_degat_ennemi=1
        boost_degat_joueur=1
        boss_info[boss_choix][12]=0
        if boss_choix==2:
            boss_info[boss_choix][1]=235
            boss_info[boss_choix][2]=30

    


# Fonction qui contrôle le loot tombé au sol quand nous tueons un ennemie
# Si random est égal à 0 : C'est de l'agent
# Si random est égal à 1 : C'est de la vie
def drop_loot(x, y):
    random_loot = randint(0,1)

    if random_loot == 0:
        loot.coins(x, y)
    else:
        loot.coeur(x, y)


# Liste de tous les enemies à afficher à l'écran

