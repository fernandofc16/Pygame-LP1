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

    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def rotateCenter(self, angle):
        rot_image = pygame.transform.rotate(self.img, angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        self.setImage(rot_image)
        self.setRect(rot_rect)

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screen.fill((255, 255, 255))

img_player = pygame.image.load('sprite_player.jpg')
player1 = Player((500-68/2, 350-90/2), img_player, (0, 0, 68, 90))

inGame = True

while inGame:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                player1.setPosition((player1.position[0]-10, player1.position[1]-10))
            elif event.key == pygame.K_UP:
                player1.setPosition((player1.position[0], player1.position[1]-10))
            elif event.key == pygame.K_DOWN:
                player1.setPosition((player1.position[0], player1.position[1]+10))
            elif event.key == pygame.K_RIGHT:
                #player1.setPosition((player1.position[0]+10, player1.position[1]))
                player1.rotateCenter(math.radians(45))
            elif event.key == pygame.K_LEFT:
                #player1.setPosition((player1.position[0]-10, player1.position[1]))
                player1.rotateCenter(math.radians(-45))
            
    screen.blit(player1.img, player1.position, player1.rect)
    pygame.display.update()
