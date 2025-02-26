import pygame
import random

from entities import *

SIZE = (1920, 1080)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

game_running = True

entities = []
obstacles = []

bullets = [] # пули

for i in range(10):
        obstacles.append(Obstacle(random.randint(0, 192) * 10, i * 100))