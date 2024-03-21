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
                  [0,1,10,100],
                  [0,220,10,450],
                  [0,96,150,10],
                  [0,205,70,16],
                  [66,300,90,10],
                  [66,205,10,100],
                  [140,96,10,90],
                  [66,420,70,10],
                  [66,170,10,100],
                  [66,378,10,200],
                  [200,350,70,10],
                  [270,350,10,50],
                  [280,390,70,10],
                  [0,487,4000,20],

                  

                  


                
]

walls=[]   

for w in walls_cordinates:
    wall = Walls(w[0],w[1],w[2],w[3],(225,255,255))
    walls.append(wall)






class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 60:
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys [K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
           self.rect.y=0
           self.rect.x=randint(80, win_widht-80)
           lost = lost + 1


mo1 =GameSprite('mo.png', 10,50,30,30,0)
mo2 =GameSprite('mo.png', 15,165,30,30,0)
mo3 =GameSprite('mo.png', 80,450,30,30,0)
mo4 =GameSprite('mo.png', 500,450,30,30,0)
mo5 =GameSprite('mo.png', 500,100,30,30,0)
mo6 =GameSprite('mo.png', 370,300,30,30,0)
mo7 =GameSprite('mo.png', 500,450,30,30,0)


window = display.set_mode((win_widht, win_height))
background = scale(load('images.jpg'), (win_widht, win_height))

ship = Player('uou.png', 10, win_height-60, 50, 50, 4)



font.init()
font1 = font.SysFont('Arial', 36)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    for w in walls:
        w.draw()
        w.draw()
        w.draw()





        if not finish:
            txt_win = font1.render(f'score: {score}', True, (255, 255, 255))
            window.blit(txt_win, (460, 16))

        mo1.reset()
        mo2.reset()
        mo3.reset()
        mo4.reset()
        mo5.reset()
        mo6.reset()
        mo7.reset()


    ship.reset()
    ship.update()


    display.update()
    clock.tick(FPS)