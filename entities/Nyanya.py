import pygame
from .EnemyEntity import *
from config import *

class Nyanya(EnemyEntity):
    def __init__(self, name, idle_anims: list, roll_anims: list, attack_anims: list):
        super().__init__(name)
        self.idle_anims = idle_anims
        self.roll_anims = roll_anims
        self.attack_anims = attack_anims

        self.anims = [self.idle_anims, self.roll_anims, self.attack_anims]
        self.state = 0 # idle, roll, attack

        self.active_sprite_num = 0

        self.position = [SIZE[0] / 2, SIZE[1] / 2]

        self.damage = 50

    def set_next_sprite(self):
        a = self.anims[self.state]

        if self.active_sprite_num + 1 >= len(a):
            self.active_sprite_num = 0
        else:
            self.active_sprite_num += 1

        self.active_sprite = pygame.image.load(a[self.active_sprite_num])

    def tick(self):
        self.set_next_sprite()

        screen.blit(self.active_sprite, self.position)