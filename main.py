"""
Cat invaders!A simple space shooter game with python and pygame.
Created by: Max Datsun
Github: https://github.com/datmax

TODO:
	add lives and damage to shoots(and maybe even different shoots or ships?)
	add new levels(well,it's too early for this)
"""




import pygame
import time
import random
import pyganim
import os


pygame.init()



clock = pygame.time.Clock()
display_width = 600
display_heigth = 800


life_img = pygame.image.load(os.path.join('images','life.png'))
enemy_img = pygame.image.load(os.path.join('images', 'enemy.png'))
background = pygame.image.load(os.path.join('images','background.png'))
intro_background = pygame.image.load(os.path.join('images','intro.png'))
cat_img = pyganim.PygAnimation([(os.path.join('images','cat1.png'), 200),(os.path.join('images','cat2.png'), 200),
								(os.path.join('images','cat3.png'), 200),(os.path.join('images','cat4.png'), 200),
								(os.path.join('images','cat5.png'), 200)])

cat_death_animation = pyganim.PygAnimation([(os.path.join('images', 'catdie1.png'),300),
											(os.path.join('images', 'catdie2.png'),300),
											(os.path.join('images', 'catdie3.png'),300),
											(os.path.join('images', 'catdie4.png'),300)])
cat_death_animation.play()

cat_img.play()
cat_heigth = 23
cat_width = 52


laser = pygame.image.load(os.path.join('images','bullet.png'))
laser_heigth = 30
enemy_width = 64
enemy_heigth = 64
enemy_laser_img = pygame.image.load(os.path.join('images','enemy_shoot.png'))

game_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('Cat Invaders')





#COLORS          R   G   B
black =        (  0,  0,  0)
white =        (255,255,255)
red =          (200,  0,  0)
green =        (  0,200,  0)
bright_red =   (255,  0,  0)
bright_green = (  0,255,  0)
blue =         (  0,  0,150)

def cat(x, y):
	cat_img.blit(game_display, (x, y))

def create_enemies(x, y, n, list):
	global enemies
	for i in xrange (6):
		list.append([x, y])
		x += n


def is_hit(bullet_list, enemy_list): #checks if the bullet hits the enemies.
	for bullet in bullet_list:
		for enemy in enemy_list:
			if bullet[1] <= enemy[1] + enemy_heigth:
				if enemy[0] < bullet[0] < enemy[0] + enemy_width:
					bullet_list.remove(bullet)
					enemy_list.remove(enemy)
					return True

def is_player_hit(bullet_list, player):
	for bullet in bullet_list:
		if bullet[1] > player[1] - 20 and player[0] < bullet[0] < player[0] + cat_width:
			bullet_list.remove(bullet)
			return True


def invert_speed(speed): # when the enemy line touches a border of the screen,
	return -speed  	     #it changes direction.


def button(msg, x, y, w, h, ic, ac, action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] >y:
		pygame.draw.rect(game_display, ac, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(game_display, ic, (x, y, w, h))

	font = pygame.font.Font('Munro.ttf', 20)
	text = font.render(msg, True, white)
	game_display.blit(text,(x + w / 5, y + h / 3))


def display_score(count):
    font = pygame.font.Font('Munro.ttf', 24)
    text = font.render('Score: ' + str(count), True, white)
    game_display.blit(text,(0, display_heigth - 80))


def starting_screen():
	Intro = True
	while Intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		game_display.blit(intro_background,(0,0))
		font = pygame.font.Font('Munro.ttf', 115)
		text = font.render('Cat Invaders', True, white)
		game_display.blit(text,(0, display_heigth*0.3))

		button("Play",50,450,100,50,green,bright_green,game_loop)
		button("Quit",400,450,100,50,red,bright_red,exit_game)

		pygame.display.update()



def make_bullets(bullet_list, x, y):
	bullet_list.append([x + cat_width/2, y])


def display_lives(life):
	x=520
	for i in xrange(life):
		game_display.blit(life_img,(x,display_heigth - 80))
		x += 25

def death_screen(playerpos):
	death = True
	while death:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		game_display.blit(background, (0, 0))
		cat_death_animation.blit(game_display, (playerpos[0], playerpos[1]))
		font = pygame.font.Font('Munro.ttf', 100)
		text = font.render('Game Over :(', True, white)
		game_display.blit(text,(25 , display_heigth * 0.4))
		button("Try Again",50,450,100,50,green,bright_green,game_loop)
		button("Quit",400,450,100,50,red,bright_red,exit_game)
		pygame.display.update()



def game_loop():
	#when user press SPACE, turns to True and enemies shoot
	enemy_can_shoot = False 
	cooldown = 1000
	last = pygame.time.get_ticks()
	lives = 3
	score = 0
	enemy_bullets = []    #laser positions
	enemies = []		#for enemies positions
	game_exit = False
	cat_x = display_width*0.5
	cat_y = display_heigth*0.85
	bullet_speed = 10
	bullets = []	
	enemy_x = 10
	enemy_y = 10
	enemy_speed = 1
	enemy_bullet_speed = 15

	#useful when it will be more levels 
	create_enemies(enemy_x,enemy_y,90,enemies)
	bullet_x = random.randrange(0, len(enemies))


	change_x = 0

	#main loop
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 5
				if event.key == pygame.K_LEFT:
					change_x = -5
				
				if event.key == pygame.K_SPACE:
					make_bullets(bullets, cat_x, cat_y)
					enemy_can_shoot = True
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					change_x = 0
				if event.key == pygame.K_RIGHT:
					change_x = 0			
				



		game_display.blit(background,(0,0))

		if lives == 0:
			cat_img.blit(game_display, (-1,-1))
			death_screen([cat_x, cat_y])

		for b in range(len(bullets)):
			bullets[b][1]-= bullet_speed	
		for bullet in bullets:
			if bullet[1]<0:
				bullets.remove(bullet)
		for bullet in bullets:
			game_display.blit(laser,(bullet[0], bullet[1]))	

		if enemy_can_shoot:
			now = pygame.time.get_ticks()
			if now - last >= cooldown:
				last = pygame.time.get_ticks()
				bullet_x = random.randrange(0, len(enemies))
				enemy_bullets.append([enemies[bullet_x][0] + (enemy_width / 2), enemy_y])	

		for bullet in enemy_bullets:
			bullet[1] += enemy_bullet_speed
			game_display.blit(enemy_laser_img,(bullet[0], bullet[1]))

		cat_x += change_x
		if cat_x >= display_width - cat_width:
			cat_x = display_width - cat_width 
		if cat_x <= 0:
			cat_x = 0
		cat(cat_x,cat_y)

		for enemy in enemies: #displays the enemies and move them left and right
			game_display.blit(enemy_img,(enemy[0], enemy[1]))		
			if enemy[0] == 0 or enemy[0] == display_width - enemy_width:
				enemy_speed = invert_speed(enemy_speed)
			enemy[0] += enemy_speed


		
		if is_hit(bullets, enemies): #checks if aliens are hit, then eventually 
			score += 1               #increase the score
		if score == 50:
			lives += 1
		display_lives(lives)
		display_score(score)

		if is_player_hit(enemy_bullets, [cat_x, cat_y]):
			lives -= 1


		

		pygame.display.flip()


		clock.tick(60)

def exit_game():
	pygame.quit()
	quit()

starting_screen()
