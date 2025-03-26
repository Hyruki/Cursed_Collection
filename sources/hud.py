#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
from utils import *
import joueur
import game_management

stats=joueur.stats_joueur

stats_affichage=[[10,56,0,80,16,16,16,6,30,56,str(stats[0]),0],[10,72,0,96,16,16,16,6,30,72,str(stats[1]),0],[10,88,0,112,16,16,16,6,30,88,str(stats[2]),0],[10,104,0,80,32,16,16,6,30,104,str(stats[3]),0],[10,120,0,96,32,16,16,6,30,120,str(stats[4]),0],[10,136,0,112,32,16,16,6,30,136,str(stats[5]),0],[10,152,0,80,48,16,16,6,30,152,str(stats[6]),0],[10,168,0,96,48,16,16,6,30,168,str(stats[7]),0],[10,184,0,112,48,16,16,6,30,184,str(stats[8]),0]]
degats_subi=0

couleur_butin=10
trapped_create=0
butin=0
valeur_butin=0
sauvegarde=0
capacité=0
coins = [(70,50,4,4,10), (90,50,4,4,10)] # x y w h color
récolte=0

dessin=[[ 237,249,'X',7 ],[217,249,0,0,120,5,8,1],[179,249,0,2,128,5,8,1],[198,248,0,9,127,5,8,1]]
dodge=[215, 250, pyxel.MOUSE_BUTTON_MIDDLE, 460, 0, dessin[1],1,3,0,[[60,],[120,],[100,]],pyxel.KEY_2]
attack1=[177, 250, pyxel.MOUSE_BUTTON_LEFT, 25, 0, dessin[2],1,1,0,0,pyxel.KEY_E]
attack2=[196, 250, pyxel.MOUSE_BUTTON_RIGHT, 140, 0, dessin[3],1,2,0,[[60,'x','y',0,80,213,16,6,4,96,213,0,0],[30,0,0,0,0],[60,0]],pyxel.KEY_1]
ulti=[234, 250, pyxel.KEY_X, 840, 0, dessin[0],0,4,0,[[180,0,81,164,29,8,82,148,10,1],[220,120+32,0,112,224,64,24,1],[240,]],pyxel.KEY_3]
ensemble_des_capacité_secondaire=[attack2,dodge,ulti]
temp=[0,0,0,0]

cam_x, cam_y = 0, 0


DECALAGE = 0
"""
def suivie_camera(camX, camY):
    global cam_x, cam_y

    dodge[1] = dodge[1] + camY
    print('CAM')


# Fonction d'affichage des coins ainsi que les collisions avec le joueur
def affichage_coins(joueur):
    for i in range(len(coins)):
            pyxel.rect(coins[i][0],coins[i][1],coins[i][2],coins[i][3],coins[i][4])#pour les tests
            if collision(coins[i][0],coins[i][1],coins[i][2],coins[i][3], joueur.x, joueur.y, joueur.h, joueur.l):
                ajout_coins()
                récolte_butin()
                coins.pop(i)
                break
        
def ajout_coins():
    global butin
    butin += 1
"""
def stats_mise_à_jour():
    global stats_affichage
    stats_affichage=[[10,56,0,80,16,16,16,6,30,56,str(joueur.stats_joueur[0]),0],[10,72,0,96,16,16,16,6,30,72,str(joueur.stats_joueur[1]),0],[10,88,0,112,16,16,16,6,30,88,str(joueur.stats_joueur[2]),0],[10,104,0,80,32,16,16,6,30,104,str(joueur.stats_joueur[3]),0],[10,120,0,96,32,16,16,6,30,120,str(joueur.stats_joueur[4]),0],[10,136,0,112,32,16,16,6,30,136,str(joueur.stats_joueur[5]),0],[10,152,0,80,48,16,16,6,30,152,str(joueur.stats_joueur[6]),0],[10,168,0,96,48,16,16,6,30,168,str(joueur.stats_joueur[7]),0],[10,184,0,112,48,16,16,6,30,184,str(joueur.stats_joueur[8]),0]]


def afficher_pv_perso():#afficher la vie actuel du perso
    global degats_subi
    pv_perso=joueur.stats_joueur[1]+degats_subi

    barre=[98,240]
    pv=(1*pv_perso)/joueur.stats_joueur[1]
    if pv>0.49:
        pyxel.blt(barre[0],barre[1],0,17,2,pv*60,12,1)
    if pv<0.5 and pv>0.19:
        pyxel.blt(barre[0],barre[1],0,1,18,pv*60,12,1)
    if pv<0.2:
        pyxel.blt(barre[0],barre[1],0,1,34,pv*60,12,1)
    if pv <= 0:
        game_management.isgameover = True
        degats_subi=0

    

 
def hud():
    global récolte
    if récolte>0:
        pyxel.blt(4,238,0,0,72,16,16,1)
        coef_particule=pyxel.frame_count//15%3
        pyxel.blt(9,240,0,8*coef_particule,88,6,6,1)
    else :
        pyxel.blt(4,238,0,16,72,16,16,1)
    pyxel.text(20,246,str(butin),10)
    
        
def gérer_capacité(x_pos, y_pos, key, cooldown, capacité, à_écrire,écrire,reconnaitre,key2):  #gère l'affichage
    global sauvegarde,x
    if écrire==0:
        pyxel.text(à_écrire[0],à_écrire[1],à_écrire[2],à_écrire[3])        
    else :
        pyxel.blt(à_écrire[0],à_écrire[1],à_écrire[2],à_écrire[3],à_écrire[4],à_écrire[5],à_écrire[6],à_écrire[7]) #quel touche il faut appuyer
      
    if capacité==True:
        pyxel.blt(x_pos, 239, 0, 19, 107, 9, 9, 1)    
    if capacité==False:
        pyxel.blt(x_pos, 239, 0, 3, 107, 9, 9, 1)
        if pyxel.btn(key) or pyxel.btn(key2):
            sauvegarde=capacité+reconnaitre

            x=pyxel.frame_count   
                                          #la couleur du badge


# AAA REFAIRE
def temp_capa():       #gère le cooldown
    global sauvegarde,dodge,attack1,attack2,ulti,x
    if sauvegarde==1:
        attack1[4]=True
        temp[0]=x
    if sauvegarde==2:
        attack2[4]=True
        temp[1]=x
    if sauvegarde==3:
        dodge[4]=True
        temp[2]=x
    if sauvegarde==4:
        ulti[4]=True
        temp[3]=x
    if pyxel.frame_count>temp[3]+ulti[3]-(stats[7]*1.5):
        ulti[4]=False
    if pyxel.frame_count>temp[2]+dodge[3]-stats[7]:
        dodge[4]=False
    if pyxel.frame_count>temp[1]+attack2[3]-(stats[7]*0.9):
        attack2[4]=False
        
    if pyxel.frame_count>temp[0]+(1000/(joueur.stats_joueur[8]*joueur.boost_ulti)):
        attack1[4]=False
    
        
    sauvegarde=0
    x=0


def HUD_initialisation():
    global cam_x, cam_y, dodge

    pyxel.rect(0,236,256,20,0) # Zone noir du HUD
    pyxel.rect(0,236,256,2,13)#barre grise du hud
    afficher_pv_perso()
    hud()

    gérer_capacité(dodge[0]+cam_x, dodge[1]+cam_y, dodge[2], dodge[3], dodge[4], dodge[5],dodge[6],dodge[7],dodge[10])
    gérer_capacité(ulti[0]+cam_x, ulti[1]+cam_y, ulti[2], ulti[3], ulti[4], ulti[5],ulti[6],ulti[7],ulti[10])
    gérer_capacité(attack2[0]+cam_x, attack2[1]+cam_y, attack2[2], attack2[3], attack2[4], attack2[5],attack2[6],attack2[7],attack2[10])
    gérer_capacité(attack1[0]+cam_x, attack1[1]+cam_y, attack1[2], attack1[3], attack1[4], attack1[5],attack1[6],attack1[7],attack1[10])       


def pause_menu():
    if game_management.ispause:

        pyxel.rect(0,0,256,256,7)

        pyxel.rect(82, 80, 90, 15, 3)
        pyxel.text(116, 84, "Resume", 7)
        
        pyxel.rect(82, 105, 90, 15,5)
        pyxel.text(114, 109, "Restart", 7)
        
        pyxel.rect(82, 130, 90, 15, 10)
        pyxel.text(120, 135, "Exit", 7)

        for elm in stats_affichage:
            pyxel.blt(elm[0],elm[1],elm[2],elm[3],elm[4],elm[5],elm[6],elm[7])
            pyxel.text(elm[8],elm[9]+5,elm[10],elm[11])

        if 82 <= pyxel.mouse_x <= 172 and 80 <= pyxel.mouse_y <= 95:
            pyxel.rectb(82, 80, 90, 15, 8)
            game_management.button_sound()
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                game_management.ispause = False

        elif 82 <= pyxel.mouse_x <= 172 and 105 <= pyxel.mouse_y <= 120:
            pyxel.rectb(82, 105, 90, 15, 8)
            game_management.button_sound()

            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                game_management.reset_game()

        elif 82 <= pyxel.mouse_x <= 172 and 130 <= pyxel.mouse_y <= 145:
            pyxel.rectb(82, 130, 90, 15, 8)
            game_management.button_sound()

            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.quit()
        else:
            game_management.reset_button_sound()