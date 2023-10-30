#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


g1 = Game("Pacman")
g2 = Game("Tetris")
g3 = Game("Mario Kart")

p1 = Player("Trogdor")
p2 = Player("Cptn Kirk")

r1 = Result(p1, g1, 350)
r2 = Result(p1, g2, 19)
r3 = Result(p1, g2, 12)
r4 = Result(p2, g2, 3000)



ipdb.set_trace()
