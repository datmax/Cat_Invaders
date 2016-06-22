"""
Nyan invaders!A simple space shooter game with python and pygame.
Created by: Max Datsun 
Github: https://github.com/datmax

TODO:
	add boundaries to the surface
	add enemies
	add starting screen
	add score
	add death screen
	add lives and damage to shoots(and maybe even different shoots or ships?)
	add new levels(well,it's too early for this)
"""




import pygame
import time


pygame.init()
								



clock = pygame.time.Clock()
display_width = 600
display_heigth = 800

#enemy_img = pygame.image.load('enemy.png')
background = pygame.image.load('background.png')
cat_img = pygame.image.load('cat1.png')
cat_heigth = 23
cat_width = 52
laser = pygame.image.load('bullet.png')
laser_heigth = 30


game_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('Space Invaders')

def cat(x,y):
	game_display.blit(cat_img,(x,y))




def starting_screen():
	pass

def score():
	pass

def game_loop():
	new_time = 0
	game_exit = False
	cat_x = display_width*0.5
	cat_y = display_heigth*0.8
	laser_speed = 10
	cat_position = []
	bullets = []	
	enemies = [[20,20],[50,23]]
	enemy_x = 10
	enemy_y = 10


	change_x = 0
	while not game_exit:
		new_time = pygame.time.get_ticks()/1000

		for event in pygame.event.get():
			print event
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 8
				if event.key == pygame.K_LEFT and cat_x > 5:
					change_x = -8
				if event.key == pygame.K_SPACE:
					bullets.append([cat_x + cat_width/2 ,cat_y])						
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					change_x = -1
				if event.key == pygame.K_RIGHT:
					change_x = +1			
				


		for b in range(len(bullets)):
			bullets[b][1]-= laser_speed	
		for bullet in bullets:
			if bullet[1]<0:
				bullets.remove(bullet)
		
		cat_x += change_x
		game_display.blit(background,(0,0))
		cat(cat_x,cat_y)
		for bullet in bullets:
			game_display.blit(laser,(bullet[0], bullet[1]))		


		
		

		pygame.display.flip()


		clock.tick(60)

def exit():
	pygame.quit()
	quit()

game_loop()
