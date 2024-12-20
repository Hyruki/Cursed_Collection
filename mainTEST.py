import pyxel

pyxel.init(156, 156, "The Darkness Lord")

pyxel.load('sprites.pyxres')

player_x, player_y = 40, 40

gravity = 0.8
velocity = 0
jumping = False

on_floor = False

tile_size = 8

WALL = [(0,2),(1,2),(0,3),(1,3)]

def verif_col_liste(x, y, l):
    tile_x = int(x / tile_size)
    tile_y = int(y / tile_size)

    return pyxel.tilemap(0).pget(tile_x,tile_y) in l


def move_player():
    global player_x, player_y, jumping, velocity

    if pyxel.btn(pyxel.KEY_RIGHT) and not verif_col_liste(player_x+14, player_y, WALL) and not verif_col_liste(player_x+14, player_y+19, WALL):
        player_x += 1

    if pyxel.btn(pyxel.KEY_LEFT) and not verif_col_liste(player_x-1, player_y, WALL) and not verif_col_liste(player_x-1, player_y+19, WALL):
        player_x -= 1

    """if pyxel.btn(pyxel.KEY_UP) and not verif_col_liste(player_x, player_y-1, WALL) and not verif_col_liste(player_x+13, player_y-1, WALL):
        player_y -= 1
    if pyxel.btn(pyxel.KEY_DOWN) and not verif_col_liste(player_x, player_y+20, WALL) and not verif_col_liste(player_x+13, player_y+20, WALL):
        player_y += 1"""


    if pyxel.btn(pyxel.KEY_SPACE) and jumping == False and on_floor:
        jumping = True
    else: 
        jumping = False

def jump_sys():
    global jumping, velocity, on_floor
    if jumping:
        velocity = -5

    """if pyxel.btn(pyxel.KEY_UP):
        player_y -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y += 1"""

def update():
    global player_y, velocity, jumping, on_floor
  
    move_player()

    if verif_col_liste(player_x, player_y-1, WALL) or verif_col_liste(player_x+13, player_y-1, WALL):
        velocity = 0

    if not verif_col_liste(player_x, player_y+20, WALL) and not verif_col_liste(player_x+13, player_y+20, WALL):
        if velocity < 0.8:
            velocity += gravity
        on_floor = False
    else:
        on_floor = True
        velocity = 0

        jump_sys()




    player_y += velocity

 
         

def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 16*50, 16*50, 0)
    player = pyxel.blt(player_x, player_y, 0, 0, 32, 13, 19, 11)


# Execution du jeu en boucle
pyxel.run(update, draw)