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
	SCREEN_WIDTH = 640
	SCREEN_HEIGHT = 480

	#class has default constructor or initializer
	def __init__(self):
		self.running = True
		self.screen = None
		self.imgsurf = None
		self.snake = Snake()

	def display(self):
		SCREEN_WIDTH = 640
		SCREEN_HEIGHT = 480
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.running = True
		imgsurf = pygame.image.load("Pygame_logo.bmp").convert()

	def render(self):
		self.surface.fill((0,0,0))
		self.surf.blit(self.imgsurf, (self.snake.x,self.snake.y))

	def oncommand(self):
		if self.display() == False:
			self.running = False
		while (self.running):
			pygame.event.pump()
			keys = pygame.key.get_pressed()
			if event.type == QUIT:
				self.running = False
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_UP:
					self.Snake.goup()
				if event.key == K_DOWN:
					self.Snake.godown()
				if event.key == K_RIGHT:
					self.Snake.goright()
				if event.key == K_LEFT:
					self.Snake.goleft()
				if event.key == K_ESCAPE:
					self.running = False
if __name__ == '__main__':
	game = Game()
	game.oncommand()








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

