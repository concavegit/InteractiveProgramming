import pygame
from pygame.locals import *
import time
from random import randint


class Model:
    '''Holds the model of the game state'''

    def __init__(self, size):
        self.spaceship = Spaceship()

class WindowView:
    def __init__(self, model, size):
        '''Initialize the view with a reference to the model and
        screen dimensions (width, height)
        '''
        self.model = model
        self.size = size
        self.screen = pygame.display.set_mode(size) #size is indicated below

    def draw(self):
        self.screen.fill(pygame.Color(255, 255, 255)) #background color, will be background, foreground
        #self.model.spaceship.draw()
        self.screen.blit(self.model.spaceship.image, self.model.spaceship.rect)
        pygame.display.update()


class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.rect = pygame.Rect(16, 16)
        self.image = pygame.image.load("/home/qetu0/python test files/spaceship.png")
        self.rect = self.image.get_rect()

        #Spaceship = pygame.sprite.RenderPlain()
        #Spaceship.update()
        #Spaceship.draw()

    #def draw(self):
        #return #pygame.sprite.RenderPlain()
        #self.screen.blit(self.image, self.rect)

if __name__=='__main__':
    pygame.init()
    size = (640, 480)
    model = Model(size)
    view = WindowView(model, size)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        view.draw()
        time.sleep(.01)
pygame.quit()
