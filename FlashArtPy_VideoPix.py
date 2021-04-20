import pygame
import cv2
import numpy
import pygame.gfxdraw

class FlashArtPix:
    def __init__(self, vid_path, pxl_size=5, colour_lvl = 16):
        pygame.init()
        self.video_path = vid_path
        self.capture_video = cv2.VideoCapture(vid_path)
        self.colour_level = colour_lvl
        self.pixel_size = pxl_size
        self.image = self.load_image()
        self.width = self.image.shape[0]
        self.height = self.image.shape[1]
        #self.width = 800
        #self.height = 600
        #self.image = cv2.resize(self.image, (0, 0), fx=0.1, fy=0.1)
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.resolution = self.width, self.height
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        r'''self.ascii_symbols = '01!\/|@#^*+ILVXT%!'
        self.est_ascii_index = 255 // (len(self.ascii_symbols) - 1)
        self.font = pygame.font.SysFont(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Flash Art\Pixelated_FlashArt_ASCII\FlashArtFonts_Pixelated\f2.ttf', font_size, bold=True)
        self.symbol_gap = int(font_size * 0.5)'''
        #self.rendered_ascii_symbols = [self.font.render(char, False, (255, 255, 255)) for char in self.ascii_symbols]
        self.colour_collection, self.colour_coEfficient = self.rendered_colour_collection()

    def load_image(self):
        temp, self.cv_image = self.capture_video.read()
        if not temp:
            f2 = FlashArt(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\Videos\hagler1.mp4')
            f2.execute()
        inverted_image = cv2.transpose(self.cv_image) #To rectify the inversion of the image display in pygame window
        img = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB)
        #bNw_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
        return img

    def draw_ascii_art(self):
        modified_image = cv2.resize(self.cv_image, (580, 430), interpolation=cv2.INTER_AREA)
        cv2.imshow('Original Image ', modified_image)

    def draw_modified_image(self):
        #symbol_locations = self.bnw_image // self.est_ascii_index
        self.image = self.load_image()
        colour_locations = self.image // self.colour_coEfficient
        for i in range(0, self.width, self.pixel_size):
            for j in range(0, self.height, self.pixel_size):
                colour_key = tuple(colour_locations[i, j])
                if sum(colour_key):
                    colour = self.colour_collection[colour_key]
                    pygame.gfxdraw.box(self.screen, (i, j, self.pixel_size, self.pixel_size), colour)
                '''symbol_location = symbol_locations[i, j]
                if symbol_location:
                    symbol = self.ascii_symbols[symbol_location]
                    colour = tuple(colour_locations[i, j])
                    self.screen.blit(self.colour_collection[symbol][colour], (i, j))'''

    def rendered_colour_collection(self):
        colours, colour_coEff = numpy.linspace(0, 255, num=self.colour_level, dtype=int, retstep=True)
        colour_collection = [numpy.array([c1, c2, c3]) for c1 in colours for c2 in colours for c3 in colours]
        #colour_dictionary = dict.fromkeys(self.ascii_symbols, None)
        colour_dictionary = {}
        colour_coEff = int(colour_coEff)
        #for symbol in colour_dictionary:
            #symbol_depth = {}
        for colour in colour_collection:
            colour_key = tuple(colour // colour_coEff)
            #symbol_depth[colour_key] = self.font.render(symbol, False, tuple(colour))
            colour_dictionary[colour_key] = colour
        #colour_dictionary[symbol] = symbol_depth
        return colour_dictionary, colour_coEff

    def draw_image(self):
        #pygame.surfarray.blit_array(self.screen, self.image)
        #cv2.imshow('Flash_Art', self.image)
        self.screen.fill((0, 0, 0))
        self.draw_modified_image()
        self.draw_ascii_art()

    def save_image(self):
        image = pygame.surfarray.array3d(self.screen)
        cv_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(r'C:\Users\rebor\Desktop\Academics 2k21\Group Project 2k21\Combined2\output\Pixel_Flash_Art_Screenshot.png', cv_image)

    def execute(self):
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    exit()
                elif x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_SPACE:
                        self.save_image()
            self.draw_image()
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(25)

#flash_art = FlashArtPix('C:\\Users\\rebor\\Desktop\\Academics 2k21\\Group Project 2k21\\Flash Art\\VideoPix_FlashArt_ASCII\\FlashArt_VideosPix\\hagler1.mp4')
#flash_art.execute()