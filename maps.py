import pygame
import time
import math
import random as rd
import Ranking
from monsters import Monster
from players import Player
from images_handler import Images
from bullets import Bullet

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Map():

    def __init__(self):
        self.monsters = []
        self.allies = []
        self.bullets = []
        self.level = 1
        self.quant = 1
        self.player = Player((500-70/2, 350-70/2), pygame.image.load('sprites_player/sprite1_player_0.png'))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images = Images()
        self.bossTime = True
        self.inGame = True
        self.win = False
        self.windowClosed = False
        self.initialScreen = True
        self.showGuiLevel = True
        self.ranking = []
        self.setRank = True
        self.start_time = time.time()
        self.backgroundIndex = 0
        self.winBackgroundImage = pygame.image.load('background_images/you_win.jpg')
        self.gameOverBackgroundImage = pygame.image.load('background_images/game_over.jpg')
        self.initialBackgroundImage = pygame.image.load('background_images/inicial.png')
        self.backgrounds = [pygame.image.load('background_images/floresta.png').convert_alpha(), pygame.image.load('background_images/floresta_escura.png').convert_alpha(),
                            pygame.image.load('background_images/oceano.png').convert_alpha(), pygame.image.load('background_images/deserto.png').convert_alpha(),
                            pygame.image.load('background_images/metal.png').convert_alpha(), pygame.image.load('background_images/lava.png').convert_alpha(),
                            pygame.image.load('background_images/rocha.png').convert_alpha()]

    def spawnMonsters(self, amount, game_map, life, isBoss):
        for i in range(amount):
            randmonster = rd.randint(1,3)
            if randmonster == 1:
                image = game_map.images.getHamburguers()
            elif randmonster == 2:
                image = game_map.images.getKikats()
            elif randmonster == 3:
                image = game_map.images.getNutellas()
                
            #monsters spawn at left side
            self.monsters.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at top side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life, isBoss))
            #monsters spawn at right side
            self.monsters.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at bot side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life, isBoss))

    def spawnBoss(self):
        self.spawnMonsters(1, self, self.level*3, True)
        for i in range(3):
            del self.monsters[rd.randint(0, len(self.monsters)-1)]
        self.monsters[0].changeMonsterVelocity(3)

    def spawnAllies(self, amount, game_map, life):
        for i in range(amount):
            randallies = rd.randint(1,3)
            if randallies == 1:
                image = game_map.images.getErvilhas()
            elif randallies == 2:
                image = game_map.images.getLaranjas()
            elif randallies == 3:
                image = game_map.images.getMelancias()
            elif randallies == 4:
                image = game_map.images.getTomates()
            #allies spawn at left side
            self.allies.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life, False))
            #allies spawn at top side
            self.allies.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life, False))
            #allies spawn at right side
            self.allies.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life, False))
            #allies spawn at bot side
            self.allies.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life, False))

    def spawnBullets(self, amount):
        for i in range(amount):
            self.bullets.append(Bullet())

    def showPlayerInfos(self):
        #pygame.draw.rect(screen, (0, 0, 0), player1.rect) #debug
        self.screen.blit(self.player.img, self.player.position)
        self.player.showLife(self.screen)
        self.player.showScore(self.screen)
        self.player.showAmmoAmount(self.screen)

    def showLevelGUI(self):
        if self.level < 10:
            self.screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(300), SCREEN_HEIGHT/2-150))
        else:
            self.screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(380), SCREEN_HEIGHT/2-150))

    def changeLevel(self):
        self.level += 1
        if self.level <= 35:
            self.backgroundIndex = 0
        if self.level % 3 == 0:
            self.quant += 1
        if (self.quant-1)%5 == 0:
            self.quant = 1
            self.bossTime = True
        #player1.addAmmo(self.level*4+4)
        self.spawnMonsters(self.quant, self, 1, False)
            
        self.spawnAllies(self.quant, self, 1)

        self.showGuiLevel = True
        self.start_time = time.time()

    def blitBackgroundMap(self):
        self.screen.blit(self.backgrounds[self.backgroundIndex], (-13, -30))

    def alliesInteractions(self):
        for allie in self.allies:
            allie.move(self.player)
            allie.drawMonster(self.screen)
            if self.player.is_collided_with(allie):
                allie.healAudio.play()
                self.player.healPlayer(1)
                self.allies.remove(allie)
            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(allie):
                        allie.damageMonster(1)
                        if allie.isDead():
                            self.allies.remove(allie)
                            self.player.addScore(-500)
                        self.player.shots.remove(shot)

    def monstersInteractions(self):
        for monster in self.monsters:
            monster.move(self.player)
            monster.drawMonster(self.screen)
            if self.player.is_collided_with(monster):
                monster.damageAudio.play()
                if monster.isBoss:
                    self.player.damagePlayer(5)
                else:
                    self.player.damagePlayer(1)
                self.monsters.remove(monster)
                if(self.player.isPlayerDead()):
                    self.inGame = False
            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(monster):
                        monster.damageMonster(1)
                        if monster.isDead():
                            self.monsters.remove(monster)
                            self.player.addScore(100)
                        self.player.shots.remove(shot)

    def bulletsInteractions(self):
        for bullet in self.bullets:
            self.screen.blit(bullet.img, bullet.position)
            if self.player.is_collided_with(bullet):
                bullet.reloadAudio.play()
                self.player.addAmmo(5)
                self.bullets.remove(bullet)
                if len(self.bullets) == 0:
                    self.player.canSpawnBullets = True

    def shotsInteractions(self):
        for shot in self.player.shots:
            shot.move()
            self.screen.blit(shot.img, shot.position)
            if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
                self.player.shots.remove(shot)
            elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
                self.player.shots.remove(shot)

    def checkEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.grau = 0
            self.player.moveUp()
            self.player.passo += 1
        elif keys[pygame.K_DOWN]:
            self.player.grau = 180
            self.player.moveDown()
            self.player.passo += 1
        elif keys[pygame.K_RIGHT]:
            self.player.grau = 90
            self.player.moveRight()
            self.player.passo += 1
        elif keys[pygame.K_LEFT]:
            self.player.grau = 270
            self.player.moveLeft()
            self.player.passo += 1
        elif keys[pygame.K_q]:
            print('Q PRESSED')
            for m in self.monsters:
                self.monsters.remove(m)
                self.player.addScore(200)
            for a in self.allies:
                self.allies.remove(a)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)

    def checkEndOfLevel(self):
        if len(self.monsters) == 0 and len(self.allies) == 0 and self.inGame:
            if self.level%5 == 0 and self.bossTime:
                self.spawnBoss()
                self.bossTime = False
            else:
                self.changeLevel()

    def showGuiLevelMap(self):
        if self.showGuiLevel:
            if time.time() - self.start_time > 2.2:
                self.showGuiLevel = False
            self.showLevelGUI()

    def endOfGame(self):
        if self.win:
            self.screen.blit(self.winBackgroundImage, (0, 0))
        else: 
            self.screen.blit(self.gameOverBackgroundImage, (0, 0))

        if self.setRank:    
            Ranking.SetRank(self.player.score, self.level, Ranking.GetUsername())
            Ranking.LoadRanking()
            self.ranking = Ranking.GetRanking()
            self.setRank = False

        count = 1
        for score in self.ranking:
            self.screen.blit(pygame.font.SysFont('arial', 45).render(str(count) + ". " + score[1] + " Level: " + score[2] + " Score: " + score[3] , True, (255, 255, 255)), (50, 170 + (70*count)))
            count += 1
            if count > 5: break

        pygame.display.update()

    def initalScreen(self):
        self.screen.blit(self.initialBackgroundImage, (0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 410 and pos[0] <= 630 and pos[1] >= 625 and pos[1] <= 690):
                    self.initialScreen = False
