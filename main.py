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
	x_pos = list()
	y_pos = list()
	direction = 0
	length = 3
	updateCountMax = 2
	updateCount = 0

	def __init__(self, length):
		self.length = length
		for i in range(0, length):
			self.x_pos.append(0)
			self.y_pos.append(0)
			#000
			#000

	def update(self):
		self.updateCount += 1
		if self.updateCount > self.updateCountMax:
			#update positions of snake parts that aren't the head
			#for i in 2, 1
			for i in range(self.length - 1, 0, -1):
				self.x_pos[i] = self.x_pos[i-1]
				self.y_pos[i] = self.y_pos[i-1]

			#update the snake's head position
			if self.direction == 0:
				self.x_pos[0] = self.x_pos[0] + self.FPS
			if self.direction == 1:
				self.x_pos[0] = self.x_pos[0] - self.FPS
			if self.direction == 2:
				self.y_pos[0] = self.y_pos[0] - self.FPS
			if self.direction == 3:
				self.y_pos[0] = self.y_pos[0] + self.FPS
			self.updateCount = 0

	def goright(self):
		self.direction = 0
	def goleft(self):
		self.direction = 1
	def goup(self):
		self.direction = 2
	def godown(self):
		self.direction = 3
	def draw(self, surf, img):
		for i in range(0, self.length):
			surface.blit(image, (self.x_pos[i], self.y_pos[i]))
class Game:
	snake = 0
	SCREEN_WIDTH = 720
	SCREEN_HEIGHT = 480

	#class has default constructor or initializer
	def __init__(self):
		self.running = True
		self.screen = None
		self.imgsurf = None
		self.snake = Snake(10)

	
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
			#delay the snake
			time.sleep(0.1);

if __name__ == '__main__':
	Game = Game()
	Game.oncommand()



