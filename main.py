#referenced from Snake tutorial I followed (https://pythonspot.com/en/snake-with-pygame/)
#It had a very step-by-step instruction where I learned the logic behind each different class and function
#I also used the PyGame documentation to look up PyGame functions.  
#While learning from the tutorial, I also downloaded the Github repository of another person's Snake code.  
#Often times, I found that the Github version did things differently, so the following code is a blend of my own logic from both the tutorial and the Github version

import pygame
import sys
import time
import random

from pygame.locals import *
#initialize all pygame modules
pygame.init()
class Snake:
	FPS = 32
	x_pos = 0
	y_pos = 0
	direction = 0

	def goright(self):
		self.direction = 0
		# if self.direction == 0:
		# 	self.x_pos = self.x_pos + self.FPS
	def goleft(self):
		self.direction = 1
		# if self.direction == 1:
	 # 		self.x_pos = self.x_pos - self.FPS
	def goup(self):
		self.direction = 2
		# if self.direction == 2:
		# 	self.y_pos = self.y_pos - self.FPS
	def godown(self):
		self.direction = 3
		# if self.direction == 3:
	 # 		self.y_pos = self.y_pos + self.FPS
	
	def update(self):
		if self.direction == 0:
			self.x_pos = self.x_pos + self.FPS
		if self.direction == 1:
			self.x_pos = self.x_pos - self.FPS
		if self.direction == 2:
			self.y_pos = self.y_pos - self.FPS
		if self.direction == 3:
			self.y_pos = self.y_pos + self.FPS
class Game:
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	snake = 0

	#class has default constructor or initializer
	def __init__(self):
		self.running = True
		self.screen = None
		self.imgsurf = None
		self.snake = Snake()

	
	def display(self):
		pygame.init()
		SCREEN_WIDTH = 720
		SCREEN_HEIGHT = 480
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		pygame.display.set_caption('Snake')
		self.running = True
		self.imgsurf = pygame.image.load("snakeblock.bmp").convert()

	def render(self):
		self.screen.fill((0,0,0))
		self.screen.blit(self.imgsurf, (self.snake.x_pos,self.snake.y_pos))
		pygame.display.flip()

	def oncommand(self):
		if self.display() == False:
			self.running = False

		#the tutorial had a different way of event handling for keyboard inputs.  The tutorial code had the "if event.type == QUIT" section as a Snake class function
		#creating another class function for it was unnecessary, so I added it under the for loop.
		#the tutorial created a list of keyboard inputs using "pygame.event.pump()" a
		#I used a more intuitive way listed in the pygame basics sheet handed out in class, using pygame.event.get(). 
		while (self.running):
			for event in pygame.event.get():
				if event.type == QUIT:
					self.running = False
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						self.snake.goup()
					if event.key == K_DOWN:
						self.snake.godown()
					if event.key == K_LEFT:
						self.snake.goleft()
					if event.key == K_RIGHT:
						self.snake.goright()
					if event.key == K_ESCAPE:
						self.running = False
			self.render()
			time.sleep(100.0/1000.0);

if __name__ == '__main__':
	Game = Game()
	Game.oncommand()



