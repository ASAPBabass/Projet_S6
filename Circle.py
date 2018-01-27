#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import random
import sys
from math import pi

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()


WIDTH = 640
HEIGHT = 480
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)


colors = {WHITE,BLACK,BLUE,RED,GREEN}

# initialisation de la fenetre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SwitchColor")
clock = pygame.time.Clock() # fps

background = pygame.image.load("Vue/Image/planete1.jpg").convert()
#screen.blit(background,(0,0))



class Ball(pygame.sprite.Sprite) :

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Vue/Image/redball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        #self.image = pygame.Surface((50,50))
        #self.image.fill(color)
        #self.image.fill(a)
        #self.image.set_alpha(128)
        #pygame.gfxdraw.filled_circle(self.image,25,25,25,RED)
        

    def jump(self) :
        self.rect.y -= 40
    
    def update(self) : # gravite
        if self.rect.y < 410 :
            self.rect.y += 2

class Circle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (640 / 2, 480 / 2)
        
        self.coord_3 = 75
        self.i = 0.02  # vitesse de rotation

        pygame.draw.arc(
            self.image, WHITE, self.rect, 0 + self.i, pi / 2 + self.i, 2)
        pygame.draw.arc(
            self.image, GREEN, self.rect, pi / 2 + self.i, pi + self.i, 2)
        pygame.draw.arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 2)
        pygame.draw.arc(
            self.image, RED,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 2)

        

    def fifou(self, screen):
        pygame.draw.arc(
            screen, WHITE, [320, 75, self.coord_3, 75], 0 + self.i, pi / 2 + self.i, 2)
        pygame.draw.arc(
            screen, GREEN, [320, 75, self.coord_3, 75], pi / 2 + self.i, pi + self.i, 2)
        pygame.draw.arc(
            screen, BLUE, [320, 75, self.coord_3, 75], pi + self.i, 3 * pi / 2 + self.i, 2)
        pygame.draw.arc(
            screen, RED,  [320, 75, self.coord_3, 75], 3 * pi / 2 + self.i, 2 * pi + self.i, 2)

    def update(self):
        self.coord_3 += 1

    def set(self):
        self.coord_3 = 75
        

pygame.key.set_repeat(400,30)

all_sprites = pygame.sprite.Group() # permet de regrouper les sprites

def intro() :
    intro = True
    intro_background = pygame.image.load("Vue/Image/planete1.jpg")
    screen.blit(intro_background,(0,0))
    while intro :
        
        for event in pygame.event.get() :
            if event.type == QUIT : 
                pygame.quit()
                quit()
            else :
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN :
                    circle_loop()
                    intro = False
        pygame.display.flip()

    pygame.quit()
    quit()


def ligne(l) :
    if l < 640 :
        return l+1
    else : return 0

def circle_loop():

    end = False

    ball = Ball()
    cercle = Circle()
    all_sprites.add(ball)
    #all_sprites.add(cercle)

    #objet = Cercle(300,200,50,RED)

    coord = 75
    coord1 = 75
    coord2 = 75
    coord3 = 75
    i = 1
    #parametrage des lignes mutlicolor
    wgreen = 426
    wred = 0
    wblue = 213

    wgreen2 = 640
    wred2 = 213
    wblue2 = 426


    
    while not end :
        # Events
        try :
            for event in pygame.event.get() :
                if event.type == QUIT :
                    end = True
                else :
                    if event.type == KEYDOWN :
                        if event.key == K_SPACE  :
                            #ball.jump()
                            all_sprites.jump()
                            
                        if event.key == K_q :
                            end = True
        except Exception :
            print("Erreur !")

        #print(circle.rect.x,circle.rect.y,circle.rect.height,circle.rect.width)
        
    
        

        # Update
        all_sprites.update() # met a jour tous les sprites

        # Draw / render
        #screen.fill(WHITE)
        screen.blit(background,(0,0))
        all_sprites.draw(screen) # affiche tous les sprites

    

        #cercle multicolor
        pygame.draw.arc(screen, WHITE,[320, coord2, coord+i, coord1], 0+i, pi/2+i, 2)
        pygame.draw.arc(screen, GREEN,[320, coord2, coord+i, coord1], pi/2+i, pi+i, 2)
        pygame.draw.arc(screen, BLUE, [320 ,coord2, coord+i, coord1], pi+i,3*pi/2+i, 2)
        pygame.draw.arc(screen, RED,  [320, coord2, coord+i, coord1], 3*pi/2+i, 2*pi+i, 2)

        pygame.draw.arc(screen, WHITE,[100, coord2, coord, coord1], 0+i, pi/2+i, 10)
        pygame.draw.arc(screen, GREEN,[100, coord2, coord, coord1], pi/2+i, pi+i, 10)
        pygame.draw.arc(screen, BLUE, [100, coord2, coord, coord1], pi+i,3*pi/2+i, 10)
        pygame.draw.arc(screen, RED,  [100, coord2, coord, coord1], 3*pi/2+i, 2*pi+i, 10)

        #pygame.draw.lines(screen, RED, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

        #pygame.draw.aaline(screen, GREEN, [0, 400],[640, 400], True) # [width,height] to [width,height] une ligne
        
        #ligne multicolor
        wblue = ligne(wblue)
        wblue2 = ligne(wblue2)
        wgreen = ligne(wgreen)
        wgreen2 = ligne(wgreen2)
        wred = ligne(wred)
        wred2 = ligne(wred2)
        
        
        #pygame.draw.lines(screen, GREEN, False, [[426,400],[640,400]],6)
        pygame.draw.lines(screen, BLUE, False, [[wblue,400],[wblue2,400]],6)
        pygame.draw.lines(screen, GREEN, False, [[wgreen,400],[wgreen2,400]],6)
        pygame.draw.lines(screen, RED, False, [[wred,400],[wred2,400]],6)
        pygame.draw.lines(screen, BLUE, False, [[wblue,400],[wblue2,400]],6)
        
        
        #pygame.draw.lines(screen, RED, False, [[400-l,400],[400,400]],6)

        #pygame.draw.lines(screen, GREEN, False, [[600,300],[10,300]],6)
        pygame.gfxdraw.line(screen,600,300,10,300,GREEN)
        #pygame.gfxdraw.hline(screen,50,200,300,RED)

        center = [150, 200]
        #pygame.gfxdraw.aacircle(screen, center[0], center[1], 105, WHITE)
        #pygame.gfxdraw.aacircle(screen, center[0], center[1], 120, WHITE)
        #pygame.draw.arc(screen,RED, [30,70,240,245],0+i, pi/2+i, 20)

        coord = 200
        coord1 = 200
        i += 0.02

       
        

        

        # Flip
        pygame.display.flip() # met à jour la fenetre
        clock.tick(60)


#intro()
circle_loop()
pygame.quit()

quit()
