import pygame
import time
import Ranking
from maps import Map

Ranking.SetUsername()

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.mixer.music.load('audio/background_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

game_map = Map()

##poring_right_image = [pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##poring_left_image = [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##
##angeling_right_images = [pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]
##angeling_left_images = [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]

game_map.spawnAllies(1, game_map, 1)
game_map.spawnMonsters(2, game_map, 1, False)

#game_map.changeLevel()

#image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.png')


while not game_map.windowClosed:
    pygame.time.Clock().tick(30)
    game_map.screen.fill((255, 255, 255))

    if game_map.initialScreen:
        game_map.initalScreen()
    elif game_map.inGame:
        game_map.blitBackgroundMap()    
        
        game_map.player.animatePlayerSprite()

        game_map.shotsInteractions()

        game_map.bulletsInteractions()
        
        game_map.monstersInteractions()
                        
        game_map.alliesInteractions()
                        
        game_map.checkEndOfLevel()

        game_map.showPlayerInfos()

        game_map.showGuiLevelMap()

        pygame.display.update()
    else:
        game_map.endOfGame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_map.inGame = False
                game_map.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 380 and pos[0] <= 600 and pos[1] >= 630 and pos[1] <= 690):
                    game_map = Map()
                    game_map.spawnAllies(1, game_map, 1)
                    game_map.spawnMonsters(1, game_map, 1, False)

    game_map.checkEvents()

    
