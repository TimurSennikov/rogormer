import pygame
import pygame.locals

from entities import *
from config import *
from overlay import *

player = ControllableHero(["sprite/roman0.png", "sprite/roman1.png", "sprite/roman2.png"], "sprite/roman_attack.png")

entities.append(player)

class Game:
    def __init__(self, obstacle = "sprite/obstacle.png"):
        pygame.display.set_caption("Dont Mess With Roger")
        pygame.display.set_icon(pygame.image.load("sprite/roman0.png"))

        self.bg_image = pygame.image.load("bg/def_0.png")
        self.obstacle = pygame.image.load(obstacle)

        self.first_start_of_level = True
        self.storyteller = TextOverlay()

    def mainloop(self):
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()

        screen.fill((144, 238, 144))
        screen.blit(self.bg_image, (0, 0))

        self.draw_obstacles()

        keys = pygame.key.get_pressed()
        player.handle_keys(keys=keys)

        for i, entity in enumerate(entities):
            entity.tick()
            if entity.get_todestroy():
                entity.final_words()
                del entities[i]

        for i, b in enumerate(bullets):
            b.tick()
            if b.get_todestroy():
                del bullets[i]

        if self.first_start_of_level:
            for i in range(3, -1, -1):
                self.storyteller.set_text(str(i))
                self.storyteller.draw()
                pygame.time.delay(1000)

                pygame.display.update()

            self.first_start_of_level = False

        pygame.display.update()

        if self.get_enemy_count() == 0:
            self.storyteller = TextOverlay()
            self.storyteller.set_text("Уровень пройден!")
            self.storyteller.draw()

            pygame.display.update()
            pygame.time.delay(5000)

            return False
        return True

    def draw_obstacle(self, x: int, y: int):
        screen.blit(self.obstacle, (x, y))

    def draw_obstacles(self):
        for i in obstacles:
            self.draw_obstacle(i.position[0], i.position[1])

    def create_enemy(self, enemy):
        entities.append(enemy)

    def setup_level(self, enemy_count):
        for i in range(enemy_count):
            self.create_enemy(AIEnemy(["player"], ["sprite/enemy.png"], "sprite/enemy_pain.png"))

    def get_enemy_count(self):
        c = 0
        for i in entities:
            if i.get_name() == "enemy":
                c += 1

        return c

    def set_map(self, m: list):
        obstacles = m

    def show_story(self, phrases: list, backgrounds: list):
        storyteller = TextOverlay()

        story_remains = True
        i = 0

        bg = pygame.image.load(backgrounds[i])
        phrase = phrases[i]

        storyteller.set_text(phrase)

        while story_remains:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()

            clock.tick(60)
            screen.blit(bg, (0, 0))
            storyteller.draw()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                i += 1
                if i >= len(phrases):
                    story_remains = False
                    break

                bg = pygame.image.load(backgrounds[i])
                phrase = phrases[i]

                storyteller.set_text(phrase)

                pygame.time.wait(100)

            pygame.display.update()