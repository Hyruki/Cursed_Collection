#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
import joueur
import monstre
import time
import loot
import hud
import random

musique=True
isgameover = False # Booléen du game over

ispause = False

info_difficultée=[[104,35,192,115,63,77,4,1.8],[16,157,64,181,64,75,4,1],[184,160,192,192,64,63,4,0.5]]
mode_de_jeu=0
gerer_sound=False
round_game = 1
round_cooldown = 0
place_enemie = False
# LE GAME STATE EST L'ETAT DANS LAQUEL L'UTILISATEUR CE SITUE
# Le 0 désigne le menu de base
# Le 1 désigne la selection du personnage
# Le 2 désigne le choix de difficultée
# Le 3 désigne le lancement du jeu
game_state = 0

PERSONNAGE = 0

butin = 0

cam_coordonnée = [0,0]
temp_attente=0
music_play =[0,0,0,0,0,0,0,0]

music_gameover = False

# Couleur des boutons de Game Over
rejouer_couleur = 7
quiter_couleur = 7

sound_button = False

def difficultée():
    global info_difficultée,mode_de_jeu,game_state,temp_attente
    for elm in info_difficultée:
        if joueur.collision(pyxel.mouse_x,pyxel.mouse_y,10,10,elm[0],elm[1],elm[5],elm[4]) :
            pyxel.blt(elm[0],elm[1],2,elm[2],elm[3],elm[4],elm[5],elm[6])
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and temp_attente>=15:
                mode_de_jeu=elm[7]
                game_state=3
                temp_attente=0
        


def afficher_intro():
    global temp_attente
    temp_attente+=1
    pyxel.bltm(0,0,2,0,0,256,256)
    pyxel.text(100,15,"Signez un contrat !",8)
    if joueur.collision(pyxel.mouse_x,pyxel.mouse_y,10,10,info_difficultée[0][0],info_difficultée[0][1],info_difficultée[0][5],info_difficultée[0][4]) or joueur.collision(pyxel.mouse_x,pyxel.mouse_y,10,10,info_difficultée[1][0],info_difficultée[1][1],info_difficultée[1][5],info_difficultée[1][4]) or joueur.collision(pyxel.mouse_x,pyxel.mouse_y,10,10,info_difficultée[2][0],info_difficultée[2][1],info_difficultée[2][5],info_difficultée[2][4]):
        button_sound()
    else:
        reset_button_sound()
    


# Fonction du menu
def menu():
        global game_state
        
        pyxel.rect(0, 0, 260, 260, 0)
        pyxel.mouse(True)

        pyxel.text(95, 50, "Cursed Collection", 7)
        pyxel.rect(100, 115, 50, 20, 5)
        pyxel.text(117, 122, "Play", 7)
        
        
        if 100 <= pyxel.mouse_x <= 150 and 115 <= pyxel.mouse_y <= 135:
            pyxel.rectb(100, 115, 50, 20, 8)
            button_sound()
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):

                game_state = 1
        else:
            reset_button_sound()
#bouton son
def son_icone():
    global musique
    if musique==False:
        pyxel.blt(224,0,0,32,72,32,32,1)
    if musique==True :
        pyxel.blt(224,0,0,64,72,32,32,1)
#gerer son
def gerer_son():
    global musique
    x=0
    if pyxel.btnr(pyxel.KEY_M) and musique==True and x<pyxel.frame_count:
        x=pyxel.frame_count
        musique=False
    if pyxel.btnr(pyxel.KEY_M) and musique==False and x<pyxel.frame_count:
        x=pyxel.frame_count
        musique=True
    
        
                

# Fonction du menu de selection du personnage
def selection_perso():
    global game_state, PERSONNAGE
    # les personnages fix du menu
    pyxel.rect(0,0,400,400,15) # Zone noir en arrière plan
    pyxel.blt(56, 75, 0, 0, 228, 14, 20,15) # Personnage gauche
    pyxel.blt(113, 75, 0, 16, 227, 16, 21,10)  # Personnage centre
    pyxel.blt(169, 75, 0, 32, 228, 16, 20,6)  # Personnage droit
    pyxel.blt(50,67,2,34,10,30,36,15)
    pyxel.blt(107,67,2,34,10,30,36,15)
    pyxel.blt(163,67,2,34,10,30,36,15)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 3, 3, 10)  # Curseur comme un petit rectangle jaune
    pyxel.text(86, 20,"select your player",1)
    pyxel.mouse(True)
    
    #si le curseur est sur l'un des personnages
    if 50 <= pyxel.mouse_x <= 80 and 67 <= pyxel.mouse_y <= 67+36:
        pyxel.blt(49,66,2,97,1,31,38,15)# Contour rouge si souris sur le personnage à la position (20, 50)
        button_sound()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            game_state = 2
            joueur.TYPE = 0
            joueur.stats_joueur=[random.randint(10,15),random.randint(110,135),random.randint(0,2),random.randint(100,110),random.randint(0,2),random.randint(0,2),random.randint(85,95),random.randint(0,2),random.randint(90,95)]
        
    elif 107 <= pyxel.mouse_x <= 107+30 and 67 <= pyxel.mouse_y <= 67+36:
        pyxel.blt(106,66,2,97,1,31,38,15)# Contour rouge si souris sur le personnage à la position (55, 50)
        button_sound()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            game_state = 2
            joueur.TYPE = 1
            joueur.stats_joueur=[random.randint(0,2),random.randint(90,100),random.randint(0,2),random.randint(120,135),random.randint(10,15),random.randint(0,2),random.randint(90,100),random.randint(15,30),random.randint(80,85)]
            joueur.generation_type()
            
    elif 163 <= pyxel.mouse_x <= 163+30 and 67 <= pyxel.mouse_y <= 67+36:
        pyxel.blt(162,66,2,97,1,31,38,15)# Contour blanc si souris sur le personnage à la position (90, 50)
        button_sound()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            game_state = 2
            joueur.TYPE = 2
            joueur.stats_joueur=[random.randint(0,2),random.randint(80,90),random.randint(5,10),random.randint(90,100),random.randint(0,2),random.randint(0,2),random.randint(110,125),random.randint(0,2),random.randint(110,120)]
            joueur.generation_type()
            
    else:
        reset_button_sound()



def music_menu(etat=None):
    global musique
    if etat == "start" and musique==True:
        if not music_play[0]:
            pyxel.playm(0, 0, True)
            music_play[0] = 1
            
    if (etat != "start" or not musique==True) and music_play[0] == 1:
        music_play[0] = 0
        print("STOP")
        pyxel.stop()
    
    

def music_game(etat=None):
    global musique
    if etat == "start" and musique==True:
        if not music_play[1]:
            pyxel.playm(1, 0, True)
            music_play[1] = 1
            
    if etat != "start" or not musique==True:
        music_play[1] = 0
        pyxel.stop()

def button_sound():
    global sound_button
    if not sound_button:
        pyxel.play(0, 14)
        sound_button = True

def reset_button_sound():
    global sound_button
    sound_button = False


# Fonction qui fait un ecran noir avec text 'YOU DIED'
def game_over():
    global isgameover, cam_coordonnée, music_gameover, rejouer_couleur, quiter_couleur


    if not music_gameover:
        music_game()
        pyxel.play(0, 6)
        music_gameover = True

    pyxel.rect(cam_coordonnée[0], cam_coordonnée[1], 256, 256, 0)
    pyxel.text(235//2, 238//2, f"VOUS ÊTES MORT(E) \nVOUS AVIEZ : {hud.butin} PIECE(s)", 7)

    pyxel.text(235//2, 238//2+30, "REJOUER", rejouer_couleur)
    pyxel.text(235//2, 238//2+60, "QUITER", quiter_couleur)

    if 235//2 <= pyxel.mouse_x <= 235//2 + 27 and 238//2+30 <= pyxel.mouse_y <= 238//2+35:
        rejouer_couleur = 13
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.stop(0)
            reset_game()
    else : rejouer_couleur = 7
    
    if 235//2 <= pyxel.mouse_x <= 235//2 + 27 and 238//2+60 <= pyxel.mouse_y <= 238//2+65:
        quiter_couleur = 13
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()
    else : quiter_couleur = 7

    pyxel.mouse(True)
# TEST TELEPORTATION MARILINE MONRO
def test_tp(x,y, cam):
    pass
#    joueur.x = x
 #   joueur.y = y
  #  cam(x-100, y-100)
   # cam_coordonnée[0], cam_coordonnée[1] = x-100, y-100

# NOCLIP TEST
def noclip():
    pass
   # joueur.noclip = True

def disable_noclip():
    pass
 #   joueur.noclip = False

def camera_deplacement(x, y):
    pass
#    global cam_coordonnée
#    cam_coordonnée[0], cam_coordonnée[1] = x, y
#    pyxel.camera(x, y)

def move_gui():
    pass

def pause():
    global ispause
    if pyxel.btnp(pyxel.KEY_A):
        if not ispause:
            ispause = True
        else:
            ispause = False

def round_sys():
    global round_game, round_cooldown, place_enemie
    if monstre.enemies_coord == [] and not place_enemie and joueur.coords_orbes==[] and joueur.orbes_choix :
        if round_cooldown == 0 and not monstre.boss_info[monstre.boss_choix][0] and joueur.coords_orbes==[]and joueur.orbes_choix:
            round_game += 1
        
        round_cooldown += 1
        if round_cooldown >= 100 :
            place_enemie = True
            round_cooldown = 0
            joueur.orbes_choix=0
    

def reset_game():
    global isgameover,ispause,round_game,round_cooldown,place_enemie,game_state,PERSONNAGE,butin,cam_coordonnée,music_play,music_gameover,rejouer_couleur,quiter_couleur,info_difficultée,musique,mode_de_jeu,gerer_sound,temp_attente,sound_button
   


    monstre.TEMP=0
    monstre.limite_ennemis=2

    monstre.boost_degat_ennemi=1
    monstre.boost_degat_joueur=1

    monstre.mariline_rouge=[32,160]
    monstre.mariline_mid=[0,192]
    monstre.TEMP_boss=0
    monstre.boss_choix=0
    monstre.bossatk1=[120,154-(82-32),1,128,56,16,16,7]
    monstre.bossatk2=[120,154-(82-32),1,144,56,16,16,7]
    monstre.boss_info=[[0,112,154-(82-32),1,96,56,32,72,7,monstre.bossatk1,monstre.bossatk2,0,0,15],[0,112,102+32,0,0,160,32,32,13,monstre.mariline_rouge,monstre.mariline_mid,0,0,20],[0,235,30,1,120,0,16,48,11,120,104,10,0,1000]]
    monstre.boss_ennemi_coord=[]

    monstre.nombre_ennemi=0
    monstre.perso1_x = 821

    monstre.perso1_y = 10

    monstre.message = ""

    monstre.en_mouvement = False

    monstre.restart_game = False

    monstre.compteur = 0

    monstre.hidden=0
    monstre.stun=0

    monstre.w = 32

    monstre.h = 32

    monstre.c = 0

    monstre.vitesse = 0.6
    monstre.vitesse_chasse = 0.8

    monstre.enemie_spawn_cooldown = 0

# TESSST
    monstre.activation = False

    monstre.enemies_coord=[]






 


    loot.coins_list = [(32, 9, 8, 6, 7), 
         (50, 6, 5, 10, 7),
         (58, 1, 4, 15, 7),
         (65, 7, 5, 8, 7),
         (72, 6, 13, 10, 7)]

    loot.coins_present = []

    loot.coeurs_present = []


    hud.DECALAGE = 0
    hud.stats=joueur.stats_joueur

    hud.stats_affichage=[[10,56,0,80,16,16,16,6,30,56,str(hud.stats[0]),0],[10,72,0,96,16,16,16,6,30,72,str(hud.stats[1]),0],[10,88,0,112,16,16,16,6,30,88,str(hud.stats[2]),0],[10,104,0,80,32,16,16,6,30,104,str(hud.stats[3]),0],[10,120,0,96,32,16,16,6,30,120,str(hud.stats[4]),0],[10,136,0,112,32,16,16,6,30,136,str(hud.stats[5]),0],[10,152,0,80,48,16,16,6,30,152,str(hud.stats[6]),0],[10,168,0,96,48,16,16,6,30,168,str(hud.stats[7]),0],[10,184,0,112,48,16,16,6,30,184,str(hud.stats[8]),0]]
    hud.degats_subi=0

    hud.couleur_butin=10
    hud.trapped_create=0
    hud.butin=0
    hud.valeur_butin=0
    hud.sauvegarde=0
    hud.capacité=0
    hud.coins = [(70,50,4,4,10), (90,50,4,4,10)] # x y w h color
    hud.récolte=0

    hud.dessin=[[ 237,249,'X',7 ],[217,249,0,0,120,5,8,1],[179,249,0,2,128,5,8,1],[198,248,0,9,127,5,8,1]]
    hud.dodge=[215, 250, pyxel.MOUSE_BUTTON_MIDDLE, 460, 0, hud.dessin[1],1,3,0,[[60,],[120,],[100,]],pyxel.KEY_2]
    hud.attack1=[177, 250, pyxel.MOUSE_BUTTON_LEFT, 25, 0, hud.dessin[2],1,1,0,0,pyxel.KEY_E]
    hud.attack2=[196, 250, pyxel.MOUSE_BUTTON_RIGHT, 140, 0, hud.dessin[3],1,2,0,[[60,'x','y',0,80,213,16,6,4,96,213,0,0],[30,0,0,0,0],[60,0]],pyxel.KEY_1]
    hud.ulti=[234, 250, pyxel.KEY_X, 840, 0, hud.dessin[0],0,4,0,[[180,0,81,164,29,8,82,148,10,1],[220,120+32,0,112,224,64,24,1],[240,]],pyxel.KEY_3]
    hud.ensemble_des_capacité_secondaire=[hud.attack2,hud.dodge,hud.ulti]
    hud.temp=[0,0,0,0]

    hud.cam_x, cam_y = 0, 0







    


    joueur.info_orbes=[[39,111,0],[103,111,1],[71,111,2]]
    joueur.orbes_choix=False
    joueur.coords_orbes=[]
    joueur.boost_orbs=1

    joueur.stats_joueur=[0,100,0,100,0,0,100,0,100]
    joueur.activation_stun=0
    joueur.debugmode=0#pour empêcher le joueur de fly avec flèche du haut

# Variable de Base
    joueur.x, joueur.y = random.choice([33,209]), 68
    joueur.l, joueur.h = 13, 20
    joueur.u, joueur.v = 1, 228

    joueur.valeur_random=0
    joueur.valeur_1=0
    joueur.valeur_2=0
    joueur.valeur_3=0
# Direction : 0 : Droite | 1 : Gauche
    joueur.direction = 0

    joueur.color = 15

    joueur.minuteur=0
    joueur.modèle_flèche=[66,244,48]
    joueur.conserve=0
    joueur.boss_stun=0
#vie_perso = 10

    joueur.boost_ulti=1

    joueur.atk=[]
    

    joueur.info_flamme=0
    joueur.timeur=0
    joueur.gravity = 1
    joueur.velocity = 0
    joueur.jumping = False

    joueur.on_floor = False

    joueur.noclip = False

    joueur.TYPE = 0

# Coordoné tiles des murs
#WALL = [(0,2),(1,2),(0,3),(1,3)]

    joueur.WALL =[(8,0),(9,0),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(9,3),(10,3),(1,2),(2,2),(0,21)]# [(11,2),(12,2),(13,2),(14,18),(15,18),(16,18)]

    joueur.NEXT_ZONE = [(0,1)]

# Liste des projectiles jetés
    joueur.tirs_liste = []

    joueur.tirs_cooldown = 0







    isgameover = False # Booléen du game over

    ispause = False

    info_difficultée=[[104,35,192,115,63,77,4,1.8],[16,157,64,181,64,75,4,1],[184,160,192,192,64,63,4,0.5]]
    mode_de_jeu=0
    gerer_sound=False
    round_game = 1
    round_cooldown = 0
    place_enemie = False
    # LE GAME STATE EST L'ETAT DANS LAQUEL L'UTILISATEUR CE SITUE
    # Le 0 désigne le menu de base
    # Le 1 désigne la selection du personnage
    # Le 2 désigne le choix de difficultée
    # Le 3 désigne le lancement du jeu
    game_state = 0

    PERSONNAGE = 0

    butin = 0

    cam_coordonnée = [0,0]
    temp_attente=0
    music_play =[0,0,0,0,0,0,0,0]

    music_gameover = False

    # Couleur des boutons de Game Over
    rejouer_couleur = 7
    quiter_couleur = 7

    sound_button = False