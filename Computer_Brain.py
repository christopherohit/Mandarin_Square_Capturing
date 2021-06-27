import pygame
import os
 
from CauHinh import *
from copy import deepcopy
from random import shuffle, choice, randint
# from BangGame import fill_if_empty, finished, play_turn
import time
import sys

LNavigation = pygame.image.load(os.path.join(RES, 'left.png'))
RNavigation = pygame.image.load(os.path.join(RES, 'right.png'))

class Computer_Brain:
    def __init__(self , player_id , algo = None, screen = None , table = None):
        self.INF = 70
        self.SLQUAN = SLQuan
        self.player_id = player_id
        self.algo = algo
        self.screen = screen
        self.table = table

    def Condition_Ending(self, state_, cur_point_): # Show Resutl that will be display you will win or Draw or lose
        state, player_point = deepcopy(state_), deepcopy(cur_point_)

        
        