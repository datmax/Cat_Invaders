"""
Nyan invaders!A simple space shooter game with python and pygame.
Created by: Max Datsun 
Github: https://github.com/datmax

TODO:
	add starting screen
	add score
	add death screen
	add lives and damage to shoots(and maybe even different shoots or ships?)
	add new levels(well,it's too early for this)
"""




import pygame
import time
import random


pygame.init()
								


clock = pygame.time.Clock()
display_width = 600
display_heigth = 800

enemy_img = pygame.image.load('enemy.png')
background = pygame.image.load('background.png')
cat_img = pygame.image.load('cat1.png')
cat_heigth = 23
cat_width = 52
laser = pygame.image.load('bullet.png')
laser_heigth = 30
enemy_width = 64
enemy_heigth = 64

game_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('Space Invaders')

def cat(x,y):
	game_display.blit(cat_img,(x,y))

def create_enemies(x,y,n,list):
	global enemies
	for i in xrange (7):
		list.append([x,y])
		x += n

def is_hit(bullet_list,enemy_list): #checks if the bullet hits the enemies.
	for bullet in bullet_list:
		for enemy in enemy_list:
			if bullet[1] < enemy[1] + enemy_heigth:
				if enemy[0] < bullet[0] < enemy[0] + enemy_width:
					bullet_list.remove(bullet)
					enemy_list.remove(enemy)
				



def invert_speed(speed): # when the enemy line touches a border of the screen,
	return -speed  		 #it changes direction.

def starting_screen():
	pass

def score():
	pass

def game_loop():
	enemies = []
	new_time = 0
	game_exit = False
	cat_x = display_width*0.5
	cat_y = display_heigth*0.8
	laser_speed = 10
	cat_position = []
	bullets = []	
	enemy_x = 10
	enemy_y = 10
	enemy_speed = 1
	create_enemies(enemy_x,enemy_y,80,enemies)
	change_x = 0
	while not game_exit:
		new_time = pygame.time.get_ticks()/1000

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 8
				if event.key == pygame.K_LEFT:
					change_x = -8
				
				if event.key == pygame.K_SPACE:
					bullets.append([cat_x + cat_width/2 ,cat_y])						
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					change_x = 0
				if event.key == pygame.K_RIGHT:
					change_x = 0			
				

		game_display.blit(background,(0,0))


		for b in range(len(bullets)):
			bullets[b][1]-= laser_speed	
		for bullet in bullets:
			if bullet[1]<0:
				bullets.remove(bullet)
		for bullet in bullets:
			game_display.blit(laser,(bullet[0], bullet[1]))		


		cat_x += change_x
		if cat_x >= display_width - cat_width:
			cat_x = display_width - cat_width 
		if cat_x <= 0:
			cat_x = 0

		cat(cat_x,cat_y)



		for enemy in enemies: #displays the enemies and move them left and right
			game_display.blit(enemy_img,(enemy[0],enemy[1]))
			if enemy[0] == 0 or enemy[0] == display_width - enemy_width:
				enemy_speed = invert_speed(enemy_speed)
				print enemies
			enemy[0] += enemy_speed

		is_hit(bullets,enemies)
		

		pygame.display.flip()


		clock.tick(60)

def exit():
	pygame.quit()
	quit()

game_loop()
