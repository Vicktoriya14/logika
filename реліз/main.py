from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0

back = (200,255,255)
win_widht = 600
win_height = 500
window = display.set_mode((win_widht,win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60





 
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

class Walls(GameSprite):
    def __init__(self,x,y,w,h,fill_color):
        self.rect = Rect(x,y,w,h)
        self.fill_color = fill_color

    def draw(self):
        draw.rect(window,self.fill_color, self.rect)

walls_cordinates = [

                  [0,0,4000,20],
                  [0,1,30,100],
                  [0,220,30,450],
                  [0,96,150,10],
                  [0,205,77,16],
                  [66,300,90,10],
                  [66,205,20,100],
                  [135,96,20,90],


                
]

walls=[]   

for w in walls_cordinates:
    wall = Walls(w[0],w[1],w[2],w[3],(10,88,90))
    walls.append(wall)




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 80:
            self.rect.x += self.speed

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


window = display.set_mode((win_widht, win_height))
background = scale(load('images.jpg'), (win_widht, win_height))

ship = Player('uou.png', 5, win_height-60, 60, 100, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    for w in walls:
        w.draw()
        w.draw()
        w.draw()


    ship.reset()
    ship.update()

    display.update()
    clock.tick(FPS)