import pygame

from config import *
from .Entity import *

class VitaChamber(Entity):
    def __init__(self, sprites: list, name: str):
        Entity.__init__(self, name)

        self.sprites = []
        for sprite in sprites:
            self.sprites.append(pygame.image.load(sprite))

        self.active_sprite_num = 0
        self.active_sprite = self.sprites[self.active_sprite_num]

        self.position = (1500, SIZE[1] - self.active_sprite.get_height())

    def draw(self):
        screen.blit(self.active_sprite, self.position)

    def tick(self):
        self.draw()

        self.active_sprite_num += 1
        if self.active_sprite_num + 1 >= len(self.sprites):
            self.active_sprite_num = 0

        self.active_sprite = self.sprites[self.active_sprite_num]