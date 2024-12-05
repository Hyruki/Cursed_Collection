import pyxel
pyxel.init(256,256,title="Zone de test")
vie_perso=10
boost_de_vie=0
vie_perso=vie_perso+boost_de_vie#la santé totale du perso
pyxel.load("vie256.pyxres")
dégats_subit=0
pv_perso=vie_perso-dégats_subit
def afficher_pv_perso():
    x_barre=98
    y_barre=240
    pv=(pv_perso*vie_perso)/100
    if pv>0.49:
        pyxel.blt(x_barre,y_barre,0,1,2,pv*60,12,1)
    if pv<0.5 and pv>0.19:
        pyxel.blt(x_barre,y_barre,0,1,18,pv*60,12,1)
    if pv<0.2:
        pyxel.blt(x_barre,y_barre,0,1,34,pv*60,12,1)
    pyxel.blt(x_barre-2,y_barre-2,0,0,48,64,16,1)            
def update():
    pass
def draw():
    pyxel.cls(0)
    pyxel.rect(0,0,256,256,0)
    afficher_pv_perso()
pyxel.run(update,draw)     