#referenced from Snake tutorial I followed (https://pythonspot.com/en/snake-with-pygame/).  It gave
import pygame
import sys
import time
import random

from pygame.locals import *
#initialize all pygame modules
pygame.init()
class Snake:
	FPS = 5
	x_pos = 10
	y_pos = 10

	#member methods.  Must link methods to events
	def goright(self):
		self.x_pos = self.x_pos + self.FPS

	def goleft(self):
		self.x_pos = self.x_pos - self.FPS

	def goup(self):
		self.y_pos = self.y_pos + self.FPS

	def godown(self):
		self.y_pos = self.y_pos - self.FPS
class Game:
	SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

	#start events
	

	#class has default constructor or initializer
	def __init__(self):
		self._running = True
		self.screen = None
		self.imgsurf = None
		self.player = Player()

	def setdimensions(self):
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self._running = True
		imgsurf = pygame.image.load("Pygame_logo.bmp").convert()

	def oncommand(self):
		if event.type == QUIT:
			self._running = False
			pygame.quit()
			sys.exit()
		if self.setdimensions() == False:
			self._running = False
		while (self._running):
			pygame.event.pump()
	keys = pygame.key.get_pressed() 
 









	#for event in pygame.event.get():
     #       if event.type == QUIT:
      #          pygame.quit()
       #         sys.exit()
        #    elif event.type == KEYDOWN:
         #       if event.key == K_UP:
          #          self.player.goup()
           #     elif event.key == K_DOWN:
            #  		self.player.godown()
             #   elif event.key == K_LEFT:
              #      self.player.goleft()
               # elif event.key == K_RIGHT:
                #    self.player.goright()


#import pygame

#screen = pygame.display.set_mode((640,400))
#while True:
#pass

