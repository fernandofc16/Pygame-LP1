import pygame
import math
import random as rd

class Monster():

    def __init__(self, position, img):
        self.position = position
        self.img = img
        self.rect = pygame.Rect(position[0], position[1], img.get_width(), img.get_height())
        self.vel = rd.randint(1, 3)

    def move(self, player):
        if player.position[0]+player.img.get_width()/2 > self.position[0]+self.img.get_width()/2:
            self.position = (self.position[0]+self.vel, self.position[1])
            self.rect.x += self.vel
        if player.position[0]+player.img.get_width()/2 < self.position[0]+self.img.get_width()/2:
            self.position = (self.position[0]-self.vel, self.position[1])
            self.rect.x -= self.vel
        if player.position[1]+player.img.get_height()/2 > self.position[1]+self.img.get_height()/2:
            self.position = (self.position[0], self.position[1]+self.vel)
            self.rect.y += self.vel
        if player.position[1]+player.img.get_height()/2 < self.position[1]+self.img.get_height()/2:
            self.position = (self.position[0], self.position[1]-self.vel)
            self.rect.y -= self.vel

class Player():

    def __init__(self, position, img):
        self.position = position
        self.img = img
        self.rect = pygame.Rect(position[0], position[1], img.get_width(), img.get_height())
        self.grau = 0
        self.passo = 1
        self.vel = 7
        self.life = 3
  
    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def moveUp(self):
        self.setPosition((self.position[0], self.position[1]-self.vel))
        self.rect.y -= self.vel
        
    def moveDown(self):
        self.setPosition((self.position[0], self.position[1]+self.vel))
        self.rect.y += self.vel

    def moveRight(self):
        self.setPosition((self.position[0]+self.vel, self.position[1]))
        self.rect.x += self.vel

    def moveLeft(self):
        self.setPosition((self.position[0]-self.vel, self.position[1]))
        self.rect.x -= self.vel

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def damagePlayer(self, amount):
        self.life -= amount

    def isPlayerDead(self):
        return self.life <= 0

class Shot():

    def __init__(self, position, eixo, vel):
        self.position = position
        self.eixo = eixo
        if eixo == 'x':
            self.img = pygame.image.load('sprites_player/shotX.png')
        else:
            self.img = pygame.image.load('sprites_player/shotY.png')
        
        self.rect = pygame.Rect(position[0], position[1], self.img.get_width(), self.img.get_height())
        self.vel = vel * 25

    def move(self):
        if self.eixo == 'x':
            self.position = (self.position[0]+self.vel, self.position[1])
            self.rect.x += self.vel
        else:
            self.position = (self.position[0], self.position[1]+self.vel)
            self.rect.y += self.vel

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screen.fill((255, 255, 255))

img_player = pygame.image.load('sprites_player/sprite1_player_0.png')
player1 = Player((500-70/2, 350-70/2), img_player)
monsters = []

for i in range(2):
    monsters.append(Monster((rd.randint(-50, -30), rd.randint(30, 670)), pygame.image.load('poring.png')))
    monsters.append(Monster((rd.randint(30, 970), rd.randint(-50, -30)), pygame.image.load('poring.png')))
    monsters.append(Monster((rd.randint(1030, 1050), rd.randint(30, 670)), pygame.image.load('poring.png')))
    monsters.append(Monster((rd.randint(30, 970), rd.randint(730, 750)), pygame.image.load('poring.png')))

inGame = True
win = False

shots = []
image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.png')

while inGame:
    pygame.time.Clock().tick(25)
    screen.fill((255, 255, 255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.grau = 0
        player1.moveUp()
        player1.passo += 1
    elif keys[pygame.K_DOWN]:
        player1.grau = 180
        player1.moveDown()
        player1.passo += 1
    elif keys[pygame.K_RIGHT]:
        player1.grau = 90
        player1.moveRight()
        player1.passo += 1
    elif keys[pygame.K_LEFT]:
        player1.grau = 270
        player1.moveLeft()
        player1.passo += 1
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player1.grau == 0:
                    shots.append(Shot((player1.position[0]+40, player1.position[1]), 'y', -1))
                elif player1.grau == 180:
                    shots.append(Shot((player1.position[0]+20, player1.position[1]), 'y',  1)) 
                elif player1.grau == 90:
                    shots.append(Shot((player1.position[0], player1.position[1]+40), 'x',  1))
                else:
                    shots.append(Shot((player1.position[0], player1.position[1]+20), 'x', -1))
            print(len(shots))

    if player1.grau >= 360:
        player1.grau = 0
    if player1.grau < 0:
        player1.grau = 360 + player1.grau

    if player1.passo > 3:
        player1.passo = 1
        
    image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.png')      
    player1.setImage(image)

    for shot in shots:
        shot.move()
        screen.blit(shot.img, shot.position)
        if shot.position[0] > 1000 or shot.position[0] < 0:
            shots.remove(shot)
        elif shot.position[1] > 700 or shot.position[1] < 0:
            shots.remove(shot)
    
    for monster in monsters:
        monster.move(player1)
        screen.blit(monster.img, monster.position)
        if player1.is_collided_with(monster):
            print("COLIDIU")
            player1.damagePlayer(1)
            monsters.remove(monster)
            if(player1.isPlayerDead()):
                inGame = False
        for shot in shots:
            if shot.is_collided_with(monster):
                print("MATOU")
                monsters.remove(monster)
                shots.remove(shot)

    if len(monsters) == 0:
        win = True
        inGame = False
                    
    screen.blit(player1.img, player1.position)
    
    pygame.display.update()

if win:
    screen.blit(pygame.image.load('you_win.jpg'), (0, 0))
else: 
    screen.blit(pygame.image.load('game_over.png'), (0, 0))
pygame.display.update()
