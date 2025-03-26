#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
from utils import *
import monstre
import game_management
import monstre
import loot
import hud
from random import randint
import random

info_orbes=[[39,111,0],[103,111,1],[71,111,2]]
orbes_choix=False
coords_orbes=[]
boost_orbs=1

stats_joueur=[0,100,0,100,0,0,100,0,100]
activation_stun=0
debugmode=0#pour empêcher le joueur de fly avec flèche du haut

# Variable de Base
x, y = random.choice([33,209]), 68
l, h = 13, 20
u, v = 1, 228

valeur_random=0
valeur_1=0
valeur_2=0
valeur_3=0
# Direction : 0 : Droite | 1 : Gauche
direction = 0

color = 15

minuteur=0
modèle_flèche=[66,244,48]
conserve=0
boss_stun=0
#vie_perso = 10

boost_ulti=1

atk=[]

info_flamme=0
timeur=0
gravity = 1
velocity = 0
jumping = False

on_floor = False

noclip = False

TYPE = 0

# Coordoné tiles des murs
#WALL = [(0,2),(1,2),(0,3),(1,3)]

WALL =[(8,0),(9,0),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(9,3),(10,3),(1,2),(2,2),(0,21)]# [(11,2),(12,2),(13,2),(14,18),(15,18),(16,18)]

NEXT_ZONE = [(0,1)]

# Liste des projectiles jetés
tirs_liste = []

tirs_cooldown = 0

# Déplacement du personnage
def double_hit():
    x=random.choices((0,1),(100,hud.stats[4]))
    plus=0
    if hud.stats[4]>100 and hud.stats[4]<200:
        plus=1
    if hud.stats[4]>200:
        plus=2
    
    if x:
        double_hit_variable=2+plus
    if not x :
        double_hit_variable=1+plus
    return double_hit_variable
def move_player():
    global x, y, jumping, velocity, on_floor, direction,h

    monstre.en_mouvement = False


    # Déplacement du personnage vers la DROITE
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)  :
        if x<256-25 and y>124 or (not verif_col_liste(x+14, y, WALL) and not verif_col_liste(x+14, y+19, WALL) or noclip) :
            x += 1*(hud.stats[6]/100)
            direction = 0
            monstre.en_mouvement = True

    # Déplacement du personnage vers la GAUCHE
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) :
        if x>25 and y>124 or (not verif_col_liste(x-1, y, WALL) and not verif_col_liste(x-1, y+19, WALL) or noclip):
            x -= 1*(hud.stats[6]/100)
            direction = 1
            monstre.en_mouvement = True


    if debugmode==True and( pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)) and (not verif_col_liste(x, y-1, WALL) and not verif_col_liste(x+13, y-1, WALL) or noclip):
        y -= 1
        monstre.en_mouvement = True

    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) and y<124+32:
        y += 1
        monstre.en_mouvement = True
        
    # Détection Saut
    if pyxel.btn(pyxel.KEY_SPACE) and jumping == False and on_floor and not noclip:
        jumping = True
    else: 
        jumping = False

    # Détection collision du haut
    #if verif_col_liste(x, y-1, WALL) or verif_col_liste(x+13, y-1, WALL) or verif_col_liste(x+l//2, y-1, WALL) and not noclip:
     #   velocity = 0

    # Système de gravité
    if (y>133 and y<124+32) or (y+h>=121 and y+h<=151) or not verif_col_liste(x, y+20, WALL) and not verif_col_liste(x+13, y+20, WALL) and  not noclip and not( ((collision(x,y,h,l,27,60,1,26) or collision(x,y,h,l,203,60,1,26))and y+h<=61) or ((collision(x,y,h,l,27,88,1,26) or collision(x,y,h,l,203,88,1,26))and y+h<=89) or ((collision(x,y,h,l,99,32+4,1,56)and y+h<=33+4) or (collision(x,y,h,l,99,64,1,56)and y+h<=65) or (collision(x,y,h,l,100,84,1,56)and y+h<=85) ) ):
        if velocity < 1:
            velocity += gravity
        on_floor = False
    else:
        on_floor = True
        velocity = 0
        jump_sys()
    # Ajout vélocité avec les coordonnées Y
    if not noclip:
        y += velocity

    # DEBUG MODE
    if noclip:
        pass

def DEBUG_MODE():
    global x, y
    pass
#    if pyxel.btn(pyxel.KEY_K):
 #       x = 116
  #      y = 8
   # if pyxel.btn(pyxel.KEY_B):
   #     game_management.noclip()
    #    pyxel.camera(x, y)
    #
   # if pyxel.btn(pyxel.KEY_N):
    #    game_management.disable_noclip()
   # if pyxel.btn(pyxel.KEY_K):
    #    game_management.test_tp(821, 28, pyxel.camera)
     #   monstre.activation = True


#def test_degat():
 #   pyxel.rect(150, 50, 50, 50, 8)

   # if collision(150,50,50,50,x,y,h,l):
    #   pass# hud.degats_subi -=10 #1+2*game_management.round_game
    

#def get_vie():
 #   return hud.degats_subi
# Système de Saut
def jump_sys():
    global jumping, velocity, on_floor
    # Ajout vélocité afin de sauté de façon fluide
    if jumping:
        velocity = -9

    """if pyxel.btn(pyxel.KEY_UP):
        player_y -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y += 1"""


def generation_type():
    global l, h, u, v, color, TYPE

    if TYPE == 0:
        pass
    elif TYPE == 1:
        u = 16
        v = 227
        l = 15
        h = 20
        color = 10
    elif TYPE == 2:
        u = 32
        v = 227
        l = 16
        h = 20
        color = 6

# Création des projectiles
def tirs_creation(x, y):
    global direction, tirs_liste, tirs_cooldown
    # Création d'un tir avec la barre d'espace
    if (pyxel.btnr(pyxel.KEY_E) or pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT)) and tirs_cooldown >= 1000/(stats_joueur[8]*boost_ulti):
        pyxel.play(0, 5)
        tirs_liste.append([x, y + 12, 0, direction]) # Ajuste la position de départ
        tirs_cooldown = 0
    else:
        tirs_cooldown += 1
    

# Déplacement des projectiles
def tirs_deplacement():
    global tirs_liste
    # Déplacement des tirs vers la droite et suppression s'ils sortent du cadre
    for tir in tirs_liste:

        if tir[3] == 0:  # Si le tir est à droite
            tir[0] = tir[0] + 2  # Déplace le tir vers la droite
        else:
            tir[0] = tir[0] - 2  # Déplace le tir vers la gauche

        tir[2] = tir[2] + 2  # Ajout de la zone possible de projectile max
        if monstre.enemies_coord != [] :
            for elem in monstre.enemies_coord :
                if collision(elem[0],elem[1],elem[6],elem[5], tir[0], tir[1], 14, 6):
                    if tir in tirs_liste:
                        tirs_liste.remove(tir)
                    elem[8] -= 1*monstre.boost_degat_joueur*(hud.stats[3]/100)*double_hit()
                    if hud.degats_subi<0:
                        hud.degats_subi+=(hud.stats[2]/200)
                    else:
                        hud.degats_subi=0
                    if elem[8] <= 0:
                        monstre.drop_loot(elem[0], elem[1])
                        monstre.enemies_coord.remove(elem)
        if monstre.boss_ennemi_coord !=[]:
                if collision(monstre.boss_ennemi_coord[0],monstre.boss_ennemi_coord[1],monstre.boss_ennemi_coord[3],monstre.boss_ennemi_coord[2], tir[0], tir[1], 14, 6):
                    if tir in tirs_liste:
                        tirs_liste.remove(tir)
                    monstre.boss_ennemi_coord[4] -= 4.5*monstre.boost_degat_joueur*(hud.stats[3]/100)*double_hit()
                    hud.degats_subi+=(hud.stats[2]/200)
                    if monstre.boss_ennemi_coord[4] <= 0:
                        monstre.boss_ennemi_coord=[]
                        monstre.boss_info[monstre.boss_choix][0]=0
        if tir[2] > 128 or not (tir[0]>6 and tir[0]<256-6): #or verif_col_liste(tir[0], tir[1], WALL) or verif_col_liste(tir[0]+14, tir[1], WALL):  # Si le tir sort de l'écran ou s'il rencontre un mur
            try:
                tirs_liste.remove(tir)
            except:
                pass
        

def tirs_type(couleur):
    global TYPE, tirs_liste
    # Système d'attaque normal
    if TYPE == 0:
         for tir in tirs_liste:#je blt le chevalier
            if tir[3] == 0:
            # Si le perso est en dirrection de la droite
                pyxel.blt(tir[0], tir[1], 0, 48, 229, 14, 6, 4)#je blt le tir dans le fichier 4.pyxres
            else:
            # Si le perso est en dirrection de la droite
                pyxel.blt(tir[0], tir[1], 0, 66, 229, 14, 6, 4)
    elif TYPE == 1:
         for tir in tirs_liste:#je blt le chevalier
            pyxel.rect(tir[0], tir[1], 3, 3, couleur)#magicien avec le tir boule de magie # Execution du jeu en boucle
    elif TYPE == 2:
         for tir in tirs_liste:#je blt le chevalier
            if tir[3] == 0:
                pyxel.blt(tir[0], tir[1], 0, modèle_flèche[2], modèle_flèche[1], 14, 8, 3)
            else:
                pyxel.blt(tir[0], tir[1], 0, modèle_flèche[0], modèle_flèche[1], 14, 8, 3)


# Dégât causé par les ennemis
def degats():
    global x, y, h, l
    for elem in monstre.enemies_coord :
        if collision(elem[0], elem[1], elem[5], elem[6], x, y, h, l):
            hud.degats_subi -= 0.04*game_management.round_game*monstre.boost_degat_ennemi*((150-hud.stats[0])/150)
            if hud.stats[5]>0:
                elem[8] -= monstre.boost_degat_joueur*(hud.stats[5]/500)
                if hud.degats_subi<0:
                    hud.degats_subi+=(hud.stats[2]/200)/5
                else:
                    hud.degats_subi=0



# Fonction de rotation du personnage
def rotation():
    global TYPE, direction, l, h, u, v

    if TYPE == 0:
        if direction == 0:
            u, v = 1, 228
        if direction == 1:
            u, v = 34, 196
    if TYPE == 1:
        if direction == 0:
            u, v = 16, 227
        if direction == 1:
            u, v = 48, 195
    if TYPE == 2:
        if direction == 0:
            u, v = 32, 227
        if direction == 1:
            u, v = 64, 196


def capacitée():
    global direction,x,y,h,l,activation_stun,boss_stun,timeur,atk,conserve,info_flamme,modèle_flèche,boost_ulti,minuteur

    
    
    for elm in hud.ensemble_des_capacité_secondaire:
        if elm[4] and elm[8]<=elm[9][TYPE][0]:
            
            
            elm[8]+=1

            if TYPE ==0:
                if elm[7]==4:
                    if direction :
                        pyxel.blt(x-l-2,y+9,elm[9][0][1],elm[9][0][6],elm[9][0][7],elm[9][0][4],elm[9][0][5],1)
                        atk=[x-l-2,y+9,elm[9][0][4],elm[9][0][5]]
                    if not direction:
                        pyxel.blt(x-1,y+9,elm[9][0][1],elm[9][0][2],elm[9][0][3],elm[9][0][4],elm[9][0][5],1)
                        atk=[x-1,y+9,elm[9][0][4],elm[9][0][5]]
                    for element in monstre.enemies_coord:
                        if collision(atk[0],atk[1],atk[3],atk[2],element[0], element[1], element[6], element[5]):
                            element[8]-=elm[9][0][8]*monstre.boost_degat_joueur
                            hud.degats_subi+=(hud.stats[2]/200)/10
                    if monstre.boss_ennemi_coord!=[]:
                        if collision(atk[0],atk[1],atk[3],atk[2],monstre.boss_ennemi_coord[0],monstre.boss_ennemi_coord[1],monstre.boss_ennemi_coord[3],monstre.boss_ennemi_coord[2]):
                            monstre.boss_ennemi_coord[4]-=elm[9][0][8]*monstre.boost_degat_joueur/10
                            if hud.degats_subi<0:
                                hud.degats_subi+=(hud.stats[2]/200)/15
                            else:
                                hud.degats_subi=0
                if elm[7]==3:
                    pyxel.blt(x,y+6,0,65,178,14,14,1)
                    if conserve==0:
                        conserve=monstre.boost_degat_ennemi
                    monstre.boost_degat_ennemi=0 
                    

                    
                if elm[7]==2 and not activation_stun:
                    if not direction and elm[9][0][11]==0 :
                        elm[9][0][11],elm[9][0][1],elm[9][0][2],elm[9][0][12]=1,x,y+9,elm[9][0][4]
                        
                    if direction and elm[9][0][11]==0:
                        elm[9][0][11],elm[9][0][1],elm[9][0][2],elm[9][0][12]=-1,x,y+9,elm[9][0][9]
                        
                    if elm[9][0][0]>=timeur:
                        pyxel.blt(elm[9][0][1],elm[9][0][2],0,elm[9][0][12],elm[9][0][5],elm[9][0][6],elm[9][0][7],elm[9][0][8])
                        elm[9][0][1]+=2*elm[9][0][11]
                        timeur+=2
                        
                    
                   

                    
                    for elem in monstre.enemies_coord:
                        if collision(elm[9][0][1],elm[9][0][2],elm[9][0][7],elm[9][0][6],elem[0], elem[1], elem[5], elem[6]):
                            activation_stun=1
                            elem[11]=1
                    if monstre.boss_choix ==2 and collision(monstre.boss_info[monstre.boss_choix][1],monstre.boss_info[monstre.boss_choix][2],monstre.boss_info[monstre.boss_choix][7],monstre.boss_info[monstre.boss_choix][6],elm[9][0][1],elm[9][0][2],elm[9][0][7],elm[9][0][6]):
                        activation_stun=1
                        boss_stun=1
                

            if TYPE ==1:
                if elm[7]==4:
                    if info_flamme==0:
                        info_flamme=x-(32-l/2)
                    pyxel.blt(info_flamme,elm[9][1][1],elm[9][1][2],elm[9][1][3],elm[9][1][4],elm[9][1][5],elm[9][1][6],elm[9][1][7])
                    for things in monstre.enemies_coord:
                        if collision(info_flamme,elm[9][1][1],elm[9][1][6],elm[9][1][5],things[0],things[1],things[6],things[5]):
                            things[8]-=0.08*monstre.boost_degat_joueur
                            hud.degats_subi+=(hud.stats[2]/200)/10
                    if monstre.boss_ennemi_coord!=[]:
                        if collision(info_flamme,elm[9][1][1],elm[9][1][6]+3,elm[9][1][5],monstre.boss_ennemi_coord[0],monstre.boss_ennemi_coord[1],monstre.boss_ennemi_coord[3],monstre.boss_ennemi_coord[2]):
                            monstre.boss_ennemi_coord[4]-=0.25*monstre.boost_degat_joueur
                            hud.degats_subi+=(hud.stats[2]/200)/15
                if elm[7]==3:
                    if direction:
                        pyxel.blt(x-9,y-11,1,224,216,32,32,6)
                    if not direction:
                        pyxel.blt(x-8,y-11,1,224,184,32,32,6)
                    if hud.degats_subi<0:
                        hud.degats_subi+=0.3
                    else:
                        hud.degats_subi=0

                if elm[7]==2:
                    if not direction and elm[9][1][1]==0 :
                            elm[9][1][3],elm[9][1][2],elm[9][1][1],elm[9][1][4]=1,y+7,x,226
                        
                    if direction and elm[9][1][1]==0:
                            elm[9][1][3],elm[9][1][2],elm[9][1][1],elm[9][1][4]=-1,y+7,x,242
                    pyxel.blt(elm[9][1][1],elm[9][1][2],0,177,elm[9][1][4],14,14,1)
                    elm[9][1][1]+=1.2*elm[9][1][3]
                    for méchants in monstre.enemies_coord:
                        if collision(elm[9][1][1],elm[9][1][2],14,14,méchants[0],méchants[1],méchants[6],méchants[5]):
                            méchants[8]-=0.5*monstre.boost_degat_joueur
                            hud.degats_subi+=(hud.stats[2]/200)/10
                    if monstre.boss_ennemi_coord!=[]:
                        if collision(elm[9][1][1],elm[9][1][2],14,14,monstre.boss_ennemi_coord[0],monstre.boss_ennemi_coord[1],monstre.boss_ennemi_coord[3],monstre.boss_ennemi_coord[2]):
                            monstre.boss_ennemi_coord[4]-=0.7*monstre.boost_degat_joueur
                            hud.degats_subi+=(hud.stats[2]/200)/15
            if TYPE ==2:
                if elm[7]==4:
                    modèle_flèche=[98,180,80]
                    boost_ulti=6
                    if not direction :
                        pyxel.blt(x,y,0,80,228,l,h,6)    
                    if direction :
                        pyxel.blt(x,y,0,96,228,l,h,6)
                if elm[7]==3:
                    if not direction :
                        pyxel.blt(x,y,0,192,228,l,h,6)    
                    if direction :
                        pyxel.blt(x,y,0,208,228,l,h,6)
                    monstre.hidden=True
                    
                if elm[7]==2:
                    if elm[9][2][1]==0:
                        elm[9][2][1]=x
                    pyxel.blt(elm[9][2][1],132+32,0,226,241,12,14,1)
                            


        for item in monstre.enemies_coord:
            if item[8] <= 0:
                monstre.drop_loot(item[0], item[1])
                monstre.enemies_coord.remove(item)
        if  monstre.boss_ennemi_coord!=[] and monstre.boss_ennemi_coord[4] <= 0:
            monstre.boss_ennemi_coord=[]
            monstre.boss_info[monstre.boss_choix][0]=0
                        
                        

                       
        if not elm[8]<=elm[9][TYPE][0]:
            if TYPE==0:
                if elm[7]==3 and conserve!=0 :
                    monstre.boost_degat_ennemi=conserve
                    conserve=0 
            if TYPE==2:
                if elm[7]==3:
                    monstre.hidden=False
                if elm[7]==4:
                    boost_ulti=1
                    modèle_flèche=[66,244,48]
                if elm[7]==2:
                    
                    if elm[9][2][1]!=0:
                        pyxel.blt(elm[9][2][1],132+32,0,241,241,15,15,1)
                        minuteur+=1
                        for entity in monstre.enemies_coord:
                            if collision(elm[9][2][1],132+32,15,15,entity[0], entity[1], entity[5], entity[6]):
                                entity[8]-=0.4*monstre.boost_degat_joueur
                                hud.degats_subi+=(hud.stats[2]/200)/10
                        if monstre.boss_ennemi_coord!=[]:
                            if collision(elm[9][2][1],132+32,15+5,15+5,monstre.boss_ennemi_coord[0],monstre.boss_ennemi_coord[1],monstre.boss_ennemi_coord[3],monstre.boss_ennemi_coord[2]):
                                monstre.boss_ennemi_coord[4]-=0.3*monstre.boost_degat_joueur
                                hud.degats_subi+=(hud.stats[2]/200)/15

                    if minuteur>30:
                        minuteur=0
                        elm[9][2][1]=0
        

           
        if not elm[4] :
            elm[8]=0
            if TYPE==0:
                if elm[7]==2:
                    timeur=0
                    elm[9][0][11]=0
            if TYPE==1:
                if elm[7]==4:
                    info_flamme=0
                if elm[7]==2:
                    elm[9][1][1]=0
            
               

                
                
                
            
    if activation_stun>0 and activation_stun <=160:
        activation_stun+=1
        if boss_stun:
            monstre.stun=1
        
    else:
        activation_stun=0
        monstre.stun=0
        boss_stun=0
        for elm in monstre.enemies_coord:
            elm[11]=0

def orbes_afficher():
    global orbes_choix,coords_orbes,info_orbes,boost_orbs,x,y,h,l,valeur_random,valeur_1,valeur_2,valeur_3
    if not orbes_choix and not game_management.place_enemie:
        if monstre.enemies_coord==[]:
            if game_management.round_game%5!=0:
                boost_orbs=1
                if coords_orbes==[]:
                    valeur_random=randint(0,2)
                    coords_orbes.append([110,156,info_orbes[valeur_random][2]])
                pyxel.blt(119,156,0,info_orbes[valeur_random][0],info_orbes[valeur_random][1],18,18,1)
            
            if game_management.round_game%5==0 and not monstre.boss_info[monstre.boss_choix][0] :
                boost_orbs=1.5
                if coords_orbes==[]:
                    valeur_1=randint(0,2)
                    coords_orbes.append([23,156,info_orbes[valeur_1][2]])
                    valeur_2=randint(0,2)
                    coords_orbes.append([119,156,info_orbes[valeur_2][2]])
                    valeur_3=randint(0,2)
                    coords_orbes.append([215,156,info_orbes[valeur_3][2]])
                pyxel.blt(23,156,0,info_orbes[valeur_1][0],info_orbes[valeur_1][1],18,18,1)
                pyxel.blt(119,156,0,info_orbes[valeur_2][0],info_orbes[valeur_2][1],18,18,1)
                pyxel.blt(215,156,0,info_orbes[valeur_3][0],info_orbes[valeur_3][1],18,18,1)
        for elm in coords_orbes:
            if collision(x,y,h,l,elm[0],elm[1],18,18) and pyxel.btn(pyxel.KEY_F):
                loot.orbes(elm[2])
                coords_orbes=[]
                orbes_choix=1

    
    
        


            
        

            


