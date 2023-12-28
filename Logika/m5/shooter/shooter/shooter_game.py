
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed) :
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 30, 15)
        bullets.add(bullet)




class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
           self.rect.y=0
           self.rect.x=randint(80, win_widht-80)
           lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

b1 = Bullet('bullet.png', 350, 350, 15, 30, 3)


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.01)

font.init()
font1 = font.SysFont('Arial', 36)

font2 = font.SysFont('Arial', 80) 
txt_lose_game = font2.render('Ти програв!', True, (200, 0, 0))
txt_win_game = font2.render('Ти виграв!', True, (0, 200, 50))

win_widht = 700
win_height = 500

window = display.set_mode((win_widht, win_height))
background = scale(load('galaxy.jpg'), (win_widht, win_height))

ship = Player('rocket.png', 5, win_height-80, 80, 100, 4)

bullets = sprite.Group()




monsters = sprite.Group()
for i in range(5):
    mon = Enemy('ufo.png', randint(0, win_widht-80), 0, 80, 50, randint(1, 5))
    monsters.add(mon)

clock = time.Clock()
FPS = 60

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()



    if not finish:
        window.blit(background, (0, 0))
        txt_lose = font1.render(f'Пропущено: {lost}', True, (255, 255, 255))
        window.blit(txt_lose, (10, 50))

        txt_win = font1.render(f'Рахунок: {score}', True, (255, 255, 255))
        window.blit(txt_win, (10, 10))

        monsters.draw(window)
        monsters.update()



        bullets.draw(window)
        bullets.update()

        ship.reset()
        ship.update()

        if sprite.spritecollide(ship, monsters, False):
            finish = True
            window.blit(txt_lose_game, (200, 200))
           


        collied = sprite.groupcollide(monsters, bullets, True, True)
        for c in collied:
            mon = Enemy('ufo.png', randint(0, win_widht-80), 0, 80, 50, randint(1, 5))
            monsters.add(mon)
            score = score + 1


        if score == 5:
            finish = True
            window.blit(txt_win_game, (200, 200))

    else:
        finish = False
        score = 0
        lost = 0
        
        for b in bullets:
            b.kill()

        for m in monsters:
            m.kill()


        time.delay(3000)
        for i in range(5):
            mon = Enemy('ufo.png', randint(0, win_widht-80), 0, 80, 50, randint(1, 5))
            monsters.add(mon)




    display.update()
    clock.tick(FPS)


        

