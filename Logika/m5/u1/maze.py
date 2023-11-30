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
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_widht - 80:
            self.rect.y += self.speed



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



class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.hight = wall_height
        self.image = Surface((self.width, self.hight))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

        self.image.fill((0, 255, 0))


    def  reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




win_widht = 700
win_height = 500

window = display.set_mode((win_widht, win_height))
background = scale(load('background.jpg'), (win_widht, win_height))


wall_1 = Wall(1, 20, 45, 15)
wall_2 = Wall(3, 45, 67, 23)
wall_3 = Wall(3, 45, 67, 23)
wall_4 = Wall(3, 45, 67, 23)

player = Player("hero.png", 5, win_height - 80, 4 )
monster = Enemy("cyborg.png", win_widht - 120, win_height - 280, 2)
treasure = GameSprite('treasure.png', win_widht-80, win_height-80, 0)



clock = time.Clock()
FPS = 60
game = True
finish = False


font.init()
f = font.Font(None, 70)

win = f.render('YOU WIN!', True, (255, 215, 0))
lose = f.render('YOU LOSE!', True, (255, 0, 0))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if  not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        treasure.reset()
        wall_1.reset()
        wall_2.reset()
        wall_3.reset()
        wall_4.reset()


        player.update()
        monster.update()

    if sprite.collide_rect(player, treasure):
        finish = True
        window.blit(win, (200, 200))
        money_sound.play()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall_1):
        finish = True
        window.blit(lose, (200, 200))
        kick_sound.play()

  

    display.update()
    clock.tick(FPS)