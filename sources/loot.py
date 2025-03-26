#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
import random
from utils import *
import hud
import joueur
from random import randint

coins_list = [(32, 9, 8, 6, 7), 
         (50, 6, 5, 10, 7),
         (58, 1, 4, 15, 7),
         (65, 7, 5, 8, 7),
         (72, 6, 13, 10, 7)]

coins_present = []

coeurs_present = []

# Système de sauvegarde des coins dans la liste coins_present
def coins(x, y):
    alea_coins = random.randint(0, 4)

    # Le Y à la fin sert à l'animation des éléments
    # Le 1 est la direction dans laquel l'objet va
    # 1 : vers le haut / 0 : vers le bas
    coins_present.append([x, y, 1, coins_list[alea_coins][0], 
              coins_list[alea_coins][1], 
              coins_list[alea_coins][2], 
              coins_list[alea_coins][3], 
              coins_list[alea_coins][4], 
              y,
              1])

# Système de sauvegarde du coeur dans la liste coeurs_present
def coeur(x, y):
    # Le Y à la fin sert à l'animation des éléments
    # Le 1 est la direction dans laquel l'objet va
    # 1 : vers le haut / 0 : vers le bas
    coeurs_present.append([x, y, 1, 17, 17, 13, 12, 1, y, 1])

# Système d'affichage des coins dans la liste coins_present
def coins_show(x, y, h, l):
    for elem in coins_present :
        if coins_present != []:
            pyxel.blt(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7])

            if collision(elem[0], elem[1], elem[5], elem[6], x, y, h, l):
                coins_present.remove(elem)
                hud.butin += 1
                pyxel.play(3, 4)


# Système d'affichage du coeur dans la liste coeurs_present
def coeurs_show(x, y, h, l):
    for elem in coeurs_present :
        if coeurs_present != []:
            pyxel.blt(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7])

            if collision(elem[0], elem[1], elem[5], elem[6], x, y, h, l):
                coeurs_present.remove(elem)
                if hud.degats_subi+8 > 0:
                    hud.degats_subi=0
                else :
                    hud.degats_subi+=8
                    #hud.degats_subi = round(hud.degats_subi + 2)
                    pyxel.play(3, 3)

# Système d'animation des loots
def anim_all():
    if coins_present != []:
        for coin in coins_present:
            if coin[1] <= coin[8] + 3 and coin[9] == 1:
                coin[1] += 0.1
            else:
                coin[9] = 0
                if coin[1] >= coin[8] and coin[9] == 0:
                    coin[1] -= 0.1
                else:
                    coin[9] = 1              
    if coeurs_present != []:
        for coeur in coeurs_present:
            if coeur[1] <= coeur[8] + 3 and coeur[9] == 1:
                coeur[1] += 0.1
            else:
                coeur[9] = 0
                if coeur[1] >= coeur[8] and coeur[9] == 0:
                    coeur[1] -= 0.1
                else:
                    coeur[9] = 1
             
def orbes(couleur):
    if couleur==0:
        joueur.stats_joueur[randint(0,2)]+=randint(1,5)*joueur.boost_orbs

    if couleur==1:
        joueur.stats_joueur[randint(3,5)]+=randint(1,5)*joueur.boost_orbs

    if couleur==2:
        joueur.stats_joueur[randint(6,8)]+=randint(1,5)*joueur.boost_orbs
    

def show_all(x, y, h, l, pause):
    coins_show(x, y, h, l)
    coeurs_show(x, y, h, l)
    if not pause:
        anim_all()