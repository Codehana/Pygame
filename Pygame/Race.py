#! /usr/bin/env python2.7
import pygame
from Crash import Crash
from Level import Level
import time
import random
	
'''''
This file contains: diplay, picture and falling objects creating functions, game loop, driver of key pushing. -- whole nub of the game.
'''''

pygame.init()

d_width = 800
d_height = 600

black = (0,0,0)
white = (255,255,255)
c = (0,255,128)
red = (255,0,0)
python_width = 100
player = Crash()
speed = Level()

Display = pygame.display.set_mode((d_width,d_height))
snakeImg = pygame.image.load("index.jpg").convert()
snakeImg = pygame.transform.scale(snakeImg,(100,100))

pygame.display.set_caption("Race")
Time= pygame.time.Clock()

def avoid(avoidx,avoidy, avoid_width, avoid_height,c):
	pygame.draw.rect(Display,c,[avoidx,avoidy,avoid_width,avoid_height])

def snake(x,y):
		Display.blit(snakeImg,(x,y))

def game():
	x=300
	y=500 
	x_change=0	
	crashed = False
	avoid_start_x = random.randrange(0,d_width)
	avoid_start_y = -600
	avoid_speed = 3
	avoid_w = 75
	avoid_h = 75
	speed.start_count()

#driver
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or pygame.K_RIGHT:
					x_change = 0	
		
		x += x_change
		Display.fill(white)
		avoid(avoid_start_x,avoid_start_y,avoid_w,avoid_h,c)
		avoid(avoid_start_x,avoid_start_y,avoid_w,avoid_h,c)
		avoid_start_y += avoid_speed
		
		snake(x,y)
		speed.level()
#boundary crashing
		if x > d_width - python_width or x < 0:
			player.crash()
			game()

#falling object(square)
		if avoid_start_y > d_height:
			avoid_start_y = 0 - avoid_h
			avoid_start_x = random.randrange(0,d_width)
			speed.add()
			avoid_speed += 1
#falling object crashing
		if y < avoid_start_y + avoid_h:
			if x > avoid_start_x and x < avoid_start_x + avoid_w or x + python_width > avoid_start_x and x + python_width < avoid_start_x + python_width + avoid_w:
				player.crash()
				game()
		
		pygame.display.update()
		Time.tick(90)
game()
pygame.quit()
quit()
