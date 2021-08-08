import pygame
from pygame.locals import *

pygame.init()

def draw_text(display, loc, size, color, text):
    surf = pygame.Surface((display.get_size()[0] / size, display.get_size()[1] / size))

    size_max = display.get_size()[0] / size
    cx = 0
    cy = 0
    for x in text:

        if size_max - cx < 12:
            cy += 6
            cx = 0

        if x.lower() == "a":
            
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "b":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
        
        elif x.lower() == "c":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "d":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
        
        elif x.lower() == "e":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "f":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
        
        elif x.lower() == "g":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "h":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
        
        elif x.lower() == "i":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "j":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
        
        elif x.lower() == "k":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
        
        elif x.lower() == "l":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
        
        elif x.lower() == "m":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "n":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "o":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "p":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
        
        elif x.lower() == "q":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 3 + cy), color)
        
        elif x.lower() == "r":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((3 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "s":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
        
        elif x.lower() == "t":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
        
        elif x.lower() == "u":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "v":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 3 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 3 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
        
        elif x.lower() == "w":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 1 + cy), color)
            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((0 + cx, 3 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 2 + cy), color)
            surf.set_at((4 + cx, 3 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "x":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 3 + cy), color)
            surf.set_at((1 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 3 + cy), color)
            surf.set_at((3 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
        
        elif x.lower() == "y":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 1 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 3 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
        
        elif x.lower() == "z":

            surf.set_at((0 + cx, 0 + cy), color)
            surf.set_at((0 + cx, 4 + cy), color)
            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((1 + cx, 4 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 4 + cy), color)
            surf.set_at((4 + cx, 0 + cy), color)
            surf.set_at((4 + cx, 4 + cy), color)
            surf.set_at((3 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 3 + cy), color)
        
        elif x == "-":

            surf.set_at((0 + cx, 2 + cy), color)
            surf.set_at((1 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((3 + cx, 2 + cy), color)
        
        elif x == ".":

            surf.set_at((1 + cx, 4 + cy), color)
        
        elif x == "?":

            surf.set_at((1 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((3 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
        
        elif x == "!":

            surf.set_at((2 + cx, 0 + cy), color)
            surf.set_at((2 + cx, 1 + cy), color)
            surf.set_at((2 + cx, 2 + cy), color)
            surf.set_at((2 + cx, 4 + cy), color)
        
        elif x == "/":
            cx = -6
            cy += 6
            

            
        if x != " ":
            cx += 6
        else:
            cx += 3
        
        display.blit(pygame.transform.scale(surf, display.get_size()), loc)