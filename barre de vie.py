import pyxel
import math
pyxel.init(128,128,title="Zone de test")

vie_perso=10
boost_de_vie=0
vie_perso=vie_perso+boost_de_vie#la santé totale du perso
pyxel.load("vie.pyxres")
dégats_subit=0
pv_perso=vie_perso-dégats_subit

 
def barre_de_vie_perso():
    global vie_perso
    
    
    
def afficher_pv_perso():
    global vie_perso
    
    pv=(pv_perso*10)/vie_perso
    if pv>4.9:
        pyxel.blt(48,119,0,0,0,32,8,1)
    if pv<5 and pv>1.9:
        pyxel.blt(48,119,0,16,8,32,8,1)
    if pv<2:
        pyxel.blt(48,119,0,0,8,16,8,1)
        pyxel.blt(64,119,0,0,32,16,6,1)
    pyxel.blt(47,120,0,0,16,34,8,1)
    #liste_pv=[0]
    #liste_pv[0]=
    
    
    if pv<10.0 :
        pv=pv*10
        pv=math.floor(pv)
        pv=pv/10
        pv=str(pv)
        liste_pv=pv.split(".",1)
        liste_pv[0]=int(liste_pv[0])
        liste_pv[1]=int(liste_pv[1])
        
        
        if liste_pv[0]==8:                   #dizaines
            pyxel.blt(76,121,0,0,32,3,6,1)
            x=76
        if liste_pv[0]==7:
            pyxel.blt(73,121,0,0,32,6,6,1)
            x=73
        if liste_pv[0]==6:
            pyxel.blt(70,121,0,0,32,9,6,1)
            x=70
        if liste_pv[0]==5:
            pyxel.blt(67,121,0,0,32,12,6,1)
            x=67
        if liste_pv[0]==4:
            pyxel.blt(64,121,0,0,32,15,6,1)
            x=64
        if liste_pv[0]==3:
            pyxel.blt(61,121,0,0,32,18,6,1)
            x=61
        if liste_pv[0]==2:
            pyxel.blt(58,121,0,0,32,21,6,1)
            x=58
        if liste_pv[0]==1:
            pyxel.blt(55,121,0,0,32,24,6,1)
            x=55
        if liste_pv[0]==0:
            pyxel.blt(52,121,0,0,32,27,6,1)
            x=52
        
        
        if liste_pv[1]==8:                    #unitées
            pyxel.blt(x-1,121+2,0,0,32,1,4,1)
        if liste_pv[1]==7:
            pyxel.blt(x-1,121,0,0,32,1,6,1)
        if liste_pv[1]==6:
            pyxel.blt(x-1,121,0,0,32,1,6,1)
            pyxel.blt(x-2,121+5,0,0,32,1,1,1)
        if liste_pv[1]==5:
            pyxel.blt(x-1,121,0,0,32,1,6,1)
            pyxel.blt(x-2,121+3,0,0,32,1,3,1)
        if liste_pv[1]==4:
            pyxel.blt(x-1,121,0,0,32,1,6,1)
            pyxel.blt(x-2,121+1,0,0,32,1,5,1)
        if liste_pv[1]==3:
            pyxel.blt(x-2,121,0,0,32,2,6,1)
        if liste_pv[1]==2:
            pyxel.blt(x-2,121,0,0,32,2,6,1)
            pyxel.blt(x-3,121+4,0,0,32,1,2,1)
        if liste_pv[1]==1:
            pyxel.blt(x-2,121,0,0,32,2,6,1)
            pyxel.blt(x-3,121+2,0,0,32,1,4,1)
        if liste_pv[1]==9:
            pyxel.blt(x-1,121+4,0,0,32,1,2,1)
            
         
            
def update():
    barre_de_vie_perso()

def draw():
    pyxel.cls(0)
    pyxel.rect(0,0,128,128,0)
    afficher_pv_perso()
    
pyxel.run(update,draw)     