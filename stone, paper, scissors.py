import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 24)
pygame.display.set_caption("stone, paper, scissors")
icon = pygame.image.load("h2.png")
pygame.display.set_icon(icon)
color = (0, 0, 0)
player_turn = "off"
oponent_turn = "off"
turn = "on"
background = pygame.image.load("10572.jpg")
backgroundX = 0
backgroundY = 0
startpos_1 = 690, 1000
startpos_2 = 680, 1000
endpos_1 = 690, -10
endpos_2 = 680, -10
num = [1, 2, 3]

player_paper = pygame.image.load("h2.png")
playerpX = 100
playerpY = -2000

player_scissors = pygame.image.load("2f.png")
playersX = 100
playersY = -2000

player_rock = pygame.image.load("p2.png")
playerrX = 100
playerrY = -2000

enemy_paper = pygame.image.load("five.png")
enemypX = 100
enemypY = -2000

enemy_scissors = pygame.image.load("two-fingers.png")
enemysX = 100
enemysY = -2000

change = 1

enemy_rock = pygame.image.load("fist.png")
enemyrX = 100
enemyrY = -2000

player_score = 0
oponent_score = 0

game_font = pygame.font.Font("KurriIslandItaPERSONAL-Bold.ttf", 100)
won_font = pygame.font.Font("SEASRN__.ttf", 200)

player_fontX = 350
player_fontY = 20
enemy_fontX = 1050
enemy_fontY = 20
score_fontX = 490
score_fontY = 20
won_fontX = 80
won_fontY = 170


def player_fon(x, y):
    gaming = game_font.render(str(player_score), True, (0, 0, 0))
    screen.blit(gaming, (x, y))


def won():
    win2 = won_font.render("YOU WON", True, (0, 0, 0))
    screen.blit(win2, (won_fontX, won_fontY))


def won2():
    win = won_font.render("YOU LOST", True, (0, 0, 0))
    screen.blit(win, (won_fontX, won_fontY))


def score(x, y):
    scoring = game_font.render(": SCORE :", True, (0, 0, 0))
    screen.blit(scoring, (x, y))


def enemy_fon(x, y):
    ene = game_font.render(str(oponent_score), True, (0, 0, 0))
    screen.blit(ene, (x, y))


def players():
    screen.blit(player_paper, (playerpX, playerpY))


def back():
    screen.blit(background, (backgroundX, backgroundY))


def players2():
    screen.blit(player_scissors, (playersX, playersY))


def players3():
    screen.blit(player_rock, (playerrX, playerrY))


def enemy():
    screen.blit(enemy_paper, (enemypX, enemypY))


def enemy2():
    screen.blit(enemy_scissors, (enemysX, enemysY))


def enemy3():
    screen.blit(enemy_rock, (enemyrX, enemyrY))


running = True
while running:
    screen.fill((0, 255, 127))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                playerrX = 20
                playerrY = 170
                playersX = 1000
                playersY = -2000
                playerpY = -4000
                player_turn = "stone"
                oponent = random.choice(num)
                if oponent == 1:
                    enemyrX = 850
                    enemyrY = 170
                    enemysX = 750
                    enemysY = -2550
                    enemypY = -2900
                    enemypX = 4000
                    oponent_turn = "stone"
                if oponent == 2:
                    enemysX = 850
                    enemysY = 170
                    oponent_turn = "scissor"
                    enemyrX = 750
                    enemyrY = -2550
                    enemypY = -2900
                    enemypX = 4000
                if oponent == 3:
                    enemypX = 850
                    enemypY = 170
                    enemyrX = 750
                    enemyrY = -2550
                    enemysX = 750
                    enemysY = -2550
                    oponent_turn = "paper"
            if event.key == pygame.K_2:
                playerpX = 20
                playerpY = 170
                playersX = 3000
                playersY = -2000
                playerrY = -2000
                player_turn = "paper"
                oponent = random.choice(num)
                if oponent == 1:
                    enemyrX = 850
                    enemyrY = 170
                    enemysX = 750
                    enemysY = -2550
                    enemypY = -2900
                    enemypX = 4000
                    oponent_turn = "stone"
                if oponent == 2:
                    enemysX = 850
                    enemysY = 170
                    oponent_turn = "scissor"
                    enemyrX = 750
                    enemyrY = -2550
                    enemypY = -2900
                    enemypX = 4000
                if oponent == 3:
                    enemypX = 850
                    enemypY = 170
                    enemyrX = 750
                    enemyrY = -2550
                    enemysX = 750
                    enemysY = -2550
                    oponent_turn = "paper"
            if event.key == pygame.K_3:
                playersX = 20
                playersY = 170
                playerpY = 3000
                playerrY = 3000
                player_turn = "scissor"
                oponent = random.choice(num)
                if oponent == 1:
                    enemyrX = 850
                    enemyrY = 170
                    enemysX = 750
                    enemysY = -2550
                    enemypY = -2900
                    enemypX = 4000
                    oponent_turn = "stone"
                if oponent == 2:
                    enemysX = 850
                    enemysY = 170
                    oponent_turn = "scissor"
                    enemyrX = 750
                    enemyrY = -2550
                    enemypY = -2900
                    enemypX = 4000
                if oponent == 3:
                    enemypX = 850
                    enemypY = 170
                    enemyrX = 750
                    enemyrY = -2550
                    enemysX = 750
                    enemysY = -2550
                    oponent_turn = "paper"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                player_turn = "no"
                oponent_turn = "no"
            if event.key == pygame.K_2:
                player_turn = "no"
                oponent_turn = "no"
            if event.key == pygame.K_3:
                player_turn = "no"
                oponent_turn = "no"

        if player_turn == "stone" and oponent_turn == "scissor":
            player_score += change
            turn = "off"

        if player_turn == "paper":
            if oponent_turn == "stone":
                player_score += change
                turn = "off"

        if player_turn == "scissor" and oponent_turn == "paper":
            player_score += change

        if oponent_turn == "stone" and player_turn == "scissor":
            oponent_score += 1
        if oponent_turn == "paper" and player_turn == "stone":
            oponent_score += 1
        if oponent_turn == "scissor" and player_turn == "paper":
            oponent_score += 1

        if oponent_turn == "stone" and player_turn == "stone":
            oponent_score += 0
            player_score += 0
        if oponent_turn == "paper" and player_turn == "paper":
            oponent_score += 0
            player_score += 0
        if oponent_turn == "scissor" and player_turn == "scissor":
            oponent_score += 0
            player_score += 0

    if player_score >= 15:
        playerrY, playerpY, playersY = 10000, 10000, 10000
        enemyrY, enemypY, enemysY = 1000, 1000, 1000
        startpos_1 = 1, 1
        startpos_2 = 1, 1
        endpos_1 = 0, 0
        endpos_2 = 0, 0
        player_fontY, enemy_fontY = 1000, 1000
        score_fontY = 1000
        won()

    if oponent_score >= 15:
        playerrY, playerpY, playersY = 10000, 10000, 10000
        enemyrY, enemypY, enemysY = 1000, 1000, 1000
        startpos_1 = 1, 1
        startpos_2 = 1, 1
        endpos_1 = 0, 0
        endpos_2 = 0, 0
        player_fontY, enemy_fontY = 1000, 1000
        score_fontY = 1000
        won2()

    pygame.draw.aaline(screen, color, startpos_1, endpos_1)
    pygame.draw.aaline(screen, color, startpos_2, endpos_2)
    players()
    players2()
    players3()
    player_fon(player_fontX, player_fontY)
    enemy_fon(enemy_fontX, enemy_fontY)
    score(score_fontX, score_fontY)
    enemy()
    enemy2()
    enemy3()
    pygame.display.update()
