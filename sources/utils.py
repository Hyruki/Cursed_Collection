#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel

tile_size = 8

# Détection de collisions par rapport à des coordonées d'un object

def collision(xobjet, yobjet, hobjet, lobjet, xperso,yperso,hperso,lperso):
    global butin
    
    if yperso<yobjet+hobjet and yperso+hperso>yobjet and xperso<xobjet+lobjet and xperso+lperso>xobjet:
        return True

    return False


# Détection collisions par rapport à une liste et des tuiles 

def verif_col_liste(x, y, l):
    tile_x = int(x / tile_size)
    tile_y = int(y / tile_size)
    return pyxel.tilemap(1).pget(tile_x,tile_y) in l