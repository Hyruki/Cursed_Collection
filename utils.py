import pyxel
from data import *

# =============================== A LIRE ! ===================================
# CE SCRIPT A POUR BUT DE RANGER LES FONCTIONS ET DES VARIABLES IMPORTANTES 
# DU PROGRAMME POUR EVITER DE TOUT METTRE DANS LE MEME FICHIER AFIN D'AERER 
# L'ESPACE DE TRAVAIL
# ============================================================================

# Affichage page en 1920x1080 (FullScreen)
pyxel.init(256, 256, "The Darkness Lord")

player_anim = {'up' : (16, 0, 16, 16, 0), 
               'down' : (0, 0, 16, 16, 0), 
               'right' : (32, 0, 16, 16, 0), 
               'left' : (48, 0, 16, 16, 0)}

curent_anim = player_anim['down']

coordinates = [10, 10]


def move_player():
    global coordinates, curent_anim
    
    if pyxel.btn(pyxel.KEY_UP):
        coordinates[1] -= 1
        curent_anim = player_anim['up']
    if pyxel.btn(pyxel.KEY_DOWN):
        coordinates[1] += 1
        curent_anim = player_anim['down']
    if pyxel.btn(pyxel.KEY_LEFT):
        coordinates[0] -= 1
        curent_anim = player_anim['left']
    if pyxel.btn(pyxel.KEY_RIGHT):
        coordinates[0] += 1
        curent_anim = player_anim['right']


