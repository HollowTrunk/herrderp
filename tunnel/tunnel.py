import math
import pygame
import sys

from pygame.locals import *
from pygame.gfxdraw import *
from random import choice

BLACK = (0,0,0)
SPEED = 200000
START = (310,450)
WHITE = (255,255,255)
window_size = (640,480)

class Cursor(pygame.sprite.Sprite):

	size = (20,20)

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(WHITE)
		self.rect = pygame.Rect(START, self.size)

	def move_left(self):
		if self.rect[0] != 0:
			self.rect = self.rect.move(-10,0)

	def move_right(self):
		if self.rect[0] != 620:
			self.rect = self.rect.move(10,0)

class Chunk(pygame.sprite.Sprite):

	def __init__(self, position, size):
		self.position = position
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(BLACK)
		self.rect = pygame.Rect(position, self.size)

	def  update(self, position, size):
		self.position = position
		self.size = size

		self.image = pygame.Surface(self.size)
		self.image.fill(BLACK)
		self.rect = pygame.Rect(position, self.size)

class Road(pygame.sprite.Group):

	size = (320,20)
	position = (160,0)

	chunk_list = []

	def __init__(self):
		pygame.sprite.Group.__init__(self)

	def calc_size(self, input):
		result = (int((300/math.exp(input/5000.0))+20), 20)
		return result

	def calc_position(self, input):
		pos_seq = [-20,-10,-5, 5, 10, 20]

		if (input[0]+self.size[0]+5) >= window_size[0]:
			result = ((input[0]-20),0)

		elif (input[0]-5) <= 0:
			result = ((input[0]+20),0)

		else:
			result = ((input[0]+choice(pos_seq)),0)

		return result

	def defill(self, score):
		self.size = self.calc_size(score)
		self.position = self.calc_position(self.position)

		self.chunk_list.insert(0, Chunk(self.position, self.size))
		self.add(self.chunk_list[0])

		for i in range(len(self.chunk_list)):
			position = (self.chunk_list[i].position[0], 20 * i)
			self.chunk_list[i].update(position, self.chunk_list[i].size)

			if i >= 24:
				self.remove(self.chunk_list[i])
				self.chunk_list.pop(i)


	def collide(self, cursor):
		collide_list = []

		collide_list = pygame.sprite.spritecollide(cursor, self, False, pygame.sprite.collide_rect_ratio(0.9))
		if not collide_list:
			return False
		else:
			return True

def display_score(score, window):
	font = pygame.font.Font(None, 50)
	text = font.render(str(score), 1, BLACK)
	textpos = text.get_rect()
	window.blit(text, textpos)

def main():
	pygame.init()
	pygame.key.set_repeat(1,0)

	score = 0

	window = pygame.display.set_mode(window_size)
	cursor = Cursor()
	road = Road()

	

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				run = False

			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					cursor.move_left()

				if event.key == K_RIGHT:
					cursor.move_right()

		for i in range(SPEED):
			if i == 0:
				road.defill(score)



		window.fill(WHITE)
		road.draw(window)
		window.blit(cursor.image, cursor.rect)
		
		display_score(score, window)

		score += 1

		#road.collide(cursor)

		pygame.display.flip()

main()
