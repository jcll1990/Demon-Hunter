import pygame as pg
from collections import deque
from settings import *
import os
from player import *


class Weapon:
    def __init__(self, game):
        self.game = game
        self.key = 1
        self.path ='resources/sprites/weapon/shotgun/'
        self.scale = .1  # Adjust the scale to make the image smaller
        self.animation_time = 90
        self.images = []
        self.num_images = 0
        self.image = ""
        self.reloading = False
        self.animation_time_prev = pg.time.get_ticks()
        self.frame_counter = 0
        self.damage = 50
        self.get_images()
        

    def change_weapon(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_1]:
            self.key =1
            self.get_images()
            self.damage = 50
        if keys[pg.K_2]:
            self.key=2
            self.get_images()
            self.damage = 100

    def get_images(self):

        if self.key == 1:
            path = 'resources/sprites/weapon/shotgun/'
        elif self.key == 2:
            path = 'resources/sprites/weapon/melee'

        images = deque()
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                img = pg.image.load(file_path).convert_alpha()
                images.append(img)

        self.path = path  # Update the self.path attribute with the selected path
        self.images = images
        self.num_images = len(images)
        self.image = images[0]

        return images


    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate()
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def update(self):
        self.check_animation_time()
        self.animate_shot() 
        self.change_weapon()

    def draw(self):
        
        self.game.screen.blit(self.image, (
            HALF_WIDTH - self.images[0].get_width()  // 2,
            HEIGHT - self.images[0].get_height() * self.scale  -500  # Adjust the vertical position (e.g., subtract 20 pixels)
        ))


    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True


