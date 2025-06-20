import pygame
import random
import sys
pygame.init()

Width, Height = 500, 600
win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Dodge the box")

clock = pygame.time.clock()

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)