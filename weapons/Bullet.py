from config import *

class Bullet:
    def __init__(self, pos, texture, speed, dir, damage):
        self.texture = pygame.image.load(texture)
        self.speed = speed * dir
        self.position = pos

        self.damage = damage

        self.to_destroy = False

    def draw(self):
        screen.blit(self.texture, self.position)

    def check_collisions(self):
        for i in entities:
            r = self.position
            e = i.get_position()

            w, h = self.texture.get_width(), self.texture.get_height()
            ew, eh = i.active_sprite.get_width(), i.active_sprite.get_height()

            if (r[0] >= e[0] and r[0] <= e[0] + ew and r[1] >= e[1] and r[1] <= e[1] + eh) and i.get_name() == "enemy":
                i.health -= self.damage
                self.to_destroy = True

    def tick(self):
        self.draw()
        self.check_collisions()

        self.position[0] += self.speed

        if self.position[0] > SIZE[0]:
            self.to_destroy = True

    def get_todestroy(self):
        return self.to_destroy