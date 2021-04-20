import pygame
import sys
from gameSettings import *
from FlashArtPy_VideoBnW import *
from FlashArtPy_VideoCol import *
from FlashArtPy_VideoPix import *
from gameSettings import *
from playerPOV import player
import math
from map import game_map
from RayCastingTechnique import ray_casting
from sprites import *
from RayCastingTechnique import *
from objects import *
from ImageManipulationMain import *
from temp_script import *
from SelfHavocMain import *

def GamImiTrack9():
    pygame.init()
    width9, height9 = 800, 600
    resolution9 = width9, height9
    clock9 = pygame.time.Clock()
    pygame.display.set_caption('GamImiTrack')
    screen9 = pygame.display.set_mode(resolution9)
    bg_img9 = pygame.image.load(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\bgImg2.jpg')
    font_style1 = pygame.font.Font(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\fonts\f2.ttf', 44)
    font_style2 = pygame.font.Font(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\fonts\f1.otf', 140)
    g9_o1 = pygame.Rect(30, 190, 320, 70)
    g9_o2 = pygame.Rect(30, 290, 320, 70)
    g9_o3 = pygame.Rect(30, 390, 320, 70)
    g9_o4 = pygame.Rect(30, 490, 220, 70)
    g9_b1 = pygame.Rect(40, 200, 300, 50)
    g9_b2 = pygame.Rect(40, 300, 300, 50)
    g9_b3 = pygame.Rect(40, 400, 300, 50)
    g9_b4 = pygame.Rect(40, 500, 200, 50)
    g9_t1 = font_style1.render('Self Havoc', True, yellow)
    g9_t2 = font_style1.render('Image Manipulation', True, yellow)
    g9_t3 = font_style1.render('Video Manipulation', True, yellow)
    g9_t4 = font_style1.render('EXIT', True, yellow)
    g9_t5 = font_style2.render('GamImiTrack', True, yellow, red)
    screen9.fill(black)
    screen9.blit(bg_img9, (0, 0))
    screen9.blit(g9_t5, (190, 20))
    pygame.draw.rect(screen9, yellow, g9_o1)
    pygame.draw.rect(screen9, yellow, g9_o2)
    pygame.draw.rect(screen9, yellow, g9_o3)
    pygame.draw.rect(screen9, yellow, g9_o4)
    pygame.draw.rect(screen9, red, g9_b1)
    pygame.draw.rect(screen9, red, g9_b2)
    pygame.draw.rect(screen9, red, g9_b3)
    pygame.draw.rect(screen9, red, g9_b4)
    screen9.blit(g9_t1, g9_b1)
    screen9.blit(g9_t2, g9_b2)
    screen9.blit(g9_t3, g9_b3)
    screen9.blit(g9_t4, g9_b4)
    pygame.display.update()
    clock9.tick()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos9 = event.pos
                if g9_b1.collidepoint(mousePos9):
                    g9_game = load_self_havoc()
                if g9_b2.collidepoint(mousePos9):
                    g9_image_manipulation = initializeImage()
                    g9_image_manipulation.execute()
                if g9_b3.collidepoint(mousePos9):
                    g9_flash_art = GamImiTrack2()
                if g9_b4.collidepoint(mousePos9):
                    exit()

final_project = GamImiTrack9()