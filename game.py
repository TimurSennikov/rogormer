import pygame
import pygame.locals
import math

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

        if self.first_start_of_level:
            storyteller = TextOverlay()

            for i in range(3, -1, -1):
                storyteller.set_text(str(i))
                storyteller.draw()
                pygame.time.delay(1000)

                pygame.display.update()

            self.first_start_of_level = False

        pygame.display.update()

    def draw_obstacle(self, x: int, y: int):
        screen.blit(self.obstacle, (x, y))

    def draw_obstacles(self):
        for i in obstacles:
            self.draw_obstacle(i.position[0], i.position[1])

    def setup_level(self, enemy_count):
        for entity in range(enemy_count):
            enemy = AIEnemy(["player"], ["sprite/enemy.png"], "sprite/enemy_pain.png")
            entities.append(enemy)

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