from .Entity import *

class Obstacle(Entity):
    def __init__(self, x, y):
        self.name = "obstacle"

        self.position = [x, y]