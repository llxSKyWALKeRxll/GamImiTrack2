import pygame
from gameSettings import *
from FlashArtPy_VideoBnW import *
from FlashArtPy_VideoCol import *
from FlashArtPy_VideoPix import *

def GamImiTrack2():
    pygame.init()
    width3, height3 = 800, 600
    resolution3 = width3, height3
    clock3 = pygame.time.Clock()
    pygame.display.set_caption('Flash Art')
    screen3 = pygame.display.set_mode(resolution3)
    bg_img3 = pygame.image.load(r"C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\bgImg1.jpg")
    font_style3 = pygame.font.Font(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\fonts\f2.ttf', 44)
    b3_1 = pygame.Rect(230, 100, 300, 50)
    b3_2 = pygame.Rect(230, 230, 300, 50) 
    b3_3 = pygame.Rect(230, 360, 300, 50) 
    o3_1 = pygame.Rect(220, 90, 320, 70) 
    o3_2 = pygame.Rect(220, 220, 320, 70)
    o3_3 = pygame.Rect(220, 350, 320, 70)
    t3_1 = font_style3.render('BnW Flash Art', True, yellow)
    t3_2 = font_style3.render('Coloured Flash Art', True, yellow)
    t3_3 = font_style3.render('Pixel Flash Art', True, yellow)
    screen3.fill(black)
    screen3.blit(bg_img3, (0, 0))
    pygame.draw.rect(screen3, yellow, o3_1)
    pygame.draw.rect(screen3, yellow, o3_2)
    pygame.draw.rect(screen3, yellow, o3_3)
    pygame.draw.rect(screen3, red, b3_1)
    pygame.draw.rect(screen3, red, b3_2)
    pygame.draw.rect(screen3, red, b3_3)
    screen3.blit(t3_1, b3_1)
    screen3.blit(t3_2, b3_2)
    screen3.blit(t3_3, b3_3)
    pygame.display.update()
    clock3.tick()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                        exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos3 = event.pos
                    if b3_1.collidepoint(mousePos3):
                        keys3 = pygame.key.get_pressed()
                        if keys3[pygame.K_ESCAPE]:
                            main_menuX = GamImiTrack2()
                        flash_art3 = FlashArt(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\Videos\hagler1.mp4')
                        flash_art3.execute()
                    if b3_2.collidepoint(mousePos3):
                        keys3 = pygame.key.get_pressed()
                        if keys3[pygame.K_ESCAPE]:
                            main_menuX = GamImiTrack2()
                        flash_art3 = FlashArtCol(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\Videos\hagler1.mp4')
                        flash_art3.execute()
                    if b3_3.collidepoint(mousePos3):
                        keys3 = pygame.key.get_pressed()
                        if keys3[pygame.K_ESCAPE]:
                            main_menuX = GamImiTrack2()
                        flash_art3 = FlashArtPix(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\Videos\hagler1.mp4')
                        flash_art3.execute()

#main_menu = GamImiTrack2()
