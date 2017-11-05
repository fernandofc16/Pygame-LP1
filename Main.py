import Ranking
import pygame
import time
from maps import Map

Ranking.SetUsername()

pygame.init()

game_map = Map()

##poring_right_image = [pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##poring_left_image = [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]
##
##angeling_right_images = [pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]
##angeling_left_images = [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]

game_map.spawnAllies(1, game_map.images.getAngelingImages(), 1)
game_map.spawnMonsters(1, game_map.images.getPoringImages(), 1, False)

#image = pygame.image.load('sprites_player/sprite' + str(player1.passo) + '_player_' + str(player1.grau) + '.png')


while game_map.inGame:
    pygame.time.Clock().tick(30)
    game_map.screen.fill((255, 255, 255))

    game_map.blitBackgroundMap()    

    game_map.checkEvents()
    
    game_map.player.animatePlayerSprite()

    game_map.shotsInteractions()

    game_map.bulletsInteractions()
    
    game_map.monstersInteractions()
                    
    game_map.alliesInteractions()
                    
    game_map.checkEndOfLevel()

    game_map.showPlayerInfos()

    game_map.showGuiLevelMap()

    pygame.display.update()

if game_map.win:
    game_map.screen.blit(pygame.image.load('background_images/you_win.jpg'), (0, 0))
else: 
    game_map.screen.blit(pygame.image.load('background_images/game_over.png'), (0, 0))
    
pygame.display.update()
Ranking.SetRank(game_map.player.score,game_map.level,Ranking.GetUsername())

Ranking.ShowRanking()
