import pygame
import sys
import random
import numpy as np


# setting the window size variables
width, height = 650, 500
size = (width, height)

# initializing pygame window
pygame.init()
# setting name
pygame.display.set_caption('Game of Life')
# setting the screen up with the size
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 60

living = (255, 255, 255)
dead = (0, 0, 0)

class Grid:
    def __init__(self, width, height, scale, offset):
        # scaling for different sized grids
        self.scale = scale
        self.columns = int(height / scale)
        self.rows = int(width / scale)
        self.size = (self.rows, self.columns)
        # creating a multi-dimensional array with the size of rows x columns
        self.grid_array = np.ndarray(shape=(self.size))

# creating a method for the random button
    def random_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                # double nested loop to assign the points in our grid to 0 or 1(dead or alive)
                # possibility: have numbers above 0 be a random choice from a list of colors
                self.grid_array[x][y] = random.randint(0, 1)