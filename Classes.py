import pygame
import math

class Monster():

    def __init__(self, position, img, rect):
        self.position = position
        self.img = img
        self.rect = rect
        self.vel = 1

    def move(self, player):
        if player.position[0] > self.position[0]:
            self.position = (self.position[0]+self.vel, self.position[1])
        if player.position[0] < self.position[0]:
            self.position = (self.position[0]-self.vel, self.position[1])
        if player.position[1] > self.position[1]:
            self.position = (self.position[0], self.position[1]+self.vel)
        if player.position[1] < self.position[1]:
            self.position = (self.position[0], self.position[1]-self.vel)

class Player():

    def __init__(self, position, img, rect):
        self.position = position
        self.img = img
        self.rect = rect
        self.grau = 0
        self.passo = 1
        self.vel = 2

    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def moveUp(self):
        self.setPosition((self.position[0], self.position[1]-self.vel))
        
    def moveDown(self):
        self.setPosition((self.position[0], self.position[1]+self.vel))

    def moveRight(self):
        self.setPosition((self.position[0]+self.vel, self.position[1]))

    def moveLeft(self):
        self.setPosition((self.position[0]-self.vel, self.position[1]))

class Shot():

    def __init__(self, position, eixo, vel):
        self.position = position
        self.eixo = eixo
        if eixo == 'x':
            self.img = pygame.image.load('sprites_player/shotX.png')
            self.rect = (0, 0, 9, 30)
        else:
            self.img = pygame.image.load('sprites_player/shotY.png')
            self.rect = (0, 0, 30, 9)
        self.vel = vel * 10

    def move(self):
        if self.eixo == 'x':
            self.position = (self.position[0]+self.vel, self.position[1])
        else:
            self.position = (self.position[0], self.position[1]+self.vel)

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screen.fill((255, 255, 255))

img_player = pygame.image.load('sprites_player/sprite1_player_0.jpg')
player1 = Player((500-70/2, 350-70/2), img_player, (0, 0, 70, 70))
monster = Monster((0, 0), pygame.image.load('poring.png'), (0, 0, 70, 70))

inGame = True

shots = []
image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.jpg')

while inGame:
    pygame.time.Clock().tick(60)
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
        
    image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.jpg')
        
    player1.setImage(image)
    monster.move(player1)

    for shot in shots:
        shot.move()
        screen.blit(shot.img, shot.position, shot.rect)
        if shot.position[0] > 1000 or shot.position[0] < 0:
            shots.remove(shot)
        elif shot.position[1] > 700 or shot.position[1] < 0:
            shots.remove(shot)
                    
    screen.blit(player1.img, player1.position, player1.rect)
    screen.blit(monster.img, monster.position, monster.rect)
    pygame.display.update()
