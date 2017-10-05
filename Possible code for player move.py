if event.key == pygame.K_UP:
                if player1.grau == 0:
                    player1.setPosition((player1.position[0], player1.position[1]-10))
                elif player1.grau == 90:
                    player1.setPosition((player1.position[0]+10, player1.position[1]))
                elif player1.grau == 180:
                    player1.setPosition((player1.position[0], player1.position[1]+10))
                elif player1.grau == 270:
                    player1.setPosition((player1.position[0]-10, player1.position[1]))
                player1.passo += 1
            elif event.key == pygame.K_DOWN:
                if player1.grau == 0:
                    player1.setPosition((player1.position[0], player1.position[1]+10))
                elif player1.grau == 90:
                    player1.setPosition((player1.position[0]-10, player1.position[1]))
                elif player1.grau == 180:
                    player1.setPosition((player1.position[0], player1.position[1]-10))
                elif player1.grau == 270:
                    player1.setPosition((player1.position[0]+10, player1.position[1]))
                player1.passo -= 1
            elif event.key == pygame.K_RIGHT:
                #player1.setPosition((player1.position[0]+10, player1.position[1]))
                player1.grau += 90
            elif event.key == pygame.K_LEFT:
                #player1.setPosition((player1.position[0]-10, player1.position[1]))
                player1.grau -= 90
