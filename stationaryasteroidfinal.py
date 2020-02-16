#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p
from asteroidfinal import *


class stationaryasteroid(asteroid):

    asteroid = p.image.load('./img/aestroid_brown_1_75x75.png')
    window = p.display.set_mode((750, 1000))

    def __init__(
        self,
        x,
        y,
        num,
    ):
        super().__init__(x, y, 0, num)

    def displayasteroid(self):  # Display the asteroid
        self.window.blit(self.asteroid, (self.x, self.y))
