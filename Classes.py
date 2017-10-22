import pygame
import math
import random as rd
import time

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Images():

    def __init__(self):
        self.poring = [[pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)],
                       [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]]

        self.angeling = [[pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)],
                         [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]]

        self.aquaring = [[pygame.transform.scale(pygame.image.load('sprites_monsters/aquaring/right/frame_' + str(i) + '_delay-0.1s.png'), (50, 50)) for i in range(9)],
                         [pygame.transform.scale(pygame.image.load('sprites_monsters/aquaring/left/frame_' + str(i) + '_delay-0.1s.png'), (50, 50)) for i in range(9)]]
        
        self.poporing = [[pygame.transform.scale(pygame.image.load('sprites_monsters/poporing/right/frame_' + str(i) + '_delay-0.1s.png'), (40, 40)) for i in range(4)],
                         [pygame.transform.scale(pygame.image.load('sprites_monsters/poporing/left/frame_' + str(i) + '_delay-0.1s.png'), (40, 40)) for i in range(4)]]

        self.stapo = [[pygame.transform.scale(pygame.image.load('sprites_monsters/stapo/right/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(13)],
                      [pygame.transform.scale(pygame.image.load('sprites_monsters/stapo/left/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(13)]]

        self.metalling = [[pygame.transform.scale(pygame.image.load('sprites_monsters/metalling/right/frame_' + str(i) + '_delay-0.09s.png'), (50, 50)) for i in range(4)],
                          [pygame.transform.scale(pygame.image.load('sprites_monsters/metalling/left/frame_' + str(i) + '_delay-0.09s.png'), (50, 50)) for i in range(4)]]

        self.magmaring = [[pygame.transform.scale(pygame.image.load('sprites_monsters/magmaring/right/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(5)],
                          [pygame.transform.scale(pygame.image.load('sprites_monsters/magmaring/left/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(5)]]

        self.develing = [[pygame.transform.scale(pygame.image.load('sprites_monsters/develing/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)],
                         [pygame.transform.scale(pygame.image.load('sprites_monsters/develing/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)]]

    def getPoringImages(self):
        return self.poring

    def getAngelingImages(self):
        return self.angeling

    def getAquaringImages(self):
        return self.aquaring

    def getPoporingImages(self):
        return self.poporing

    def getStapoImages(self):
        return self.stapo

    def getMetallingImages(self):
        return self.metalling

    def getMagmaringImages(self):
        return self.magmaring

    def getDevelingImages(self):
        return self.develing

class Monster():

    def __init__(self, position, img, life):
        self.position = position
        self.img_left = img[0]
        self.img_right = img[1]
        self.img_width = self.img_right[0].get_width()
        self.img_height = self.img_right[0].get_height()
        self.rect = pygame.Rect(position[0]+5, position[1]+5, self.img_width-10, self.img_height-10)
        self.vel = rd.randint(1, 4)
        self.direction = 1
        self.index = rd.randint(0, len(self.img_right)-1)
        self.animationFrames = len(self.img_right)
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

class Bullets():

    def __init__(self):
        self.position = (rd.randint(0, SCREEN_WIDTH-30), rd.randint(0, SCREEN_HEIGHT-30))
        self.img = pygame.image.load('sprites_player/bullets.png')
        self.rect = pygame.Rect(self.position[0], self.position[1], self.img.get_width(), self.img.get_height())
        
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
        self.ammoImage = pygame.image.load('sprites_player/ammo_amount.png')
        self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo:", True, (0, 0, 0))
        self.canSpawnBullets = True
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

    def shoot(self, game_map):
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
            if self.ammo == 0 and self.canSpawnBullets:
                game_map.spawnBullets(2)
                self.canSpawnBullets = False

    def showAmmoAmount(self, screen):
        screen.blit(self.ammoText, (7, 50))
        for i in range(self.ammo):
            screen.blit(self.ammoImage, (60 + (20*i), 50))

    def addAmmo(self, amount):
        self.ammo += amount

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
        self.bullets = []
        self.level = 1
        self.quant = 1
        self.showGuiLevel = True
        self.start_time = time.time()
        self.backgroundIndex = 0
        self.backgrounds = [pygame.image.load('background_images/floresta.png'), pygame.image.load('background_images/floresta_escura.png'),
                            pygame.image.load('background_images/oceano.png'), pygame.image.load('background_images/deserto.png'),
                            pygame.image.load('background_images/metal.png'), pygame.image.load('background_images/lava.png'),
                            pygame.image.load('background_images/rocha.png')]

    def spawnMonsters(self, amount, image, life):
        for i in range(amount):
            #monsters spawn at left side
            self.monsters.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life))
            #monsters spawn at top side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life))
            #monsters spawn at right side
            self.monsters.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life))
            #monsters spawn at bot side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life))

    def spawnAllies(self, amount, image, life):
        for i in range(amount):
            side = rd.randint(1, 4)
            if side == 1:
                #allies spawn at left side
                self.allies.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life))
            elif side == 2:
                #allies spawn at top side
                self.allies.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life))
            elif side == 3:
                #allies spawn at right side
                self.allies.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life))
            elif side == 4:
                #allies spawn at bot side
                self.allies.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life))

    def spawnBullets(self, amount):
        for i in range(amount):
            self.bullets.append(Bullets())
        

    def showLevelGUI(self):
        if self.level < 10:
            screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(300), SCREEN_HEIGHT/2-150))
        else:
            screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(380), SCREEN_HEIGHT/2-150))

    def changeLevel(self):
        self.level += 1
        if self.level <= 35:
            self.backgroundIndex = math.floor(self.level/5-0.1)
        self.quant += 1
        if (self.quant-1)%5 == 0:
            self.quant = 1
        #player1.addAmmo(self.level*4+4)
        if self.level <= 5:
            self.spawnMonsters(self.quant, images.getPoringImages(), 1)
        elif self.level <= 10:
            self.spawnMonsters(self.quant, images.getPoporingImages(), 2)
        elif self.level <= 15:
            self.spawnMonsters(self.quant, images.getAquaringImages(), 3)
        elif self.level <= 20:
            self.spawnMonsters(self.quant, images.getStapoImages(), 4)
        elif self.level <= 25:
            self.spawnMonsters(self.quant, images.getMetallingImages(), 5)
        elif self.level <= 30:
            self.spawnMonsters(self.quant, images.getMagmaringImages(), 5)
        elif self.level > 30:
            self.spawnMonsters(self.quant, images.getDevelingImages(), 6)
            
        if rd.random() > 0.65:
            self.spawnAllies(1, images.getAngelingImages(), 1)

        self.showGuiLevel = True
        self.start_time = time.time()

    def blitBackgroundMap(self, screen):
        screen.blit(self.backgrounds[self.backgroundIndex], (-13, -30))
        

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

game_map = Map()
images = Images()

##poring_right_image = [pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##poring_left_image = [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##
##angeling_right_images = [pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]
##angeling_left_images = [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]

game_map.spawnAllies(1, images.getAngelingImages(), 1)
game_map.spawnMonsters(1, images.getPoringImages(), 1)

img_player = pygame.image.load('sprites_player/sprite1_player_0.png')
player1 = Player((500-70/2, 350-70/2), img_player)

inGame = True
win = False

image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.png')

while inGame:
    pygame.time.Clock().tick(60)
    screen.fill((255, 255, 255))
    game_map.blitBackgroundMap(screen)

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
    elif keys[pygame.K_q]:
        print('Q PRESSED')
        for m in game_map.monsters:
            game_map.monsters.remove(m)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.shoot(game_map)

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

    for bullet in game_map.bullets:
        screen.blit(bullet.img, bullet.position)
        if player1.is_collided_with(bullet):
            player1.addAmmo(5)
            game_map.bullets.remove(bullet)
            if len(game_map.bullets) == 0:
                player1.canSpawnBullets = True
    
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
