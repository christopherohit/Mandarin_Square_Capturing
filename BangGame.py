from math import trunc
from CauHinh import *
import os
from copy import deepcopy
import pygame
from tkinter import * 
from tkinter import messagebox
import time


COLOR = color()

def text_to_screen(screen , text , x , y, fontsize ,color):
    try:
        pygame.font.init()
        myfont = pygame.font.Sys('Arial', fontsize)
        textsurface = myfont.render(text, True, color)
        screen.blit(textsurface, (x, y))

    except Exception as e:
        print ("Font Error !!!\nPlease recheck your font and ensure that it correct")
        raise e
    
def ipos(pos, inc = 1 ):
    ''''''
    