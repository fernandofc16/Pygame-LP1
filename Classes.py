import pygame
import math

class Monster():

    def __init__(self, posx, posy, img, rect):
        self.posx = posx
        self.posy = posy
        self.img = img
        self.rect = rect

class Player():

    def __init__(self, position, img, rect):
        self.position = position
        self.img = img
        self.rect = rect
        self.grau = 0
        self.passo = 1

    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def rotateCenter(self, angle):
        loc = self.img.get_rect().center
        rot_sprite = pygame.transform.rotate(self.img, angle)
        rot_sprite.get_rect().center = loc
        self.setImage(rot_sprite)
        self.setRect(rot_sprite.get_rect())

class Shot():

    def __init__(self, position, eixo):
        self.position = position
        self.eixo = eixo
        if eixo == 'x':
            self.img = pygame.image.load('sprites_player/shotX.png')
            self.rect = (0, 0, 9, 30)
        else:
            self.img = pygame.image.load('sprites_player/shotY.png')
            self.rect = (0, 0, 30, 9)
        self.vel = 20

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

inGame = True

shots = []

while inGame:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player1.grau == 0:
                    player1.setPosition((player1.position[0], player1.position[1]-10))
                elif player1.grau == 90:
                    player1.setPosition((player1.position[0]+10, player1.position[1]))
                elif player1.grau == 180:
                    player1.setPosition((player1.position[0], player1.position[1]+10))
                elif player1.grau == 270:
                    player1.setPosition((player1.position[0]-10, player1.position[1]))
                player1.passo += 1
            elif event.key == pygame.K_DOWN:
                if player1.grau == 0:
                    player1.setPosition((player1.position[0], player1.position[1]+10))
                elif player1.grau == 90:
                    player1.setPosition((player1.position[0]-10, player1.position[1]))
                elif player1.grau == 180:
                    player1.setPosition((player1.position[0], player1.position[1]-10))
                elif player1.grau == 270:
                    player1.setPosition((player1.position[0]+10, player1.position[1]))
                player1.passo -= 1
            elif event.key == pygame.K_RIGHT:
                #player1.setPosition((player1.position[0]+10, player1.position[1]))
                player1.grau += 90
            elif event.key == pygame.K_LEFT:
                #player1.setPosition((player1.position[0]-10, player1.position[1]))
                player1.grau -= 90
            elif event.key == pygame.K_SPACE:
                if player1.grau == 0 or player1.grau == 180:
                    shots.append(Shot(player1.position, 'y'))
                else:
                    shots.append(Shot(player1.position, 'x'))

            for shot in shots:
                shot.move()
                if shot.position[0] > 1000 or shot.position[0] < 0:
                    shots.remove(shot)
                elif shot.position[1] > 700 or shot.position[1] < 0:
                    shots.remove(shot)

            if player1.grau >= 360:
                player1.grau = 0
            if player1.grau < 0:
                player1.grau = 360 + player1.grau
            if player1.passo > 3:
                player1.passo = 1
            if player1.passo < 1:
                player1.passo = 3
            player1.setImage(pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.jpg'))
                   
    screen.blit(player1.img, player1.position, player1.rect)
    pygame.display.update()

clock.tick(60)
