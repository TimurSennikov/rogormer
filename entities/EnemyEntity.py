from .Entity import *

class EnemyEntity(Entity):
    def __init__(self, name):
        super().__init__(name)

        self.speed = 1

        self.target = None
        self.target_locked = False

        self.actual_speed = self.speed

        self.health = 1000
        self.last_health = self.health

        self.in_pain = False
        self.last_pain = 0

        self.damage = 10