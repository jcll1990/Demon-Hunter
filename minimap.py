import pygame as pg
from map import *
from settings import *


class Minimap:
    def __init__(self, game):
        self.game = game
        self.minimap = self.game.map.world_map
        self.y_pos = 0

    def minimap_pos(self):
        max_y = max(key[1] for key in self.minimap.keys())
        a = HEIGHT - (max_y * 12) - 100
        self.y_pos = a
        return self.y_pos

    def draw(self):
        self.minimap_pos()  
        [pg.draw.rect(self.game.screen, 'white', (pos[0]*12, self.y_pos + pos[1]*12, 12, 12), 1)
        for pos in self.minimap]

    