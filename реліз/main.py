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

class Walls(sprite.Sprite):
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
                  [350,240,10,160],
                  [200,460,10,220],
                  [480,330,10,160],
                  [430,360,55,10],
                  [560,400,55,10],
                  [350,280,70,10],
                  [420,130,10,160],
                  [500,200,100,10],
                  [528,130,10,100],
                  [595,0,10,400],
                  [150,176,100,10],
                  [528,130,10,100],
                 

                
]

walls=[]

for w in walls_cordinates:
    wall = Walls(w[0],w[1],w[2],w[3],(225,255,255))
    walls.append(wall)


def check_collide(obj,target_group):
    for target in target_group:
        if obj.rect.colliderect(target):
            return True



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            if check_collide(self,walls):
                self.rect.x += self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 60:
            self.rect.x += self.speed
            if check_collide(self,walls):
                self.rect.x -= self.speed
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            if check_collide(self,walls):
                self.rect.y += self.speed
        
        if keys [K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
            if check_collide(self,walls):
                self.rect.y -= self.speed
                
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
mo8 =GameSprite('mo.png', 300,350,30,30,0)
mo9 =GameSprite('mo.png', 440,380,30,30,0)
mo10 =GameSprite('mo.png', 160,130,30,30,0)
mo11 =GameSprite('mo.png', 550,170,30,30,0)



window = display.set_mode((win_widht, win_height))
background = scale(load('images.jpg'), (win_widht, win_height))

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (160, 0, 0))

ship = Player('uou.png', 10, win_height-60, 50, 50, 4)



font.init()
font1 = font.SysFont('Arial', 36)
coins = sprite.Group()
coins.add(mo1)
coins.add(mo2)
coins.add(mo3)
coins.add(mo4)
coins.add(mo5)
coins.add(mo6)
coins.add(mo7)
coins.add(mo8)
coins.add(mo9)
coins.add(mo10)
coins.add(mo11)




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    for w in walls:
        w.draw()
        w.draw()
        w.draw()

        if sprite.spritecollide(ship, coins, True):
            score+=1

     
     



        if not finish:
            txt_win = font1.render(f'score: {score}', True, (255, 255, 255))
            window.blit(txt_win, (460, 16))


        coins.draw(window)

        if score ==10: 
             finish = True
             window.blit(win,(200,200))


    ship.reset()
    ship.update()


    display.update()
    clock.tick(FPS)