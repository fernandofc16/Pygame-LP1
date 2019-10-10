import pygame

class Images():

    def __init__(self):
        self.hamburguer = [[pygame.image.load('sprites_monsters/hamburguer/right/frame_' + str(i) + '_delay-0.12s.png') for i in range(1, 8)],
                           [pygame.image.load('sprites_monsters/hamburguer/left/frame_' + str(i) + '_delay-0.12s.png') for i in range(1, 8)]]
        
        self.poring = [[pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)],
                       [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]]

        self.angeling = [[pygame.image.load('sprites_allies/angeling/right/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)],
                         [pygame.image.load('sprites_allies/angeling/left/frame_' + str(i) + '_delay-0.15s.png') for i in range(27)]]


    def getPoringImages(self):
        return self.poring

    def getAngelingImages(self):
        return self.angeling

    def getHamburguerImages(self):
        return self.changeImagesSize(self.hamburguer, (80, 80))

    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
