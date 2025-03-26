import pyxel #enlever les bltm
pyxel.init(256,256,title="Zone de test",fps=60)
vie_perso=10
boost_de_vie=6
pv_perso=10
#vie_perso=vie_perso+boost_de_vie#la santé totale du perso
pyxel.load("vie256.pyxres")
dégats_subit=0
#pv_perso=vie_perso-dégats_subit
xperso=0
yperso=10
hperso=10
lperso=10
xbutin=50
ybutin=12
hbutin=4
lbutin=4
couleur_butin=10
trapped_create=butin=valeur_butin=sauvegarde=capacité=x=dégats=0
pyxel.mouse(True)
personage=[vie_perso,boost_de_vie,pv_perso]
tableau=[161,106,0,0]
heal_liste=[1,2,5,0.01]
ennemi_test=[100,100,50,50,8,0.01]
dessin=[[ 237,249,'E',7 ],[217,249,0,0,120,5,8,1],[179,249,0,2,128,5,8,1],[198,248,0,9,127,5,8,1]]
dodge=[215, 250, pyxel.KEY_SPACE, 480, 0, dessin[1],1,3]
attack1=[177, 250, pyxel.MOUSE_BUTTON_LEFT, 25, 0, dessin[2],1,1]
attack2=[196, 250, pyxel.MOUSE_BUTTON_RIGHT, 140, 0, dessin[3],1,2]
ulti=[234, 250, pyxel.KEY_E, 840, 0, dessin[0],0,4]
temp=[0,0,0,0]
def perso(): #temporaire pour les tests
    global xperso,yperso
    if pyxel.btn(pyxel.KEY_D):
        xperso=xperso+1
    if pyxel.btn(pyxel.KEY_S):
        yperso=yperso+1
def afficher_pv_perso():#afficher la vie actuel du perso
    global personage
    barre=[98,240]
    pv=(personage[2]*100)/personage[0]
    if pv>49:
        pyxel.blt(barre[0],barre[1],0,1,2,pv/100*60,12,1)
    if pv<50 and pv>19:
        pyxel.blt(barre[0],barre[1],0,1,18,pv/100*60,12,1)
    if pv<20 and pv>0:
        pyxel.blt(barre[0],barre[1],0,1,34,pv/100*60,12,1)
    print(pv)
    
    
def vieperso(vie_perso,boost_de_vie,pv_perso):
    global personage
    personage[0]=vie_perso+boost_de_vie
    personage[2]=pv_perso+boost_de_vie
    return personage[0],personage[2]

def heal(pv_perso,heal_elm):
    global personage
    personage[2]=pv_perso+heal_elm
    if personage[2]>personage[0]:
        personage[2]=personage[0]
    return personage[2]
def dégatperso(dégats_subit,pv_perso):
    global personage
    personage[2]=pv_perso-dégats_subit
    return personage[2]
def testdégats():
    global ennemi_test,personage,dégats
    boost=False
    pyxel.rect(ennemi_test[0],ennemi_test[1],ennemi_test[2],ennemi_test[3],ennemi_test[4])
    if yperso<ennemi_test[1]+ennemi_test[3] and yperso+hperso>ennemi_test[1] and xperso<ennemi_test[0]+ennemi_test[2] and xperso+lperso>ennemi_test[0]:
        dégatperso(ennemi_test[5],personage[2])
    while boost==False and xperso==250:
        vieperso(personage[0],personage[1],personage[2])
        boost=True
    if xperso==200:
        heal(personage[2],heal_liste[3])
def récolte_butin():
    
    global récolte,butin,valeur_butin,xperso,yperso,hperso,x,lperso,xbutin,ybutin,hbutin,lbutin
    #print(xbutin)
    y=récolte=x=0
    if yperso<ybutin+hbutin and yperso+hperso>ybutin and xperso<xbutin+lbutin and xperso+lperso>xbutin:
        valeur_butin=1#le 1 est temporaire la variable dépendra de l'objet ramasé
        x=pyxel.frame_count#initialisation du minuteur
        xbutin=400#fait disparaitre le butin de la map
        butin=butin+valeur_butin
        valeur_butin=0
    if pyxel.frame_count>240 and xbutin==400 or xbutin==400 :
        for i in range (pyxel.frame_count<x+240):
            récolte=1
    else:
        récolte = 0
    return xbutin
        
 
def hud():
    global récolte
    if récolte>0:
        pyxel.blt(4,238,0,0,72,16,16,1)
        coef_particule=pyxel.frame_count//15%3
        pyxel.blt(9,240,0,8*coef_particule,88,6,6,1)
    else :
        pyxel.blt(4,238,0,16,72,16,16,1)
    pyxel.text(20,246,str(butin),10)
    
def boss_blanc(): #spawn du boss et affichage
    
    global trapped_create,tableau
    tableau[0]=tableau[0]+tableau[2]
    tableau[1]=tableau[1]+tableau[3]   #préparation mouvement
    if trapped_create==False:          #spawn
        pyxel.rect(tableau[0],tableau[1],55,80,7) #affichage
        
def gérer_capacité(x_pos, y_pos, key, cooldown, capacité, à_écrire,écrire,reconnaitre):  #gère l'affichage
    global sauvegarde,x
    if écrire==0:
        pyxel.text(à_écrire[0],à_écrire[1],à_écrire[2],à_écrire[3])        
    else :
        pyxel.blt(à_écrire[0],à_écrire[1],à_écrire[2],à_écrire[3],à_écrire[4],à_écrire[5],à_écrire[6],à_écrire[7]) #quel touche il faut appuyer
      
    if capacité==True:
        pyxel.blt(x_pos, 239, 0, 19, 107, 9, 9, 1)    
    if capacité==False:
        pyxel.blt(x_pos, 239, 0, 3, 107, 9, 9, 1)
        if pyxel.btn(key):
            sauvegarde=capacité+reconnaitre
            x=pyxel.frame_count                                  #la couleur du badge
    
def temp_capa():       #gère le cooldown
    global sauvegarde,esquive,ultime,attaque_simple,abilité_simple,dodge,attack1,attack2,ulti,x
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
    if pyxel.frame_count>temp[3]+ulti[3]:
        ulti[4]=False
    if pyxel.frame_count>temp[2]+dodge[3]:
        dodge[4]=False
    if pyxel.frame_count>temp[1]+attack2[3]:
        attack2[4]=False
    if pyxel.frame_count>temp[0]+attack1[3]:
        attack1[4]=False
    sauvegarde=0
    x=0
    
def piège():
    pass
        
            
def update():
    
    récolte_butin()
    
    perso()
    if yperso<ennemi_test[1]+ennemi_test[3] and yperso+hperso>ennemi_test[1] and xperso<ennemi_test[0]+ennemi_test[2] and xperso+lperso>ennemi_test[0]:
        dégatperso(ennemi_test[5],personage[2])

    
def draw():
    
    pyxel.cls(0)
    pyxel.rect(0,0,256,256,0)#initialisation de la zone
    
    pyxel.rect(0,236,256,2,13)#barre grise du hud
    testdégats()
    
    pyxel.rect(xperso,yperso,lperso,hperso,5)
    pyxel.rect(xbutin,ybutin,lbutin,hbutin,couleur_butin)#pour les tests
    
    afficher_pv_perso()
    hud()

    gérer_capacité(dodge[0], dodge[1], dodge[2], dodge[3], dodge[4], dodge[5],dodge[6],dodge[7])
    gérer_capacité(ulti[0], ulti[1], ulti[2], ulti[3], ulti[4], ulti[5],ulti[6],ulti[7])
    gérer_capacité(attack2[0], attack2[1], attack2[2], attack2[3], attack2[4], attack2[5],attack2[6],attack2[7])
    gérer_capacité(attack1[0], attack1[1], attack1[2], attack1[3], attack1[4], attack1[5],attack1[6],attack1[7])
    
    
    temp_capa()
    
     
    boss_blanc()#afficher le boss fonction
    
pyxel.run(update,draw)     