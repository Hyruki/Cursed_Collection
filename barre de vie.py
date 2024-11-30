import pyxel
import math
pyxel.init(256,256,title="Zone de test")

vie_perso=10
boost_de_vie=0
vie_perso=vie_perso+boost_de_vie#la santé totale du perso
pyxel.load("vie256.pyxres")
dégats_subit=3.6
pv_perso=vie_perso-dégats_subit

 
def barre_de_vie_perso():
    global vie_perso
    
    
    
def afficher_pv_perso():
    global vie_perso
    x_barre=(256-60)/2
    y_barre=256-(4+12)
    pv=(pv_perso*10)/vie_perso
    if pv>4.9:
        pyxel.blt(x_barre,y_barre,0,1,2,60,12,1)
    if pv<5 and pv>1.9:
        pyxel.blt(x_barre,y_barre,0,1,18,60,12,1)
    if pv<2:
        pyxel.blt(x_barre,y_barre,0,1,34,30,12,1)
    pyxel.blt(x_barre-2,y_barre-2,0,0,48,64,16,1)
    
    
    if pv<10.0 :
        pv=pv*10
        pv=math.floor(pv)
        pv=pv/10
        pv=str(pv)
        liste_pv=pv.split(".",1)
        liste_pv[0]=int(liste_pv[0])
        liste_pv[1]=int(liste_pv[1])
        
        
        if liste_pv[0]==8:                #dizaines
            x=x_barre+9*6
            pyxel.blt(x,y_barre,0,0,64,3*2,12,1)
            
        if liste_pv[0]==7:
            x=x_barre+8*6
            pyxel.blt(x,y_barre,0,0,64,6*2,12,1)
            
        if liste_pv[0]==6:
            x=x_barre+7*6
            pyxel.blt(x,y_barre,0,0,64,9*2,12,1)
            
        if liste_pv[0]==5:
            x=x_barre+6*6
            pyxel.blt(x,y_barre,0,0,64,12*2,12,1)
           
        if liste_pv[0]==4:
            x=x_barre+5*6
            pyxel.blt(x,y_barre,0,0,64,15*2,12,1)
            
        if liste_pv[0]==3:
            x=x_barre+4*6
            pyxel.blt(x,y_barre,0,0,64,18*2,12,1)
           
        if liste_pv[0]==2:
            x=x_barre+3*6
            pyxel.blt(x,y_barre,0,0,64,21*2,12,1)
            
        if liste_pv[0]==1:
            x=x_barre+2*6
            pyxel.blt(x,y_barre,0,0,64,24*2,12,1)
            
        if liste_pv[0]==0:
            x=x_barre+1*6
            pyxel.blt(x,y_barre,0,0,64,27*2,12,1)
            
        
        
        if liste_pv[1]==8:                    #unitées
            pyxel.blt(x-1*2,y_barre+2*2,0,0,64,1*2,4*2,1)
        if liste_pv[1]==7:
            pyxel.blt(x-1*2,y_barre,0,0,64,1*2,6*2,1)
        if liste_pv[1]==6:
            pyxel.blt(x-1*2,y_barre,0,0,64,1*2,6*2,1)
            pyxel.blt(x-2*2,y_barre+5*2,0,0,64,1*2,1*2,1)
        if liste_pv[1]==5:
            pyxel.blt(x-1*2,y_barre,0,0,64,1*2,6*2,1)
            pyxel.blt(x-2*2,y_barre+3*2,0,0,64,1*2,3*2,1)
        if liste_pv[1]==4:
            pyxel.blt(x-1*2,y_barre,0,0,64,1*2,6*2,1)
            pyxel.blt(x-2*2,y_barre+1*2,0,0,64,1*2,5*2,1)
        if liste_pv[1]==3:
            pyxel.blt(x-2*2,y_barre,0,0,64,2*2,6*2,1)
        if liste_pv[1]==2:
            pyxel.blt(x-2*2,y_barre,0,0,64,2*2,6*2,1)
            pyxel.blt(x-3*2,y_barre+4*2,0,0,64,1*2,2*2,1)
        if liste_pv[1]==1:
            pyxel.blt(x-2*2,y_barre,0,0,64,2*2,6*2,1)
            pyxel.blt(x-3*2,y_barre+2*2,0,0,64,1*2,4*2,1)
        if liste_pv[1]==9:
            pyxel.blt(x-1*2,y_barre+4*2,0,0,64,1*2,2*2,1)
            
         
            
def update():
    barre_de_vie_perso()

def draw():
    pyxel.cls(0)
    pyxel.rect(0,0,256,256,0)
    afficher_pv_perso()
    
pyxel.run(update,draw)     