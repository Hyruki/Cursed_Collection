import pyxel

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
        if not pyxel.btn(pyxel.KEY_SPACE):
            curent_anim = player_anim['up']
    if pyxel.btn(pyxel.KEY_DOWN):
        coordinates[1] += 1
        if not pyxel.btn(pyxel.KEY_SPACE):
            curent_anim = player_anim['down']
    if pyxel.btn(pyxel.KEY_LEFT):
        coordinates[0] -= 1
        if not pyxel.btn(pyxel.KEY_SPACE):
            curent_anim = player_anim['left']
    if pyxel.btn(pyxel.KEY_RIGHT):
        coordinates[0] += 1
        if not pyxel.btn(pyxel.KEY_SPACE):
            curent_anim = player_anim['right']




pyxel.fullscreen = True

# Chargement des dessins
pyxel.load('sprites.pyxres')

# Fonction UPDATE qui execute à chaque FRAME
def update():
    # Touche Echape : Quitter le jeu
    if pyxel.btn(pyxel.KEY_ESCAPE):
        pyxel.quit()

    move_player()


# Fonction DRAW qui dessine à chaque FRAME
def draw():
    pyxel.cls(0)


    player = pyxel.blt(coordinates[0], coordinates[1], 0, curent_anim[0], curent_anim[1], curent_anim[2], curent_anim[3], curent_anim[4]) # Ajout du personnage de TEST

    print(curent_anim)


# Execution du jeu en boucle
pyxel.run(update, draw)