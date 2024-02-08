from pygame import*

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
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
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



racket1 = Player('llll.jpg',30,200,4,20,150)
racket2 = Player('llll.jpg',520,200,4,20,150)

ball = GameSprite('bbbb.jpg',200,200,4,50,50)

font.init()
font = font.Font(None,25)
loser1 = font.render('Player 1 Lose!',True,(180,0,10))
loser2 = font.render('Player 2 Lose!',True,(180,0,10))

speed_x = 4
speed_y = 4


while game:
    for event in event.get():
        if event.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height-50 or ball.rect.y<0:
            speed_y *= -1


        if ball.rect.x < 0:
            finish = True
            window.blit(loser1,(200,200))
            game_over = True


        if ball.rect.x > win_widht:
            finish = True
            window.blit(loser2,(200,200))
            game_over = True



        racket1.reset()
        racket2.reset()














