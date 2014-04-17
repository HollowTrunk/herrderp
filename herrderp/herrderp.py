import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(1,1)

s = pygame.mixer.Sound("bruit.wav")

w = pygame.display.set_mode((640,480))

bg = pygame.image.load("background.jpg").convert()
c = pygame.image.load("perso.png").convert_alpha()

bg_rect = bg.get_rect();
c_rect = c.get_rect()

click = 0

end = 0
while end == 0:
	for event in pygame.event.get():
		if event.type == QUIT:
			end =1

		if event.type == KEYDOWN:
			s.play()
			if event.key == K_LEFT:
				c_nrect = c_rect.move(-1,0)
				if c_nrect[0] >= bg_rect[0]:
					c_rect = c_nrect
			elif event.key == K_RIGHT:
				c_nrect = c_rect.move(1,0)
				if c_nrect[0]+100 < bg_rect[2]:
					c_rect = c_nrect
			elif event.key == K_UP:
				c_nrect = c_rect.move(0,-1)
				if c_nrect[1] >= bg_rect[1]:
					c_rect = c_nrect
			elif event.key == K_DOWN:
				c_nrect = c_rect.move(0,1)
				if c_nrect[1]+100 < bg_rect[3]:
					c_rect = c_nrect

		if event.type == KEYUP:
			s.stop()

		if event.type == MOUSEBUTTONDOWN:
			if event.button == 3:
				click = event.pos
	
	if click != 0:
		s.play()
		if c_rect[0]+50 < click[0]:
			c_rect[0] = c_rect[0] + 1
		if c_rect[1]+50 < click[1]:
			c_rect[1] = c_rect[1] + 1
		if c_rect[0]+50 > click[0]:
			c_rect[0] = c_rect[0] - 1
		if c_rect[1]+50 > click[1]:
			c_rect[1] = c_rect[1] - 1
		
		if c_rect[0]+50 == click[0] and c_rect[1]+50 == click[1]:
			s.stop()
			click = 0

	w.blit(bg,(0,0))
	w.blit(c,c_rect)

	pygame.display.flip()
