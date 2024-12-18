import pyxel

pyxel.init(256, 256, "The Darkness Lord")

pyxel.load('sprites.pyxres')

player_x, player_y = 50, 50

gravity = 1
jump_h = 10
velocity = jump_h
jumping = False

WALL = [(0,2),(1,2),(0,3),(1,3)]

def move_player():
    global player_x, player_y, jumping, velocity

    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.tilemap(0).pget((player_x+13)//8, player_y//8) not in WALL:
        player_x += 1

    if pyxel.btn(pyxel.KEY_LEFT) and pyxel.tilemap(0).pget((player_x-1)//8, player_y//8) not in WALL:
        player_x -= 1

    if pyxel.btn(pyxel.KEY_SPACE) and jumping == False:
        jumping = True




    """if pyxel.btn(pyxel.KEY_UP):
        player_y -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y += 1"""

def update():
    global player_y, velocity, jumping
  
    move_player()

    if pyxel.tilemap(0).pget((player_x)//8, (player_y+19)//8) not in WALL:
        player_y += gravity 
    else:

        if jumping:
            print("JUMPING")
            player_y -= velocity
            velocity -= gravity
        else:
            print("NOOOOOT JUMPING")
            jumping = False
            velocity = jump_h

        jumping = False
        
         

def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 16*50, 16*50, 0)
    player = pyxel.blt(player_x, player_y, 0, 0, 32, 13, 19, 11)


# Execution du jeu en boucle
pyxel.run(update, draw)