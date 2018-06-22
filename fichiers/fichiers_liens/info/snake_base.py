import pygame
from pygame.constants import *
from random import randint

pygame.init()
fenetre = pygame.display.set_mode((640, 480))

serpent=[(3, 0), (2, 0), (1, 0), (0, 0)]
dir=(1,0)                                       # Vers la droite

# Efface la fenetre en affichant un rectangle noir
def effacer():
    pygame.draw.rect(fenetre, 
                     (0,0,0),           # noir
                     (0,0,640,480)      # toute la fenetre
                    ) 

# Dessine le serpent (des petits carres)
def dessineSerpent(L):
    for p in L:
        pygame.draw.rect(fenetre,
                         (0,255,0),                     # vert
                         (p[0]*10, p[1]*10, 10, 10)     # un carre de 10x10 pixels
                        )
    
# Fait avancer le serpent selon dir
def avancerSerpent(L, dir):
    tete = (L[0][0]+dir[0], L[0][1]+dir[1])         # nouvelle position de la tete
    L = [tete] + L[:-1]                             # décalage du corps
    return L

#Boucle infinie
x=0
continuer=1
while continuer:
    #Limitation de vitesse de la boucle
    #20 frames par secondes suffisent
    pygame.time.Clock().tick(20)
    
    ### Affichage ###
    effacer()
    dessineSerpent(serpent)
    pygame.display.flip()
    
    ### Avance le serpent ###
    serpent = avancerSerpent(serpent,dir)
    
    ### Gère les événements ###
    for event in pygame.event.get():   
        if event.type == QUIT:     
            pygame.quit()
            continuer = 0      
        elif event.type==KEYDOWN:
            if event.key == K_DOWN:
                dir=(0,1)
            elif event.key==K_RIGHT:
                dir = (1,0)
            elif event.key == K_LEFT:
                dir = (-1,0)
            elif event.key == K_UP:
                dir = (0,-1)



