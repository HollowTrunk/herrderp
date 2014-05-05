import pygame
import sys
import tunnel_sprites

from pygame.locals import *

BLACK = (0,0,0)
SPEED = 200000
WAIT = 2000
WHITE = (255,255,255)
window_size = (640,480)

window = pygame.display.set_mode(window_size)

def display_level(road, cursor):
	window.fill(WHITE)
	road.draw(window)
	window.blit(cursor.image, cursor.rect)

def display_score(score):
	font = pygame.font.Font(None, 30)
	text = font.render(str(score), True, BLACK, WHITE)
	textpos = window.get_rect().topleft
	window.blit(text, textpos)

def display_info(msg):
	font = pygame.font.Font(None,50)

	if msg == 1:
		text = font.render("Start", True, BLACK, WHITE)
		textpos = window.get_rect().center
		window.blit(text, textpos)
	elif msg == 2:
		text = font.render("Pause", True, BLACK, WHITE)
		textpos = window.get_rect().center
		window.blit(text, textpos)
	elif msg == 3:
		text = font.render("GAME OVER", True, BLACK, WHITE)
		textpos = window.get_rect().center
		window.blit(text, textpos)

def init():
	pygame.init()
	pygame.event.set_allowed(None)
	pygame.event.set_allowed(pygame.KEYDOWN)
	pygame.event.set_allowed(QUIT)
	pygame.key.set_repeat(1,0)

def run():
	run = True
	score = 0

	cursor = tunnel_sprites.Cursor()
	road = tunnel_sprites.Road()

	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.quit()

			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					cursor.move_left()

				if event.key == K_RIGHT:
					cursor.move_right()

		for i in range(SPEED):
			if i == 0:
				road.defill(score)

		display_level(road, cursor)

		score += 1
		display_score(score)

		pygame.display.flip()

		if not road.collide(cursor):
			display_info(3)
			pygame.display.flip()
			run = False

def main():
	init()

	new_game = True
	while new_game:
		run()
		new_game = False

		pygame.time.wait(WAIT)
		
		event = pygame.event.wait()
		if event.type == QUIT:
			pygame.quit()
			sys.quit()
		if event.type == pygame.KEYDOWN:
			new_game = True

main()
