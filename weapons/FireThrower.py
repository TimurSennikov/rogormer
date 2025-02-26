from .BaseWeapon import *
from .Bullet import *

class FireThrower(FireArmWeapon):
    def __init__(self):
        super().__init__()

    def fire(self, x, y, dir):
        if self.ammo <= 0:
            return

        if self.last_fire > self.fire_rate:
            self.last_fire = 0

            b = Bullet([x, y], "sprite/fireball.png", 10, -1 if dir == 0 else 1, self.damage)
            bullets.append(b)
            self.ammo -= 1