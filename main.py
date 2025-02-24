import pygame
import pygame.locals
import math

from entities import *

import os

from game import *

g = Game()
g.setup_level(0)

game_running = True

g.show_story(["1995 год, Северная Америка.", "Из зоны 51 сбегает особо опасный иопланетянин.", "Лучшему агенту ЦРУ поручают поимку объекта.", "Лучшему среди худших...", "Вам предстоит играть за инопланетянина и отбиваться от ЦРУ.", ""], ["bg/def_0.png", "bg/roger_ship.png", "bg/stan_risk.png", "bg/stan_butt.png", "bg/stan_risk.png", "bg/info0.png"])

while game_running:
    g.mainloop()