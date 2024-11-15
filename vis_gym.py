from mdp_gym import PacmanGameEnv
import sys
import time
import pygame
from constants import *

WIDTH, HEIGHT = SCREENWIDTH, SCREENHEIGHT

screen=None

game_ended = False
action_results = [None, None, None, None, None]

game = PacmanGameEnv()

def setup(GUI=TRUE):
    global screen
    if GUI:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pacman MDP Visualization")

# map room to grid cell positions
        
# draw grid
        
# draw ghosts at their positions
        

