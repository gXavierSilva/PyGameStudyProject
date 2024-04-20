#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code import Const
from code.Menu import Menu


class Game:
    # Construtor
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Const.WIN_WIDTH, Const.WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
