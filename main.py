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
pygame.mixer.music.load("sail.wav")
class Snake:
    #how large each step is
	FPS = 20
	x_pos = list()
	y_pos = list()
	direction = 0
	length = 0
	updateCountMax = 3
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
	def draw(self, screen, image):
		for i in range(0, self.length):
			screen.blit(image, (self.x_pos[i], self.y_pos[i]))
class Enemy:
	x_pos = 0
	y_pos = 0
	FPS = 44
	def __init__(self, x_pos, y_pos):
		self.x_pos = x_pos * self.FPS
		self.y_pos = y_pos * self.FPS
	def draw (self, screen, image):
		screen.blit(image, (self.x_pos, self.y_pos))
	
class Game:
	pygame.mixer.music.play(-1)
	enemy = 0
	snake = 0
	SCREEN_WIDTH = 1080
	SCREEN_HEIGHT = 720

	#class has default constructor or initializer
	def __init__(self):
		self.running = True
		self.screen = None
		self.imgsurf = None
		self.enemysurf = None
		self.enemy = Enemy (5,5)
		self.snake = Snake(3)


	
	def display(self):
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		pygame.display.set_caption('Snake')
		self.running = True
		self.imgsurf = pygame.image.load("snakeblock.bmp").convert()
		self.enemysurf = pygame.image.load("enemy.bmp").convert()
	
		self.screen.fill((0,0,0))
		self.snake.draw(self.screen, self.imgsurf)
		self.enemy.draw(self.screen, self.enemysurf)
		#the in-class handout suggested using pygame.display.update() but apparently it only updates a section of the display
		#using pygame.display.flip() updates the entire display
		pygame.display.flip()


	def snakepartsupdate(self):
		self.snake.update()
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
			self.snakepartsupdate()
			self.display()
			#delay the snake
			time.sleep(0.05);
		
if __name__ == '__main__':
	Game = Game()
	Game.oncommand()




