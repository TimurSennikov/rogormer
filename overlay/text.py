from config import *

class TextOverlay:
    def __init__(self):
        self.font = pygame.font.Font(None, 64)
        self.text = ""

    def draw(self):
        t = self.font.render(self.text, True, (0, 255, 0), (0, 0, 128))
        trect = t.get_rect()
        trect.center = (SIZE[0] / 2, SIZE[1] / 4)
        screen.blit(t, trect)

    def set_text(self, text: str):
        self.text = text