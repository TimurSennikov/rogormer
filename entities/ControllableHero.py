import pygame

from config import *
from .Entity import *

from weapons import *

class ControllableHero(Entity):
    def __init__(self, sprite: list, attacksprite: str, blinkinterval=10, blinktimes=10):
        Entity.__init__(self, "player")

        self.sprites = []
        for i in sprite:
            self.sprites.append(pygame.image.load(i))

        self.active_sprite_num = 0
        self.active_sprite = self.sprites[self.active_sprite_num]

        self.last_key = None
        self.sprite_inverted = False

        self.position = [50, 50]

        self.impulse = 0
        self.injump = False

        self.def_blinktimes = blinktimes

        self.blinktimes = 0
        self.lastblink = 0
        self.inblink = False
        self.blinkinterval = blinkinterval

        self.health = 100

        self.attack_sprite = pygame.image.load(attacksprite)
        self.attacking = False
        self.since_attack = 0

        self.current_weapon = FireThrower()

        self.font = pygame.font.Font(None, 64) # каждый раз открывать шрифт страшно затратно

    def revive(self):
        for entity in entities:
            if entity.get_name() == "vitachamber":
                self.health = 100
                p = entity.get_position()
                self.position[0] = p[0]
                self.position[1] = p[1]

                return True

        return False

    def show_text(self, t):
        text = self.font.render(t, True, (0, 255, 0), (0, 0, 128))
        textrect = text.get_rect()
        textrect.center = (SIZE[0] / 2, SIZE[1] / 2)
        screen.blit(text, textrect)

    def handle_keys(self, keys: pygame.key.ScancodeWrapper):
        if self.health <= 0:
            if keys[pygame.K_KP_ENTER]:
                if not self.revive():
                    self.show_text("NO VITA-CHAMBER FOUND!")
            return

        mspeed = 5 * 3 if self.injump else 5
        self.last_key = keys

        if keys[pygame.K_LEFT]:
            if self.position[0] - mspeed > 0:
                self.position[0] = self.position[0] - mspeed

            self.direction = False

        if keys[pygame.K_RIGHT]:
            if self.position[0] + mspeed < SIZE[0] - self.active_sprite.get_size()[0]:
                self.position[0] = self.position[0] + mspeed

            self.direction = True

        if keys[pygame.K_UP]:
            if not self.injump:
                self.impulse -= 30
                self.injump = True

        if keys[pygame.K_f]:
            if not self.attacking and self.since_attack > 60:
                self.since_attack = 0
                self.attacking = True

        if keys[pygame.K_r]:
            self.current_weapon.fire(self.position[0] + 15, self.position[1] + 120, self.sprite_inverted)

    def draw(self):
        if self.health > 0:
            text = self.font.render(str(self.health) + " HP " + str(self.current_weapon.ammo) + " / " + str(self.current_weapon.max_ammo) + " патр.", True, (0, 255, 0), (0, 0, 128))

            screen.blit(self.active_sprite, self.position)
            screen.blit(text, (10, 10))
        else:
            self.show_text("Возродиться в ближайшей вита-камере: Enter")

    def die(self):
        pass

    def is_on_obstacle(self):
        w = self.active_sprite.get_width()
        h = self.active_sprite.get_height()

        for i in obstacles:
            if self.position[0] + (w / 2) > i.position[0] and self.position[0] + (w / 2) < i.position[0] + 100 and self.position[1] + (h / 2 + 100) >= i.position[1] and self.position[1] + (h / 2 + 100) <= i.position[1] + 100:
                return True
        return False

    def check_collisions(self):
        for entity in entities:
            if entity.get_name() == "player":
                continue

            epos = entity.get_position()
            if not self.attacking:
                if self.position[0] - epos[0] < self.active_sprite.get_width() and self.position[0] - epos[0] > -self.active_sprite.get_width() and self.position[1] - epos[1] < self.active_sprite.get_height() and self.position[1] - epos[1] > -self.active_sprite.get_height():
                    if entity.get_name() == "enemy":
                        if self.blinktimes == 0 and self.health > 0:
                            self.blinktimes = self.def_blinktimes
                            self.health -= entity.damage
                            if self.health <= 0:
                                self.die()
            else:
                if self.position[0] - epos[0] < self.active_sprite.get_width() and self.position[0] - epos[0] > -self.active_sprite.get_width() and self.position[1] - epos[1] < self.active_sprite.get_height() and self.position[1] - epos[1] > -self.active_sprite.get_height():
                    entity.health -= 1

    def next_sprite(self):
        if self.active_sprite_num + 1 < len(self.sprites):
            self.active_sprite_num += 1
            self.active_sprite = self.sprites[self.active_sprite_num]
        else:
            self.active_sprite_num = 0
            self.active_sprite = self.sprites[self.active_sprite_num]

        if self.sprite_inverted:
            self.active_sprite = pygame.transform.flip(self.active_sprite, True, False)

    def tick(self):
        self.current_weapon.tick()

        self.check_collisions()

        if self.last_key[pygame.K_RIGHT] or self.last_key[pygame.K_LEFT]:
            self.next_sprite()

        if self.last_key[pygame.K_RIGHT] and not self.sprite_inverted:
            self.active_sprite = pygame.transform.flip(self.active_sprite, True, False)
            self.sprite_inverted = True
        elif self.last_key[pygame.K_LEFT] and self.sprite_inverted:
            self.active_sprite = pygame.transform.flip(self.active_sprite, True, False)
            self.sprite_inverted = False

        if (self.position[1] < SIZE[1] - self.active_sprite.get_size()[1] and not self.is_on_obstacle()):
            self.impulse += 1
        else:
            if not self.injump:
                self.impulse = 0

        self.position[1] += self.impulse

        if self.impulse >= 0 and (self.position[1] >= SIZE[1] - self.active_sprite.get_height() or self.is_on_obstacle()):
            self.injump = False

        self.lastblink += 1
        self.since_attack += 1

        if self.attacking:
            self.active_sprite = self.attack_sprite
            if self.sprite_inverted:
                self.active_sprite = pygame.transform.flip(self.active_sprite, True, False)

            if self.since_attack > 30:
                self.attacking = False
                self.since_attack = 0
        elif self.since_attack == 1:
            self.next_sprite()

        if not self.inblink:
            self.draw()

            if self.lastblink > self.blinkinterval and self.blinktimes > 0:
                self.inblink = True
                self.lastblink = 0
        else:
            if self.lastblink > self.blinkinterval:
                self.inblink = False
                self.lastblink = 0
                self.blinktimes -= 1