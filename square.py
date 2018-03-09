import pygame
from pygame.locals import *
import time
from random import randint


class Model:
    '''Holds the model of the game state'''

    def __init__(self, size):
        self.box = Box()

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

        pygame.draw.rect(self.screen, #draws screen, and a grey nerd
                         pygame.Color(50, 50, 50),
                         self.model.box.rect())

        pygame.display.update()


class Box:
    ''' The state of the nerd '''

    def __init__(self, x=50, y=50, width=50, height=100):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


    def rect(self):
        return pygame.Rect(self.x,
                           self.y,
                           self.width,
                           self.height)




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
