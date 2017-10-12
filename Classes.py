import pygame
import math
import random as rd
import time

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Monster():

    def __init__(self, position, img_left, img_right, life):
        self.position = position
        self.img_left = img_left
        self.img_right = img_right
        self.img_width = img_right[0].get_width()
        self.img_height = img_right[0].get_height()
        self.rect = pygame.Rect(position[0]+5, position[1]+5, self.img_width-10, self.img_height-10)
        self.vel = rd.randint(1, 4)
        self.direction = 1
        self.index = rd.randint(0, len(img_right)-1)
        self.animationFrames = len(img_right)
        self.life = life

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
        #pygame.draw.rect(screen, (0, 0, 0), self.rect) #debug
        if self.direction:
            screen.blit(self.img_right[self.index], self.position)
        else:
            screen.blit(self.img_left[self.index], self.position)
        self.index += 1
        if self.index == self.animationFrames:
            self.index = 0

    def damageMonster(self, amount):
        self.life -= amount

    def isDead(self):
        if self.life <= 0:
            return True
        return False
        
class Player():

    def __init__(self, position, img):
        self.position = position
        self.img = img
        self.rect = pygame.Rect(position[0]+8, position[1]+5, img.get_width()-16, img.get_height()-10)
        self.grau = 0
        self.passo = 1
        self.vel = 7
        self.life = 5
        self.heartText = pygame.font.SysFont('arial', 30).render("Life: ", True, (0, 0, 0))
        self.heartImage = pygame.image.load('sprites_player/heart.png')
        self.shots = []
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

    def healPlayer(self, amount):
        if self.life < 5:
            self.life += amount
        else:
            self.addScore(1000)

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
                self.shots.append(Shot((self.position[0]+40, self.position[1]), 'y', -1))
            elif player1.grau == 180:
                self.shots.append(Shot((self.position[0]+20, self.position[1]+40), 'y',  1)) 
            elif player1.grau == 90:
                self.shots.append(Shot((self.position[0]+40, self.position[1]+40), 'x',  1))
            else:
                self.shots.append(Shot((self.position[0], self.position[1]+20), 'x', -1))
            self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo: " + str(self.ammo), True, (0, 0, 0))

    def showAmmoAmount(self, screen):
        screen.blit(self.ammoText, (7, 50))

    def addAmmo(self, amount):
        self.ammo += amount
        self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo: " + str(self.ammo), True, (0, 0, 0))

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

class Map():

    def __init__(self):
        self.monsters = []
        self.allies = []
        self.level = 1
        self.showGuiLevel = True
        self.start_time = time.time()

    def spawnMonsters(self, amount, right_image, left_image, life):
        for i in range(amount):
            #monsters spawn at left side
            self.monsters.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), right_image, left_image, life))
            #monsters spawn at top side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), right_image, left_image, life))
            #monsters spawn at right side
            self.monsters.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), right_image, left_image, life))
            #monsters spawn at bot side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), right_image, left_image, life))

    def spawnAllies(self, amount, right_image, left_image, life):
        for i in range(amount):
            side = rd.randint(1, 4)
            if side == 1:
                #allies spawn at left side
                self.allies.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), right_image, left_image, life))
            elif side == 2:
                #allies spawn at top side
                self.allies.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), right_image, left_image, life))
            elif side == 3:
                #allies spawn at right side
                self.allies.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), right_image, left_image, life))
            elif side == 4:
                #allies spawn at bot side
                self.allies.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), right_image, left_image, life))

    def showLevelGUI(self):
        screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-300, SCREEN_HEIGHT/2-150))

    def changeLevel(self):
        self.level += 1
        player1.addAmmo(self.level*4+4)
        self.spawnMonsters(game_map.level, poring_right_image, poring_left_image, 1)
        if rd.random() > 0.65:
            self.spawnAllies(1, angeling_right_images, angeling_left_images, 1)
        self.showGuiLevel = True
        self.start_time = time.time()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

game_map = Map()

poring_right_image = [pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
poring_left_image = [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]

angeling_right_images = [pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]
angeling_left_images = [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]

game_map.spawnAllies(1, angeling_right_images, angeling_left_images, 1)
game_map.spawnMonsters(1, poring_right_image, poring_left_image, 1)

img_player = pygame.image.load('sprites_player/sprite1_player_0.png')
player1 = Player((500-70/2, 350-70/2), img_player)

inGame = True
win = False

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

    for shot in player1.shots:
        shot.move()
        screen.blit(shot.img, shot.position)
        if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
            player1.shots.remove(shot)
        elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
            player1.shots.remove(shot)
    
    for monster in game_map.monsters:
        monster.move(player1)
        monster.drawMonster(screen)
        if player1.is_collided_with(monster):
            player1.damagePlayer(1)
            game_map.monsters.remove(monster)
            if(player1.isPlayerDead()):
                inGame = False
        else:
            for shot in player1.shots:
                if shot.is_collided_with(monster):
                    monster.damageMonster(1)
                    if monster.isDead():
                        game_map.monsters.remove(monster)
                        player1.addScore(100)
                    player1.shots.remove(shot)
                    

    for allie in game_map.allies:
        allie.move(player1)
        allie.drawMonster(screen)
        if player1.is_collided_with(allie):
            player1.healPlayer(1)
            game_map.allies.remove(allie)
        else:
            for shot in player1.shots:
                if shot.is_collided_with(allie):
                    allie.damageMonster(1)
                    if allie.isDead():
                        game_map.allies.remove(allie)
                        player1.addScore(-500)
                    player1.shots.remove(shot)
                    
    if len(game_map.monsters) == 0 and len(game_map.allies) == 0 and inGame:
        game_map.changeLevel()

    #pygame.draw.rect(screen, (0, 0, 0), player1.rect) #debug
    screen.blit(player1.img, player1.position)
    player1.showLife(screen)
    player1.showScore(screen)
    player1.showAmmoAmount(screen)

    if game_map.showGuiLevel:
        if time.time() - game_map.start_time > 1:
            game_map.showGuiLevel = False
        game_map.showLevelGUI()

    pygame.display.update()

if win:
    screen.blit(pygame.image.load('background_images/you_win.jpg'), (0, 0))
else: 
    screen.blit(pygame.image.load('background_images/game_over.png'), (0, 0))
    
pygame.display.update()
