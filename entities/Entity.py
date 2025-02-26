class Entity:
    def __init__(self, name):
        self.name = name
        self.position = None
        self.todestroy = False

        self.active_sprite = None

        self.health = 100

    def final_words(self):
        pass # вызывается при уничтожении
    def draw(self):
        pass
    def tick(self):
        pass
    def get_name(self):
        return self.name
    def get_position(self):
        return self.position
    def get_todestroy(self):
        return self.todestroy
    def destroy(self):
        self.todestroy = True