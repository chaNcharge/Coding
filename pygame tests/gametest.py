import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=600
height=600
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation Test')
background=pygame.image.load('bg.jpg')

UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('down.jpg')
spritex=200
spritey=130
direction=None

dir_from_key = {
	K_LEFT: 'left',
	K_RIGHT: 'right',
	K_UP: 'up',
	K_DOWN: 'down'
}

while True:
	DISPLAYSURF.blit(background,(0,0))

	DISPLAYSURF.blit(sprite,(spritex,spritey))

	# Get all the events for this tick into a list
	events = list(pygame.event.get()) 

	quit_events = [e for e in events if e.type == QUIT]
	keydown_events = [e for e in events if e.type == KEYDOWN 
																				 and e.key in dir_from_key]
	keyup_events = [e for e in events if e.type == KEYUP 
																			 and e.key in dir_from_key]

	# If there's no quit event, then the empty list acts like false
	if quit_events:
			pygame.quit()
			sys.exit()

	# Non-last key down events will be overridden anyway
	if keydown_events:
		direction = dir_from_key[keydown_events[-1].key]

	# Change location and image based on direction
	if direction == 'left':
		spritex-=5
		sprite=pygame.image.load('left.jpg')
	elif direction == 'right':
		spritex+=5
		sprite=pygame.image.load('right.jpg')
	elif direction == 'up':
		spritey-=5
		sprite=pygame.image.load('up.jpg')
	elif direction == 'down':
		spritey+=5
		sprite=pygame.image.load('down.jpg')

	# If there's a keyup event for the current direction.
	if [e for e in keyup_events if dir_from_key[e.key] == direction]:
		direction = None

	pygame.display.update()
	fpsClock.tick(FPS)