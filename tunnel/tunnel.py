import math
import pygame
import sys

from pygame.locals import *
from pygame.gfxdraw import *

BLACK = (0,0,0)
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
			self.rect = self.rect.move(-1,0)

	def move_right(self):
		if self.rect[0] != 620:
			self.rect = self.rect.move(1,0)

class Chunk(pygame.sprite.Sprite):

	def __init__(self, position, size):

		self.position = position
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(BLACK)
		self.rect = pygame.Rect(position, self.size)


class Road(pygame.sprite.Group):

	size = (320,20)
	position = (160,0)

	chunk_list = []

	def __init__(self):
		pygame.sprite.Group.__init__(self)
		for i in range(24):
			position = (160, (0 + 20*i))
			self.chunk_list.append(Chunk(position, self.size))
		self.add(self.chunk_list)

	def calc_size(self, input):
		result = (int(((320/(math.exp(input)/100000))+20)),20)
		return result

	def defill(self):
		self.size = self.calc_size(score)

		self.chunk_list.insert(0, Chunk(self.position, self.size))
		self.chunk_list.pop()

		for i in range(len(self.chunk_list)):l
			position = (160, (0 + 20*i))
			self.chunk_list[i].position = position

		self.empty()
		self.add(self.chunk_list)


	def collide(self, cursor):
		collide_list = []

		collide_list = pygame.sprite.spritecollide(cursor, self, False, pygame.sprite.collide_rect_ratio(0.9))
		if not collide_list:
			print "out"
		else:
			print "in"

def main():

	pygame.init()
	pygame.key.set_repeat(1,0)

	window = pygame.display.set_mode(window_size)
	cursor = Cursor()
	road = Road()

	print road.calc_size(0)

	score = 0

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

		#road.calc_size(score)

		window.fill(WHITE)
		road.draw(window)
		window.blit(cursor.image, cursor.rect)

		score += 1

		#road.collide(cursor)

		pygame.display.flip()

main()
