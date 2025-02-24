import pygame
import random

from config import *
from .EnemyEntity import *

class AIEnemy(EnemyEntity):
    def __init__(self, enemy_list: list, sprite: list, pain: str, speed = 5):
        Entity.__init__(self, "enemy")

        self.sprites = []
        self.e_list = enemy_list

        for i in sprite:
            self.sprites.append(pygame.image.load(i))

        self.speed = speed

        self.active_sprite_num = 0
        self.active_sprite = self.sprites[self.active_sprite_num]

        self.position = [random.randint(0, SIZE[0] - self.active_sprite.get_width()), random.randint(0, 100)]
        self.target = None
        self.target_locked = False

        self.actual_speed = self.speed

        self.health = 1000
        self.last_health = self.health

        self.pain_sprite = pygame.image.load(pain)

        self.in_pain = False
        self.last_pain = 0

    def draw(self):
        screen.blit(self.active_sprite, self.position)

    def lock_target(self):
        for entity in entities:
            if entity.get_name() == "player":
                self.target = entity.get_position()
                return
        self.target = None

    def next_sprite(self):
        self.active_sprite_num += 1
        if self.active_sprite_num + 1 > len(self.sprites):
            self.active_sprite_num = 0
        self.active_sprite = self.sprites[self.active_sprite_num]

    def tick(self):
        self.lock_target()

        if self.target == None:
            self.target = (SIZE[0] / 2, SIZE[1] / 2)

        if self.position[1] < SIZE[1] - self.active_sprite.get_size()[1]:
            self.position[1] += random.randint(1, self.actual_speed)

        if self.position[0] - self.target[0] < SIZE[0] / 3:
            self.target_locked = True

        if self.target and self.target_locked:
            if self.position[0] - self.target[0] > SIZE[0] / 1.5:
                self.target_locked = False

            dir = -self.actual_speed if self.target[0] < self.position[0] else self.actual_speed
            self.position[0] += dir

            self.next_sprite()

        if self.in_pain and self.last_pain < 60:
            self.active_sprite = self.pain_sprite
        elif self.last_pain > 60:
            self.in_pain = False
            self.next_sprite()

        if not self.health == self.last_health:
            self.in_pain = True
            self.last_pain = 0

            self.last_health = self.health

            if self.health <= 0:
                self.destroy()

        self.last_pain += 1

        self.draw()