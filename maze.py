from pygame import *


init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 15:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 615:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)
        self.direction = 'left'

    def update1(self):
        if self.rect.x <= 100:
            self.direction = 'right'
        if self.rect.x > 500:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update2(self):
        if self.rect.x <= 350:
            self.direction = 'right'
        if self.rect.x > 600:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height, color1, color2, color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Лаберинт')
background = transform.scale(image.load('background.jpg'), (700, 500))
player = Player('hero.png', 5, 50, 400)
enemy1 = Enemy('cyborg.png', 2, 325, 150)
enemy2 = Enemy('cyborg.png', 4, 450, 350)
treasure = GameSprite('treasure.png', 5, 400, 50)
wall_1 = Wall(20, 20, 10, 550, 255, 255, 255)
wall_2 = Wall(20, 20, 640, 10, 255, 255, 255)
wall_3 = Wall(340, 20, 10, 100, 255, 255, 255)
wall_4 = Wall(660, 20, 10, 550, 255, 255, 255)
wall_5 = Wall(120, 120, 440, 10, 255, 255, 255)
wall_6 = Wall(340, 240, 10, 350, 255, 255, 255)
wall_7 = Wall(560, 120, 10, 200, 255, 255, 255)
wall_8 = Wall(120, 240, 10, 350, 255, 255, 255)


game = True
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.2)
mixer.music.play()
clock = time.Clock()
FPS = 60
finish = False
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
win_text = font.SysFont('verdana', 70).render('YOU WIN!', True, (250, 244, 60))
lose_text = font.SysFont('verdana', 70).render('YOU LOSE!', True, (232, 62, 39))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
                player.rect.x = 50
                player.rect.y = 400

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy1.update1()
        enemy1.reset()
        enemy2.update2()
        enemy2.reset()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        if sprite.collide_rect(player, treasure):
            finish = True
            money.play()
            window.blit(win_text, (150, 200))
        if sprite.collide_rect(player, enemy1):
            finish = True
            kick.play()
            window.blit(lose_text, (150, 200))
        if sprite.collide_rect(player, enemy2):
            finish = True
            kick.play()
            window.blit(lose_text, (150, 200))
        if sprite.collide_rect(player, wall_1):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_2):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_3):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_4):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_5):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_6):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_7):
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, wall_8):
            player.rect.x = 50
            player.rect.y = 400

    clock.tick(FPS)
    display.update()