from utils import * 

# Affichage page en 1920x1080 (FullScreen)
pyxel.init(1920, 1080, "The Darkness Lord")

# Fonction UPDATE qui execute à chaque FRAME
def update():
    # Touche Echape : Quitter le jeu
    if pyxel.btn(pyxel.KEY_ESCAPE):
        pyxel.quit()

# Fonction DRAW qui dessine à chaque FRAME
def draw():
    pass

# Execution du jeu en boucle
pyxel.run(update, draw)