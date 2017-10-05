import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong")

#Criando as duas barras e a área do jogo
back = pygame.Surface((640,480))#suface princpal
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
#criando a bolinha
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(8,8),8)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

#definições iniciais
bar1_x, bar2_x = 10. , 620. #posicionando as barras na posição de cada lado
bar1_y, bar2_y = 215. , 215. #posicionando as barras no centro da tela
circle_x, circle_y = 307.5, 232.5 #posição incial da bola
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250. #velocidades de movimento da bola, e das barras
bar1_score, bar2_score = 0,0 #pontuação inicial

#clock and font do placar
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

#game loop
while True:
    
	#capturando os iptus do usuário
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        #verificando se foi pressinada alguma tecla
        if event.type == KEYDOWN:
            #se for pressionada a tecla para cima, o movimento é invertido para que a barra suba
            if event.key == K_UP:
                bar1_move = -ai_speed
            #caso contrário o movimento é setado para baixo
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        #se a tecla for levantada os movimentos são 0 e a barra para de correr
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.

    #renderizando as fontes do placar
    score1 = font.render(str(bar1_score), True,(255,255,255))
    score2 = font.render(str(bar2_score), True,(255,255,255))

    
    screen.blit(background,(0,0))

    #desenhando a área do jogo
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    #linha central
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))

    #blitando as barras
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    #blitando a bolinha
    screen.blit(circle,(circle_x,circle_y))
    #blitando o placar
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))

    bar1_y += bar1_move
    
# movimenando a bolinha
    #configurando a velocidade da bolinha de acordo com o tempo
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    #movimento no eixo x
    circle_x += speed_x * time_sec
    #movimento no wixo y
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec

#Inteligencia de movimento da barra do computador
    #neste caso é bem simples, pois a barra do computador se movimenta de acordo com a direcção da velocidade da bolinha
    #desta forma a barra do computador sempre irá na mesma direção do movimento da bolinha
    #
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if  bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5

    #a barra só nao pode ultrapassar os limites do campo de jogo, nem "correr" atras da bolinha
    if bar1_y >= 420.: bar1_y = 420.
    elif bar1_y <= 10. : bar1_y = 10.
    if bar2_y >= 420.: bar2_y = 420.
    elif bar2_y <= 10.: bar2_y = 10.
    
#regras para a identificar a colisão da bolinha com as barras ou a área de jogo
#depois que a bolinha colide com algo a velocidade da bolinha é invertida
    # se a bolinha colidiu com as barrinhas a velocidade no eixo X é invertida para que ela vá
    # para o outro campo
    #se colidir com a parte superior ou inferior a velocidade do eixo Y é alterada para subir ou descer
    #como a velocidade de movimento é igual nos dois eixos, a colisão faz a bolinha mudar de direção
    #conforme um angulo de 90º
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y,bar_2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

#ultimo passo do game Loop, após todos os calculos a tela precisa ser atualizada
#atualizando a tela
    pygame.display.update()
