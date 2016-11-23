#referenced from Snake tutorial I followed (https://pythonspot.com/en/snake-with-pygame/).  It gave
import pygame
import sys
import time
import random

from pygame.locals import *

class Snake:
	FPS = 5
	x_pos = 10
	y_pos = 10

	#member function to go right.  later game class will invoke this functions through event handling.
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

pygame.event.pump()
keys = pygame.key.get_pressed() 
 



