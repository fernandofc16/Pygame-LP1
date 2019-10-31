import pygame

class Shot():

    def __init__(self, position, eixo, vel):
        self.position = position
        self.eixo = eixo
        if eixo == 'x':
            self.img = pygame.transform.scale(pygame.image.load('sprites_player/rock_shoot.png'), (12,12))
        else:
            self.img = pygame.transform.scale(pygame.image.load('sprites_player/rock_shoot.png'), (12,12))
        
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
