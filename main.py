import pygame
import time


pygame.init()

new_shoot = False
shoot = False
position = 0											##for laser shoot.

clock = pygame.time.Clock()
display_width = 600
display_heigth = 800

background = pygame.image.load('background.png')
cat_img = pygame.image.load('cat1.png')
cat_heigth = 23
laser = pygame.image.load('fire1.png')

game_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('Space Invaders')

def cat(x,y):
	game_display.blit(cat_img,(x,y))

def laser_shoot(x,y,speed):
	if shoot == True:
		game_display.blit(laser,(x,y))
		y -= speed
		if y == 0:
			y = display_heigth*0.79 - cat_heigth



def getpos(pos):
	global position
	if position == 0:
		position = pos 
	else:
		return 

def starting_screen():
	pass

def score():
	pass

def game_loop():
	global position
	global shoot
	game_exit = False
	x = display_width*0.5
	y = display_heigth*0.8
	laser_speed = 10
	laser_y = display_heigth*0.79 - cat_heigth

	change_x = 0
	while not game_exit:
		for event in pygame.event.get():
			print event
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 5
				elif event.key == pygame.K_LEFT:
					change_x = -5
				if event.key == pygame.K_SPACE:
					shoot = True
					
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					change_x = 0
			



		x += change_x
		game_display.blit(background,(0,0))
		cat(x,y)


		getpos(x)
		laser_x = position
		laser_shoot(laser_x,laser_y,laser_speed)
					
		pygame.display.update()
		clock.tick(60)

def exit():
	pygame.quit()
	quit()

game_loop()