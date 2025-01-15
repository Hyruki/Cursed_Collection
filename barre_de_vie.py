import pyxel
pyxel.init(256,256,title="Zone de test")
vie_perso=10
boost_de_vie=0
vie_perso=vie_perso+boost_de_vie#la santé totale du perso
pyxel.load("vie256.pyxres")
dégats_subit=0
pv_perso=vie_perso-dégats_subit
xperso=0
yperso=10
hperso=10
lperso=10
xbutin=50
ybutin=12
hbutin=4
lbutin=4
couleur_butin=10
valeur_butin=0
butin=0
x=0
temporaire=0
ultime=attaque_basique=esquive=abilité_simple=False
cooldown_ultime=420
cooldown_esquive=270
cooldown_attaque_basique=25
cooldown_abilité_simple=140
pyxel.mouse(True)
trapped_create=False
x_boss_tableau_blanc=161
y_boss_tableau_blanc=106
def perso():
    global xperso
    if pyxel.btn(pyxel.KEY_D):
        xperso=xperso+1
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
    #pyxel.blt(x_barre-2,y_barre-2,0,0,48,64,16,1)
def récolte_butin():
    global récolte,butin,valeur_butin,xperso,yperso,hperso,x,lperso,xbutin,ybutin,hbutin,lbutin
    récolte=y=0
    if yperso<ybutin+hbutin and yperso+hperso>ybutin and xperso<xbutin+lbutin and xperso+lperso>xbutin:
        valeur_butin=1
        x=pyxel.frame_count
        xbutin=400
        butin=butin+valeur_butin
        valeur_butin=0
    if x>y:
        for i in range(pyxel.frame_count<x+50):
            récolte=1
        if récolte==0:
            y=x
def capacité_espace():
    global esquive,cooldown_esquive,temporaire
    pyxel.blt(230-15,250,0,0,120,9,3,1)
    if esquive==False:
        pyxel.blt(230-15,239,0,3,107,9,9,1)
        if pyxel.btnr(pyxel.KEY_SPACE):
            esquive=True
            temporaire=pyxel.frame_count
    if esquive ==True:
        pyxel.blt(230-15,239,0,19,107,9,9,1)
    if pyxel.frame_count>temporaire+cooldown_esquive:
        esquive=False
def capacité_e():
    global ultime,cooldown_ultime,temporaire
    pyxel.text(247-10,249,'E',7)
    if ultime==False:
        pyxel.blt(234,239,0,3,107,9,9,1)
        if pyxel.btnr(pyxel.KEY_E):
            ultime=True
            temporaire=pyxel.frame_count
    if ultime ==True:
        pyxel.blt(234,239,0,19,107,9,9,1)
    if pyxel.frame_count>temporaire+cooldown_ultime:
        ultime=False
def attaque_secondaire():
    global abilité_simple,cooldown_abilité_simple,temporaire
    pyxel.blt(198,248,0,9,127,5,8,1)
    if abilité_simple==False:
        pyxel.blt(196,239,0,3,107,9,9,1)
        if pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
            abilité_simple=True
            temporaire=pyxel.frame_count
    if abilité_simple ==True:
        pyxel.blt(196,239,0,19,107,9,9,1)
    if pyxel.frame_count>temporaire+cooldown_abilité_simple:
        abilité_simple=False
def attaque_principale():
    global attaque_basique,cooldown_attaque_basique,temporaire
    pyxel.blt(179,249,0,2,128,5,8,1)
    if attaque_basique==False:
        pyxel.blt(177,239,0,3,107,9,9,1)
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            attaque_basique=True
            temporaire=pyxel.frame_count
    if attaque_basique ==True:
        pyxel.blt(177,239,0,19,107,9,9,1)
    if pyxel.frame_count>temporaire+cooldown_attaque_basique:
        attaque_basique=False
def hud():
    global récolte
    if récolte>0:
        pyxel.blt(4,238,0,0,72,16,16,1)
        coef_particule=pyxel.frame_count//15%3
        pyxel.bltm(9,240,0,6*coef_particule,16,6,6,1)
    else :
        pyxel.blt(4,238,0,16,72,16,16,1)
    ecrire_score=str(butin)
    pyxel.text(20,246,ecrire_score,10)
def boss_blanc():
    global trapped_create,x_boss_tableau_blanc,y_boos_tableau_blanc
    x_blanc=x_boss_tableau_blanc
    y_blanc=y_boss_tableau_blanc
    if trapped_create==False:
        for i in range(5):          #largeur
            for i in range(7):      #hauteur
                pyxel.blt(x_blanc,y_blanc,1,0,0,8,8,1)
                y_blanc=y_blanc+8
            y_blanc=y_boss_tableau_blanc
            x_blanc=x_blanc+8
        
            
def update():
    récolte_butin()
    perso()
def draw():
    boss_blanc()
    pyxel.cls(0)
    pyxel.rect(0,0,256,256,0)
    afficher_pv_perso()
    pyxel.bltm(0,236,0,0,0,512,2,1)
    pyxel.rect(xperso,yperso,lperso,hperso,5)
    pyxel.rect(xbutin,ybutin,lbutin,hbutin,couleur_butin)
    hud()
    capacité_e()
    capacité_espace()
    attaque_secondaire()
    attaque_principale()
    boss_blanc()
    
pyxel.run(update,draw)