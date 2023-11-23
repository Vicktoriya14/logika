#створи гру "Лабіринт"!
from typing import Any
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


import pygame

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_widht - 80:
            self.rect.y += self



class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_widht -80:
            self.direction = 'left'






win_widht = 700
win_height = 500

window = display.set_mode((win_widht, win_height))
background = scale(load('background.jpg'), (win_widht, win_height))

player = Player("hero.png", 5, win_height - 80, 4 )
monster = Enemy("cyborg.png", win_widht - 120, win_height - 280, 2)
treasure = GameSprite('treasure.png', win_widht-80, win_height-80, 0)



clock = time.Clock()
FPS = 60
game = True
finish = False

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if  not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        treasure.reset()

        player.update()
        monster.update()


    display.update()
    clock.tick(FPS)