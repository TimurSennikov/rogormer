import pygame
import pygame.locals
import math

from entities import *

import os

from game import *

def make_sequence(s, i, format):
    a = []
    for j in range(i):
        a.append (s + str(j) + format)
    return a

g = Game()
g.create_enemy(Nyanya("enemy", make_sequence("sprite/nyanya_idle_", 4, ".png"), [], []))

game_running = True

stories = [
    [["1995 год, Северная Америка.", "Из зоны 51 сбегает особо опасный иопланетянин.", "Лучшему агенту ЦРУ поручают поимку объекта.", "Лучшему среди худших...", "Вам предстоит играть за инопланетянина и отбиваться от ЦРУ.", ""], ["bg/def_0.png", "bg/roger_ship.png", "bg/stan_risk.png", "bg/stan_butt.png", "bg/stan_risk.png", "bg/info0.png"]],
    [["Стэн: Что? как он победил моих бойцов? ну уж нет, я не дам ему уйти...", "Стэн: выпускайте кракена!"], ["bg/stan_risk.png", "bg/stan_risk.png"]]
]
cur_story = 0

while cur_story < len(stories):
    g.show_story(stories[cur_story][0], stories[cur_story][1])

    while g.mainloop():
        pass

    cur_story += 1