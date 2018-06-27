#! /usr/bin/env python2.7
import time
import pygame
 
'''''
This class operates with crashes. Sets what will happen if player crashes.
'''''

class Crash():
	def __init__(self,x = 600,y = 400,x_change = 0 ,d_width = 800,d_height = 600,red = (255,0,0),Display = None):
		self.x = x
		self.y = y
		self.x_change = x_change
		self.d_width = d_width
		self.d_height = d_height
		self.red = red
		self.Display = pygame.display.set_mode((self.d_width,self.d_height))
		

	def x_changes(self):
		self.x = self.x + self.x_change

	def crash(self):
		self.message_print('CRASH!')

	def text_objects(self,text, font):
		T_surface = font.render(text,True,self.red)
		return T_surface,T_surface.get_rect()

	def message_print(self,text):
		Maintext = pygame.font.Font('freesansbold.ttf',100)
		T_surface,T_frame = self.text_objects(text,Maintext)
		T_frame.center = ((self.d_width/2),(self.d_height/2))
		self.Display.blit(T_surface,T_frame)
	
		pygame.display.update()
		time.sleep(3)

