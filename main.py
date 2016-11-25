#referenced from Snake tutorial I followed (https://pythonspot.com/en/snake-with-pygame/).  It gave me 
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

	def godown(self):
		self.y_pos = self.y_pos + self.FPS

	def goup(self):
		self.y_pos = self.y_pos - self.FPS
class Game:
	SCREEN_WIDTH = 640
	SCREEN_HEIGHT = 480
	snake = 0

	#class has default constructor or initializer
	def __init__(self):
		self.running = True
		self.screen = None
		self.imgsurf = None
		self.snake = Snake()

	def display(self):
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

		#the tutorial had a different way of event handling for keyboard. It had another class function which was unnecessary.  
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

if __name__ == '__main__':
	Game = Game()
	Game.oncommand()



