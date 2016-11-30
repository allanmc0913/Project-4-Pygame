#Referenced from Snake tutorial I followed (https://pythonspot.com/en/snake-with-pygame/)
#It had a very step-by-step instruction where I learned the logic behind each different class and function
#I also used the PyGame documentation to look up PyGame functions.  
#While learning from the tutorial, I also downloaded the Github repository of another person's Snake code (https://github.com/ternus/pygame-examples/blob/master/snake.py)
#Often times, I found that the Github version did things differently, so the following code is a blend of my own logic from both the tutorial and the Github version
#On top of the base Snake game, I added in music/sound effects, an enemy snake class that inherits from an existing class, a 15 second timer that forces the user to eat an item
import pygame
import sys
import time
from random import randint

from pygame.locals import *
#initialize all pygame modules
pygame.init()
#referenced (https://www.youtube.com/watch?v=8sCQQlqeOKY) for help with sounds/music
pygame.mixer.music.load("sail.wav")
eat_sound = pygame.mixer.Sound("eating.wav")
hiss_sound = pygame.mixer.Sound("snakehiss.wav")



class Snake:
	FPS = 44
	#x and y positions are lists because each element is part of the snake.  Initialize list with starting coordinates of snake
	x = [150]
	y = [150]
	direction = 0
	length = 0
	
	def __init__(self, length):
		self.length = length
		for i in range(0, 2000):
			self.x.append(-1500)
			self.y.append(-1500)

	#update method updates snake's position
	def update(self):
		#update positions of snake's body
		for i in range(self.length - 1, 0, -1):
			self.x[i] = self.x[i-1]				
			self.y[i] = self.y[i-1]

		#update the snake's head position
		if self.direction == 0:
			self.x[0] = self.x[0] + self.FPS
		if self.direction == 1:
			self.x[0] = self.x[0] - self.FPS
		if self.direction == 2:
			self.y[0] = self.y[0] - self.FPS
		if self.direction == 3:
			self.y[0] = self.y[0] + self.FPS

		# if self.x[0] < -1 and self.x[0] > 801 and self.y[0] < -1 and self.y[0] > 601:
		# 	print ("Bye")
		# 	exit(0)

	
		
	def goright(self):
		self.direction = 0
	def goleft(self):
		self.direction = 1
	def goup(self):
		self.direction = 2
	def godown(self):
		self.direction = 3

	#draw takes in image.  it is then blitted/copied to another location
	def draw(self, screen, image):
		for i in range(0, self.length):
			screen.blit(image, (self.x[i], self.y[i]))
class Rat:
	x = 0
	y = 0
	FPS = 35

	#rat class initializer
	def __init__(self, x, y):
		self.x = x * self.FPS
		self.y = y * self.FPS

	#draw function takes in an image, then blits/copies it to another location
	def draw (self, screen, image):
		screen.blit(image, (self.x, self.y))

#this enemy snake class inherits from the Rat class.  Satisfies project requirement of class inheritance.
class EnemySnake(Rat):
	x = 0
	y = 0
	FPS = 35

	def __init__(self, x, y):
		self.x = x * self.FPS
		self.y = y * self.FPS

#collision detection class.  I could have used Sprites but I chose to use coordinate matching to detect collisions.  
class Collision:
	def collide(self,x1,y1,x2,y2,blocksize):
		if x1 >= x2:
			if x1 <= x2 + blocksize:
				if y1 >= y2:
					if y1 <= y2 + blocksize:
						return True

		return False

class Game:
	#song loops infinitely
	pygame.mixer.music.play(-1)
	rat = 0
	snake = 0
	enemysnake = 0
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600

	#class has default constructor or initializer
	#initialize new variables
	def __init__(self):
		self.running = True
		self.screen = None
		self.snakeimage = None
		self.ratimage = None
		self.enemysnakeimage = None
		self.backgroundimage = None
		self.collision = Collision()
		self.collided = False
		#tutorial had a set value like Rat(5,5).  This is not ideal because the starting spot for the rat will be the same every time
		#using randit generates random locations for the starting rat, enemy snake, and snake.
		self.rat = Rat((randint(1,15)), (randint(1,15)))
		self.snake = Snake(1)
		self.enemysnake = EnemySnake((randint(1,10)), (randint(1,10)))

	#display function sets all the display elements (images, background, text)
	def display(self, counter):
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		pygame.display.set_caption('Snake')
		self.running = True
		self.snakeimage = pygame.image.load("snakeblock.bmp").convert()
		self.ratimage = pygame.image.load("rat.bmp").convert()
		self.enemysnakeimage = pygame.image.load("enemysnake.bmp").convert()
		self.backgroundimage = pygame.image.load("grassbackground.bmp").convert()
		self.screen.blit(self.backgroundimage, (0,0))
	
		self.snake.draw(self.screen, self.snakeimage)
		self.rat.draw(self.screen, self.ratimage)
		self.enemysnake.draw(self.screen, self.enemysnakeimage)
		#the in-class handout suggested using pygame.display.update() but apparently it only updates a section of the display
		#using pygame.display.flip() updates the entire display
		
		font = pygame.font.SysFont("mspgothic", 20)
		displaylength = str(self.snake.length)
		output_string = "Length: " + displaylength
		text = font.render(output_string, True, (255, 255, 255))
		self.screen.blit(text, [700,3])
		#pygame.display.update()

		frame_count = counter
		frame_rate = 2
		start_time = 20
		clock = pygame.time.Clock()
		
		#print(frame_count)
		total_seconds = start_time - (frame_count // frame_rate)
		if total_seconds < 0:
			total_seconds = 0
		minutes = total_seconds // 60
		seconds = total_seconds % 60
		#print(minutes, seconds)
		output_string = "Time Left: {0:02}:{1:02}".format(minutes,seconds)
		text = font.render(output_string, True, (255, 255, 255))
		self.screen.blit(text, [250,0])
		clock.tick(10)
		pygame.display.update()

	#new positions of snake head and snake elements are updated.  Check for collisions
	def snakepartsupdate(self):
		self.snake.update()

		#checks if snake collides with rat.  If so, randomize new location of rat and enemy snake.  Also increase the length of the snake.
		for i in range(0, self.snake.length):
			if self.collision.collide(self.rat.x, self.rat.y, self.snake.x[i], self.snake.y[i], 44):
				print ("You ran into a rat and ate it!")
				self.rat.x = randint(2, 500)
				self.rat.y = randint(2, 500) 
				self.enemysnake.x = randint(2,500)
				self.enemysnake.y = randint(2,500)
				self.snake.length = self.snake.length + 1
				#in the case the random generation of snake and rat locations are the same, randomize their locations again
				if self.enemysnake.x == self.rat.x:
					self.rat.x = randint(2,500)
					self.enemysnake.x = randint(2,500)
				if self.enemysnake.y == self.rat.y:
					self.rat.y = randint(2,500)
					self.enemysnake.y = randint(2,500)
				
				#during collision, play slurping sound
				pygame.mixer.Sound.play(eat_sound)
				self.collided = True
			
			#check to see if snake collides with enemy snake.  If so, randomize new location of enemy snake and decrease length of snake
			elif self.collision.collide(self.enemysnake.x, self.enemysnake.y, self.snake.x[i], self.snake.y[i], 44):
				print ("You ran into an enemy snake! It attacked you!")
				self.enemysnake.x = randint(2,500)
				self.enemysnake.y = randint(2,500)
				self.snake.length = self.snake.length - 1
				#in the case the random generation of snake and rat locations are the same, randomize their locations again
				if self.enemysnake.x == self.rat.x:
					self.rat.x = randint(2,500)
					self.enemysnake.x = randint(2,500)
				if self.enemysnake.y == self.rat.y:
					self.rat.y = randint(2,500)
					self.enemysnake.y = randint(2,500)
				#if the snake length is 0, print message, play sound, end game.
				if self.snake.length == 0:
					pygame.mixer.Sound.play(hiss_sound)
					print ("Enemy snakes have attacked you! You have no life left")
					pygame.mixer.music.stop()
					exit(0)
		
		#checks to see if snake has collided with itself.  If so, stop music, stop game, and print message.
		for i in range(2, self.snake.length):
			if self.collision.collide(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i], 40):
				print ("You lost! You collided with yourself!")
				pygame.mixer.music.stop()
				exit(0)


		# for j in range(0, 801):
		# 	for k in range(0, 601):
				
		# 			pygame.mixer.music.stop()
		# 			print("You ran out of bounds!")
		# 			exit(0)


	def oncommand(self):

		counter = 0
	
		if self.display(counter) == False:
			self.running = False
		
		#the tutorial had a different way of event handling for keyboard inputs.  The tutorial code had the "if event.type == QUIT" section as a Snake class function
		#creating another class function for it was unnecessary, so I added it under the for loop.
		#the tutorial created a list of keyboard inputs using "pygame.event.pump()"
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
						pygame.mixer.music.stop()
						exit(0)
					#if event.key == K_TAB:

			self.snakepartsupdate()
			self.display(counter)
			counter += 1
			#delay the snake
			time.sleep(0.25);
			pygame.display.flip()
		pygame.quit()
		
if __name__ == '__main__':
	Game = Game()
	Game.oncommand()



