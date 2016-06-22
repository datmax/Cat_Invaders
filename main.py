"""
Nyan invaders!A simple space shooter game with python and pygame.
Created by: Max Datsun 
Github: https://github.com/datmax
"""

import pygame
import time


pygame.init()

shoot = False								#for laser shoot.It will be set to True when you hit space.

clock = pygame.time.Clock()
display_width = 600
display_heigth = 800

background = pygame.image.load('background.png')
cat_img = pygame.image.load('cat1.png')
cat_heigth = 23
laser = pygame.image.load('bullet.png')
laser_heigth = 30


game_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('Space Invaders')

def cat(x,y):
	game_display.blit(cat_img,(x,y))



def get_pos(list):
	return list[-1][0]



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
	cat_position = []
	bullets = [laser]


	change_x = 0
	while not game_exit:
		ms = clock.tick(60)
		print ms 
		for event in pygame.event.get():
			print event
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 8
				elif event.key == pygame.K_LEFT:
					change_x = -8
				if event.key == pygame.K_SPACE:
					shoot = True
					laser_x = get_pos(cat_position)		#if you press again space,the laser will jump :/

					
					
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					change_x += 8
				if event.key == pygame.K_RIGHT:
					change_x -=8			
				



		x += change_x
		game_display.blit(background,(0,0))
		cat(x,y)
		cat_position.append((x,y))

		
		if shoot == True:			
			game_display.blit(bullets[0],(laser_x,laser_y))
			laser_y -= laser_speed
			if laser_y < 0:
				shoot = False
				laser_y = display_heigth*0.79 - cat_heigth - laser_heigth
		#TODO:shoot more than 1 laser.



		
					
		pygame.display.update()
		clock.tick(60)

def exit():
	pygame.quit()
	quit()

game_loop()
