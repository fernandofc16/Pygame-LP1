import pygame
import math
import random as rd

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Monster():

    def __init__(self, position, img_left, img_right):
        self.position = position
        self.img_left = img_left
        self.img_right = img_right
        self.img_width = img_right[0].get_width()
        self.img_height = img_right[0].get_height()
        self.rect = pygame.Rect(position[0], position[1], img_right[0].get_width(), self.img_height)
        self.vel = rd.randint(1, 3)
        self.direction = 1
        self.index = rd.randint(1, self.vel)
        self.changeValue = 1

    def move(self, player):
        if player.position[0]+player.img.get_width()/2 > self.position[0]+self.img_width/2:
            self.position = (self.position[0]+self.vel, self.position[1])
            self.rect.x += self.vel
            self.direction = 0
        if player.position[0]+player.img.get_width()/2 < self.position[0]+self.img_width/2:
            self.position = (self.position[0]-self.vel, self.position[1])
            self.rect.x -= self.vel
            self.direction = 1
        if player.position[1]+player.img.get_height()/2 > self.position[1]+self.img_height/2:
            self.position = (self.position[0], self.position[1]+self.vel)
            self.rect.y += self.vel
        if player.position[1]+player.img.get_height()/2 < self.position[1]+self.img_height/2:
            self.position = (self.position[0], self.position[1]-self.vel)
            self.rect.y -= self.vel

    def drawMonster(self, screen):
        self.index += self.changeValue
        if self.direction:
            if self.index >= 7-self.vel or self.index <= 0:
                screen.blit(self.img_right[1], monster.position)
                self.changeValue *= -1
            else:
                screen.blit(self.img_right[0], monster.position)
        else:
            if self.index >= 7-self.vel or self.index <= 0:
                screen.blit(self.img_left[1], monster.position)
                self.changeValue *= -1
            else:
                screen.blit(self.img_left[0], monster.position)
        
class Player():

    def __init__(self, position, img):
        self.position = position
        self.img = img
        self.rect = pygame.Rect(position[0], position[1], img.get_width(), img.get_height())
        self.grau = 0
        self.passo = 1
        self.vel = 7
        self.life = 3
        self.heartText = pygame.font.SysFont('arial', 30).render("Life: ", True, (0, 0, 0))
        self.heartImage = pygame.image.load('sprites_player/heart.png')
        self.ammo = 10
        self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo: " + str(self.ammo), True, (0, 0, 0))
        self.score = 0
        self.scoreText = pygame.font.SysFont('arial', 30).render("Score: " + str(self.score), True, (0, 0, 0))
  
    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def moveUp(self):
        if self.position[1] > 0:
            self.setPosition((self.position[0], self.position[1]-self.vel))
            self.rect.y -= self.vel
        
    def moveDown(self):
        if self.position[1] < SCREEN_HEIGHT - self.img.get_height():
            self.setPosition((self.position[0], self.position[1]+self.vel))
            self.rect.y += self.vel

    def moveRight(self):
        if self.position[0] < SCREEN_WIDTH - self.img.get_width():
            self.setPosition((self.position[0]+self.vel, self.position[1]))
            self.rect.x += self.vel

    def moveLeft(self):
        if self.position[0] > 0:
            self.setPosition((self.position[0]-self.vel, self.position[1]))
            self.rect.x -= self.vel

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def damagePlayer(self, amount):
        self.life -= amount

    def isPlayerDead(self):
        return self.life <= 0

    def showLife(self, screen):
        screen.blit(self.heartText, (7, 7))
        for i in range(1, self.life+1):
            screen.blit(self.heartImage, (20 + 40*i, 10))

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            if player1.grau == 0:
                shots.append(Shot((self.position[0]+40, self.position[1]), 'y', -1))
            elif player1.grau == 180:
                shots.append(Shot((self.position[0]+20, self.position[1]+40), 'y',  1)) 
            elif player1.grau == 90:
                shots.append(Shot((self.position[0]+40, self.position[1]+40), 'x',  1))
            else:
                shots.append(Shot((self.position[0], self.position[1]+20), 'x', -1))
            self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo: " + str(self.ammo), True, (0, 0, 0))

    def showAmmoAmount(self, screen):
        screen.blit(self.ammoText, (7, 50))

    def addScore(self, amount):
        self.score += amount
        self.scoreText = pygame.font.SysFont('arial', 30).render("Score: " + str(self.score), True, (0, 0, 0))

    def showScore(self, screen):
        screen.blit(self.scoreText, (850 , 7))
        
class Shot():

    def __init__(self, position, eixo, vel):
        self.position = position
        self.eixo = eixo
        if eixo == 'x':
            self.img = pygame.image.load('sprites_player/shotX.png')
        else:
            self.img = pygame.image.load('sprites_player/shotY.png')
        
        self.rect = pygame.Rect(position[0], position[1], self.img.get_width(), self.img.get_height())
        self.vel = vel * 30

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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

img_player = pygame.image.load('sprites_player/sprite1_player_0.png')
player1 = Player((500-70/2, 350-70/2), img_player)

monsters = []

poring_right_image = [pygame.image.load('sprites_monsters/poring_right.png'), pygame.image.load('sprites_monsters/poring_right2.png')]
poring_left_image = [pygame.image.load('sprites_monsters/poring_left.png'), pygame.image.load('sprites_monsters/poring_left2.png')]

for i in range(2):
    monsters.append(Monster((rd.randint(-50, -30), rd.randint(30, 670)), poring_right_image, poring_left_image))
    monsters.append(Monster((rd.randint(30, 970), rd.randint(-50, -30)), poring_right_image, poring_left_image))
    monsters.append(Monster((rd.randint(1030, 1050), rd.randint(30, 670)), poring_right_image, poring_left_image))
    monsters.append(Monster((rd.randint(30, 970), rd.randint(730, 750)), poring_right_image, poring_left_image))

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
                player1.shoot()

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
        if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
            shots.remove(shot)
        elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
            shots.remove(shot)
    
    for monster in monsters:
        monster.move(player1)
        monster.drawMonster(screen)
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
                player1.addScore(100)

    if len(monsters) == 0 and inGame:
        win = True
        inGame = False
                    
    screen.blit(player1.img, player1.position)
    player1.showLife(screen)
    player1.showScore(screen)
    player1.showAmmoAmount(screen)
    
    pygame.display.update()

if win:
    screen.blit(pygame.image.load('you_win.jpg'), (0, 0))
else: 
    screen.blit(pygame.image.load('game_over.png'), (0, 0))
pygame.display.update()
