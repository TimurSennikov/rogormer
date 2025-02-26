class FireArmWeapon:
    def __init__(self):
        self.name = "weapon"

        self.damage = 100 # дефолт

        self.bullet = None # текстурка пули для отрисовки
        self.bullet_speed = 10 # скорость пули (пикселей в секунду)

        self.last_fire = 0
        self.fire_rate = 5
        
        self.ammo = 30
        self.max_ammo = 30

    def fire(self, x, y, dir):
        pass

    def tick(self):
        self.last_fire += 1