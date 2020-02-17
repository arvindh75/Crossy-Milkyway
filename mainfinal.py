#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p
from asteroidfinal import *
from movingasteroidfinal import *
from stationaryasteroidfinal import *
from config import *
p.init()
p.font.init()
p.mixer.music.load(music)
p.mixer.music.play(-1, 0.0)
text = p.font.SysFont(fontGame, 30)  # loads the main game font
activePlayer = 1
textsurface1 = text.render(player1timetext, True, (255, 255, 255))
textsurface2 = text.render(player2timetext, True, (255, 255, 255))
penaltyscal = 1
x = 350
y = 920
xp2 = 350
yp2 = 0
h = 50
w = 50
finalscore1 = 0
finalscore2 = 0
gameswon1 = 0
gameswon2 = 0
score = 0
size = 750
sizey = 1000
window = p.display.set_mode((size, 1000))
speed = 5
count1 = 0
count2 = 0
extraspeed1 = 0
extraspeed2 = 0
crossedy1 = [0, 0, 0, 0, 0]
crossedy2 = [0, 0, 0, 0, 0]
window = p.display.set_mode((750, 1000))
p.display.set_caption(gamecaption)
player1 = p.image.load(player1img)
player2 = p.image.load(player2img)
bg = p.image.load(bgimg)
asteroid = movingasteroid(0, 100, 7, 'm1')  # Creates instance of Asteroid
asteroid1 = movingasteroid(5, 250, 8, 'm2')
asteroid2 = movingasteroid(-10, 400, 10, 'm3')
asteroid3 = movingasteroid(-5, 600, 3, 'm4')
asteroid4 = movingasteroid(-2, 750, 6, 'm5')
asteroidf1 = stationaryasteroid(300, 155, 's1')
asteroidf2 = stationaryasteroid(150, 320, 's2')
asteroidf3 = stationaryasteroid(500, 500, 's3')
asteroidf4 = stationaryasteroid(200, 660, 's4')
asteroidf5 = stationaryasteroid(300, 830, 's5')


# A function that calls coliision method for each asteroid and counts the
# number of collision for each player
def collision(player1time, player2time):
    global count1, finalscore1
    global count2, finalscore2
    count = 0
    count += asteroid.asteroidCollision(x, y)
    count += asteroid1.asteroidCollision(x, y)
    count += asteroid2.asteroidCollision(x, y)
    count += asteroid3.asteroidCollision(x, y)
    count += asteroid4.asteroidCollision(x, y)
    count += asteroidf1.asteroidCollision(x, y)
    count += asteroidf2.asteroidCollision(x, y)
    count += asteroidf3.asteroidCollision(x, y)
    count += asteroidf4.asteroidCollision(x, y)
    count += asteroidf5.asteroidCollision(x, y)

    count += asteroid.asteroidCollision(xp2, yp2)
    count += asteroid1.asteroidCollision(xp2, yp2)
    count += asteroid2.asteroidCollision(xp2, yp2)
    count += asteroid3.asteroidCollision(xp2, yp2)
    count += asteroid4.asteroidCollision(xp2, yp2)
    count += asteroidf1.asteroidCollision(xp2, yp2)
    count += asteroidf2.asteroidCollision(xp2, yp2)
    count += asteroidf3.asteroidCollision(xp2, yp2)
    count += asteroidf4.asteroidCollision(xp2, yp2)
    count += asteroidf5.asteroidCollision(xp2, yp2)
    if activePlayer == 1:
        count1 += count
        finalscore1 -= 10 * count
    if activePlayer == 2:
        count2 += count
        finalscore2 -= 10 * count

# Calculates the score of the player if he crosses an obstacle succesfully


def scorecalc():
    global x, y, xp2, yp2, finalscore1, finalscore2
    if activePlayer == 1:
        if y <= 830 and crossedy1[0] == 0:
            finalscore1 += 10
            crossedy1[0] = 1
        if y <= 660 and crossedy1[1] == 0:
            finalscore1 += 20
            crossedy1[1] = 1
        if y <= 500 and crossedy1[2] == 0:
            finalscore1 += 30
            crossedy1[2] = 1
        if y <= 320 and crossedy1[3] == 0:
            finalscore1 += 40
            crossedy1[3] = 1
        if y <= 155 and crossedy1[4] == 0:
            finalscore1 += 50
            crossedy1[4] = 1
    if activePlayer == 2:
        if yp2 >= 155 and crossedy2[0] == 0:
            finalscore2 += 10
            crossedy2[0] = 1
        if yp2 >= 320 and crossedy2[1] == 0:
            finalscore2 += 20
            crossedy2[1] = 1
        if yp2 >= 500 and crossedy2[2] == 0:
            finalscore2 += 30
            crossedy2[2] = 1
        if yp2 >= 660 and crossedy2[3] == 0:
            finalscore2 += 40
            crossedy2[3] = 1
        if yp2 >= 830 and crossedy2[4] == 0:
            finalscore2 += 50
            crossedy2[4] = 1

# Displays all the elements in the screen currently


def elements(player1time, player2time):
    window.blit(bg, (0, 0))
    asteroid1.displayasteroid()
    asteroid2.displayasteroid()
    asteroid3.displayasteroid()
    asteroid4.displayasteroid()
    asteroidf1.displayasteroid()
    asteroidf2.displayasteroid()
    asteroidf3.displayasteroid()
    asteroidf4.displayasteroid()
    asteroidf5.displayasteroid()
    if activePlayer == 1:
        window.blit(player1, (x, y))
    elif activePlayer == 2:
        window.blit(player2, (xp2, yp2))
    scorecalc()  # Calculates the score
    collision(player1time, player2time)
    if activePlayer == 1:
        asteroid.move(800, -5, extraspeed1)
        asteroid.displayasteroid()
        asteroid1.move(775, -10, extraspeed1)
        asteroid2.move(900, -15, extraspeed1)
        asteroid3.move(1000, -2, extraspeed1)
        asteroid4.move(1200, -7, extraspeed1)
    if activePlayer == 2:
        asteroid.move(800, -5, extraspeed2)
        asteroid.displayasteroid()
        asteroid1.move(775, -10, extraspeed2)
        asteroid2.move(900, -15, extraspeed2)
        asteroid3.move(1000, -2, extraspeed2)
        asteroid4.move(1200, -7, extraspeed2)


run = True
runmenu = True
player1time = 0
player2time = 0
countdown = p.time.get_ticks()
while runmenu:  # Runs the menu until the player starts the game
    text1 = p.font.Font(menufont, 30)
    text2 = p.font.Font(titlefont, 30)
    window.blit(bg, (0, 0))  # Displays the Background image
    textsurface2 = text2.render(gamecaption, True, (255, 255, 255))
    window.blit(textsurface2, (0, 150))
    textsurface2 = text1.render(menul1, True, (255, 255, 255))
    window.blit(textsurface2, (80, 400))
    textsurface2 = text1.render(menul2, True, (255, 255, 255))
    window.blit(textsurface2, (65, 600))
    textsurface2 = text1.render(menul3, True, (255, 255, 255))
    window.blit(textsurface2, (120, 660))
    textsurface2 = text1.render(menul4, True, (255, 255, 255))
    window.blit(textsurface2, (50, 720))
    textsurface2 = text1.render(menul5, True, (255, 255, 255))
    window.blit(textsurface2, (300, 780))
    text1 = p.font.Font(menufont, 27)
    textsurface2 = text1.render(menul6, True, (255, 255, 255))
    window.blit(textsurface2, (0, 840))
    arrow = p.key.get_pressed()
    if arrow[p.K_SPACE]:
        runmenu = False
    p.display.update()
    for a in p.event.get():
        if a.type == p.QUIT:
            runmenu = False
            run = False
while run:  # Runs the main game
    seconds = (p.time.get_ticks() - countdown) / 1000
    p.time.delay(10)
    for a in p.event.get():
        if a.type == p.QUIT:
            run = False
    arrow = p.key.get_pressed()
    if arrow[p.K_ESCAPE]:  # Quits the game if ESC is pressed
        run = False
    if activePlayer == 1:
        if arrow[p.K_LEFT]:  # Left Movement
            if x - speed >= 0:
                x -= speed
        if arrow[p.K_RIGHT]:  # Right Movement
            if x + speed <= size - w:
                x += speed
        if arrow[p.K_UP]:  # Upward Movement
            if y - speed >= 0:
                y -= speed
        if arrow[p.K_DOWN]:  # Downward Movement
            if y + speed <= sizey - h:
                y += speed

    if activePlayer == 2:  # Movement for Player 2
        if arrow[p.K_a]:
            if xp2 - speed >= 0:
                xp2 -= speed
        if arrow[p.K_d]:
            if xp2 + speed <= size - w:
                xp2 += speed
        if arrow[p.K_w]:
            if yp2 - speed >= 0:
                yp2 -= speed
        if arrow[p.K_s]:
            if yp2 + speed <= sizey - h:
                yp2 += speed
# Checks if player1 has completed successfully

    if y == 0 and activePlayer == 1:
        print(p1win)
        activePlayer = 2
        player1time = seconds
        print(seconds)
        textsurface1 = text.render(player1timetext + str(player1time),
                                   True, (255, 255, 255))
        window.blit(textsurface1, (0, 30))
        countdown = p.time.get_ticks()
        print(count1)
        asteroid = movingasteroid(0, 100, 7, 'm1')
        asteroid1 = movingasteroid(5, 250, 8, 'm2')
        asteroid2 = movingasteroid(-10, 400, 10, 'm3')
        asteroid3 = movingasteroid(-5, 600, 3, 'm4')
        asteroid4 = movingasteroid(-2, 750, 6, 'm5')
        asteroidf1 = stationaryasteroid(300, 155, 's1')
        asteroidf2 = stationaryasteroid(150, 320, 's2')
        asteroidf3 = stationaryasteroid(500, 500, 's3')
        asteroidf4 = stationaryasteroid(200, 660, 's4')
        asteroidf5 = stationaryasteroid(300, 830, 's5')
# Checks if player2 has completed successfully

    if yp2 == 940 and activePlayer == 2:
        print(p2win)
        activePlayer = 1
        x = 350
        y = 920
        yp2 = 0
        xp2 = 350
        print(count1)
        player2time = seconds
        print(seconds)
        textsurface2 = text.render(player2timetext + str(player2time),
                                   True, (255, 255, 255))
        window.blit(textsurface2, (0, 60))
        countdown = p.time.get_ticks()
        if player1time + count1 * 0.25 > player2time + count2 * 0.25:
            print(p2fwin)
            extraspeed2 += 2  # Increases the speed of obstacles for P2
            gameswon2 += 1
        elif player1time + count1 * 0.25 < player2time + count2 * 0.25:
            print(p1fwin)
            extraspeed1 += 2  # Increases the speed of obstacles for P1
            gameswon1 += 1
        else:
            print(tie)
            extraspeed1 += 2  # Increases the speed of obstacles
            extraspeed2 += 2
        count1 = 0  # Resets the scores after every round
        count2 = 0
        count = 0
        finalscore1 = 0
        finalscore2 = 0
        for x in range(5):  # Re-initializes all the flag values
            crossedy1[x] = 0
            crossedy2[x] = 0
        player1time = 0
        player2time = 0
        asteroid = movingasteroid(0, 100, 7, 'm1')
        asteroid1 = movingasteroid(5, 250, 8, 'm2')
        asteroid2 = movingasteroid(-10, 400, 10, 'm3')
        asteroid3 = movingasteroid(-5, 600, 3, 'm4')
        asteroid4 = movingasteroid(-2, 750, 6, 'm5')
        asteroidf1 = stationaryasteroid(300, 155, 's1')
        asteroidf2 = stationaryasteroid(150, 320, 's2')
        asteroidf3 = stationaryasteroid(500, 500, 's3')
        asteroidf4 = stationaryasteroid(200, 660, 's4')
        asteroidf5 = stationaryasteroid(300, 830, 's5')
    elements(player1time, player2time)
    textsurface = text.render(time + str(seconds), True, (255, 255,
                                                          255))
    textsurface4 = text.render(p1score + str(finalscore1), True, (255,
                                                                  255, 255))
    window.blit(textsurface4, (0, 150))  # Prints the Final Score of P1
    textsurface4 = text.render(p2score + str(finalscore2), True, (255,
                                                                  255, 255))
    window.blit(textsurface4, (0, 180))  # Prints the Final Score of P2
    pen1f = player1time + count1 * penaltyscal
    textsurface4 = text.render(p1pen + str(pen1f), True, (255, 255, 255))
    window.blit(textsurface4, (0, 30))  # Prints the Penalty Score of P1
    pen2f = player2time + count2 * penaltyscal
    textsurface3 = text.render(p2pen + str(pen2f), True, (255, 255, 255))
    window.blit(textsurface3, (0, 60))  # Prints the Penalty Score of P2
    textsurface5 = text.render(p1wins + str(gameswon1), True, (255,
                                                               255, 255))
    window.blit(textsurface5, (0, 90))  # Prints the number of games won
    textsurface6 = text.render(p2wins + str(gameswon2), True, (255,
                                                               255, 255))
    window.blit(textsurface6, (0, 120))
    textsurface7 = text.render(escape, True, (255, 255, 255))
    window.blit(textsurface7, (475, 0))
    window.blit(textsurface, (0, 0))
    p.display.update()  # Updates the diaplay with the current elements
p.quit()  # Quits the game
