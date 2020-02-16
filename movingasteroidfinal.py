#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p
from asteroidfinal import *


class movingasteroid(asteroid):

    asteroid = p.image.load('./img/aestroid_gray_50x50.png')
    window = p.display.set_mode((750, 1000))

    def __init__(
        self,
        x,
        y,
        speed,
        num,
    ):
        super().__init__(x, y, speed, num)

    def displayasteroid(self):
        self.window.blit(self.asteroid, (self.x, self.y))

    def move(  # Moves the asteroid around with the given velocity
        self,
        r,
        l,
        extraspeed,
    ):
        if self.x < r:
            self.x += self.speed + extraspeed
        else:
            self.x = l
