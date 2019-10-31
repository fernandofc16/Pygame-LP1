import pygame

class Images():

    def __init__(self):
        self.poring = [[pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)],
                       [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]]

        self.angeling = [[pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)],
                         [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]]

        self.hamburguer = [[pygame.transform.scale(pygame.image.load('sprites_monsters/Hamburguer/frame_' + str(i) + '_delay-0.12s.png'), (50, 50)) for i in range(1,8)],
                           [pygame.transform.scale(pygame.image.load('sprites_monsters/Hamburguer/frame_' + str(i) + '_delay-0.12s.png'), (50, 50)) for i in range(1,8)]]

        self.kikat = [[pygame.transform.scale(pygame.image.load('sprites_monsters/kitkat/frame_' + str(i) + '_delay-0.12s.png'), (50, 50)) for i in range(4)],
                      [pygame.transform.scale(pygame.image.load('sprites_monsters/kitkat/frame_' + str(i) + '_delay-0.12s.png'), (50, 50)) for i in range(4)]]

        self.nutella = [[pygame.transform.scale(pygame.image.load('sprites_monsters/Nutella/frame_' + str(i) + '_delay-0.3s.png'), (50, 50)) for i in range(2)],
                      [pygame.transform.scale(pygame.image.load('sprites_monsters/Nutella/frame_' + str(i) + '_delay-0.3s.png'), (50, 50)) for i in range(2)]]

        self.ervilha = [[pygame.transform.scale(pygame.image.load('sprites_allies/Ervilha/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,17)],
                      [pygame.transform.scale(pygame.image.load('sprites_allies/Ervilha/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,17)]]

        self.laranja = [[pygame.transform.scale(pygame.image.load('sprites_allies/Laranja/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,12)],
                      [pygame.transform.scale(pygame.image.load('sprites_allies/Laranja/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,12)]]

        self.melancia = [[pygame.transform.scale(pygame.image.load('sprites_allies/Melancia/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,14)],
                      [pygame.transform.scale(pygame.image.load('sprites_allies/Melancia/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,14)]]

        self.tomate = [[pygame.transform.scale(pygame.image.load('sprites_allies/Tomate/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,14)],
                      [pygame.transform.scale(pygame.image.load('sprites_allies/Tomate/frame_' + str(i) + '_delay-0.07s.png'), (50, 50)) for i in range(2,14)]]
        
    def getPoringImages(self):
        return self.poring
    
    def getKikats(self):
        return self.kikat

    def getHamburguers(self):
        return self.hamburguer

    def getNutellas(self):
        return self.nutella

    def getErvilhas(self):
        return self.ervilha

    def getLaranjas(self):
        return self.laranja

    def getMelancias(self):
        return self.melancia

    def getTomates(self):
        return self.tomate

    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
