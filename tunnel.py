import sys
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640,480))

run = True

while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			print "quit"
			run = False

	pygame.display.flip