#! /usr/bin/env python2.7
import pygame

class Level():
	def __init__(self, count = 0, font = None,text = None,Display = None, black = (0,0,0)):
		self.count = count
		self.font = font
		self.text = text
		self.Display = pygame.display.set_mode((800,600))
		self.black = black

	def level(self):
		self.font = pygame.font.SysFont('freesansbold.ttf',30)
		self.text = self.font.render('Speed: '+ str(self.count), True, self.black)
		self.Display.blit(self.text,(0,0))
	def add(self):
		self.count += 1
	def start_count(self):
		self.count = 0
