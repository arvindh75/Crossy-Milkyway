#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p


class asteroid:

    def __init__(
        self,
        x,
        y,
        speed,
        num,
    ):
        self.x = x
        self.y = y
        self.speed = speed
        self.num = num

    # Function that checks for collision sati is gey
    def asteroidCollision(self, sx, sy):
        count = 0
        if sx >= self.x and sx <= self.x + 50 and sy >= self.y and sy \
                <= self.y + 50:
            print('hit rock ' + self.num)
            self.x = -420
            p.time.Clock().tick(2)
            count += 1
        if sx + 50 >= self.x and sx + 50 <= self.x + 50 and sy + 50 \
                >= self.y and sy + 50 <= self.y + 50:
            print('hit rock ' + self.num)
            self.x = -420
            p.time.Clock().tick(2)
            count += 1
        if sx + 50 >= self.x and sx + 50 <= self.x + 50 and sy \
                >= self.y and sy <= self.y + 50:
            print('hit rock ' + self.num)
            self.x = -420
            p.time.Clock().tick(2)
            count += 1
        if sx >= self.x and sx <= self.x + 50 and sy + 50 >= self.y \
                and sy + 50 <= self.y + 50:
            print('hit rock ' + self.num)
            self.x = -420
            p.time.Clock().tick(2)
            count += 1
        return count
