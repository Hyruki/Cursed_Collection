#Projet  : Cursed Collection
#Auteurs : Newen Ruiz Gourbin , Quentin Carrez , Jules Rouger

import pyxel
import hud
import joueur
from utils import * 
import monstre
import game_management
import random   
import loot


pyxel.init(256, 256, "The Darkness Lord", fps=60)

pyxel.load('../data/vie256.pyxres')




# Fonction de Update
def update():
    # Fonction gérant le jeux de base
    game_management.gerer_son()
    hud.stats_mise_à_jour()
    game_management.pause()
    
    # Sélection des personnages | ETAT N°1
    if game_management.game_state ==1 :
        game_management.music_menu("start")

    # Sélection difficulté | ETAT N°2
    if game_management.game_state == 2:
        """if not game_management.gerer_sound:
            game_management.music_play[0] = 0
            game_management.gerer_sound = True"""
        game_management.music_menu("start")

    
    # Jeu de base | ETAT N°3
    if not game_management.isgameover and game_management.game_state == 3 and not game_management.ispause:
        monstre.nombre_ennemi_par_round()
        # Système de tir
        joueur.tirs_creation(joueur.x, joueur.y)
        joueur.tirs_deplacement()
        game_management.music_menu()
        game_management.music_game('start')

        # Mouvement complet du personnage avec gravité
        joueur.move_player()

        

        # Temps d'attente pour les capacités
        hud.temp_capa()
         

        # TEST | Nouvelle zone avec mouvement de caméra PAS TERMINE
        #if joueur.verif_col_liste(joueur.x, joueur.y, joueur.NEXT_ZONE):
         #   game_management.camera_deplacement(0,30)
          #  hud.suivie_camera(0,30)

        # Système de DEBUG MODE
        joueur.DEBUG_MODE()

        # Système de détection des dégâts reçus par la collision des ennemis 


        # Système de round
        game_management.round_sys()

        monstre.place_enemis(game_management.round_game)
    #gerer la musique
    
    
    #print(game_management.game_state)
         
# Fonction de Draw
def draw():


    # Système de couleur aléatoire pour le MAGE
    couleur = random.randint(1, 15)

    if game_management.game_state == 0 :
        game_management.menu()    
        game_management.music_menu("start")

    # Sélection des personnages | ETAT N°1
    if game_management.game_state == 1:
        game_management.selection_perso()

    # Sélection difficulté | ETAT N°2
    if game_management.game_state == 2:
        game_management.afficher_intro()
        game_management.difficultée()


    # Jeu de base | ETAT N°3
    if not game_management.isgameover and game_management.game_state == 3:
        
        pyxel.cls(0)
        pyxel.bltm(0, 0, 1, 0, 0, 100*50, 100*50, 0)
        # Affichage boss
        monstre.boss()
        joueur.orbes_afficher()
        #player = pyxel.blt(joueur.x, joueur.y, 0, 
         #                  joueur.u, joueur.v, 
          #                 joueur.l, joueur.h, 
           #                joueur.color)
        joueur.degats()
        
        # Fonction d'affichage des coins ainsi que les collisions avec le joueur hud.py
        #hud.affichage_coins(joueur)

        # Fonction de TEST de la zone de dégât
        #joueur.test_degat()
        
        
        

        # Fonction de TEST de l'affichage 
        if monstre.activation:
            monstre.mariline_monro()

        
       

        joueur.rotation()
        
        # Affichage de tous les ennemis
        monstre.affichages_enemies()

        # Affichage du loot drop par les ennemies
        loot.show_all(joueur.x, joueur.y, joueur.h, joueur.l, game_management.ispause)
        

        monstre.atk_boss()
        player = pyxel.blt(joueur.x, joueur.y, 0, 
                           joueur.u, joueur.v, 
                           joueur.l, joueur.h, 
                           joueur.color)
        joueur.capacitée()
        # Détection du type de tir selon le joueur sélectionné au début
        joueur.tirs_type(couleur)

        hud.HUD_initialisation()
        if not game_management.ispause:
            monstre.ennemis_cells()

        hud.pause_menu()
        
        if monstre.enemies_coord == [] and game_management.round_cooldown>0 and game_management.round_cooldown<100:
            pyxel.text(115, 115, f"Round {game_management.round_game}", 7)

   
    elif game_management.isgameover:
        game_management.game_over()
    
        #icone son
    game_management.son_icone()
    


        
    
    


pyxel.run(update, draw)#