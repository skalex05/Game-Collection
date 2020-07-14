import os
import time
import sys
import pygame
import time
import random
from pygame.locals import *
pygame.init()

path = os.path.dirname("My gamecollection")
size = width,height = 500,500

smallfont = pygame.font.SysFont("Arial",15)
medfont = pygame.font.SysFont("Arial",40)
largefont = pygame.font.SysFont("Arial",60)

def wait(x):
    ct = time.time()
    nt = time.time()
    waiting = True
    while (nt - ct) < x:
        nt = time.time()
    waiting = False
    

def play_snake():
    screen = pygame.display.set_mode(size)
    score = 0
    run = True
    snake = []
    wait(1)
    def Die():
        screen.fill((0,0,0))
        screen.blit(largefont.render("You died!",True,(255,255,255)),(125,100))
        screen.blit(medfont.render("You've got a score of "+str(score),True,(255,255,255)),(75,150))
        pygame.display.update()
        wait(2)
        return False

    x,y = 20,0
    posx,posy = 60,60
    screen.fill((0,0,0))

    pygame.display.update()
    appletime = 0
    apple = False
    appleposx,appleposy = 10000,10000 
    waiting = False
    
    while run == True:
        if posx <= 50 or posx >= 430:
            run = Die()
        if posy <= 50 or posy >= 430:
            run = Die()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                
            elif event.type == KEYDOWN and event.key == K_w:
                if y != 20:
                    x,y = 0,-20
            elif event.type == KEYDOWN and event.key == K_a:
                if x != 20:
                    x,y = -20,0
            elif event.type == KEYDOWN and event.key == K_s:
                if y != -20:
                    x,y = 0,20
            elif event.type == KEYDOWN and event.key == K_d:
                if x != -20:
                    x,y= 20,0
        if waiting == False:
            screen.fill((0,0,0))
            pygame.draw.rect(screen,(150,150,150),Rect((50,50),(400,10)))
            pygame.draw.rect(screen,(150,150,150),Rect((50,50),(10,400)))
            pygame.draw.rect(screen,(150,150,150),Rect((440,50),(10,400)))
            pygame.draw.rect(screen,(150,150,150),Rect((50,440),(400,10)))
            #scoring
            
            screen.blit(smallfont.render("Score:"+str(score),True,(255,255,255)),(400,10))
            if appletime == 5:
                if apple == False:
                    
                    appleposx,appleposy = 20*random.randint(3,16),20*random.randint(3,16)
                apple = pygame.draw.rect(screen,(255,0,0),Rect((appleposx,appleposy),(20,20)))
            
                    
            snakehead = pygame.draw.rect(screen,(100,100,100),Rect((posx,posy),(20,20)))


            for bit in snake:
                if posx == bit[0] and posy == bit[1]:
                    run = Die()
                    
            for bit in snake:
                pygame.draw.rect(screen,(255,255,255),Rect((bit[0],bit[1]),(20,20)))
            
            if posx == appleposx and posy == appleposy:
                appletime = 0
                apple = False
                score += 1
                snake.append([0,0])

            for i in range(len(snake)-1,0,-1):
                snake[i] = snake[i-1]

            if len(snake) > 0:
                snake[0] = [posx,posy]

            
            posy += y
            posx += x
            if appletime < 5:
                appletime += 1
            pygame.display.update()
            wait(0.1)
    return False

def play_battleship():
    wait(1)
    numberofships = 12
    screen = pygame.display.set_mode((width * 2,height))
    fighting = True
    
    playerships = []
    enemyships = []
    shipplacepos = placex,placey = 45,75

    while len(enemyships) < numberofships:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(100,100,100),Rect((0,0),(490,50)))
        pygame.draw.rect(screen,(100,100,100),Rect((510,0),(490,50)))
        screen.blit(medfont.render("Place your ships!",True,(255,255,255)),(150,0))
        screen.blit(medfont.render("Your Shots:",True,(255,255,255)),(650,0))
        pygame.draw.rect(screen,(0,200,255),Rect((45,75),(400,400)))
        pygame.draw.rect(screen,(0,200,255),Rect((555,75),(400,400)))
        pygame.draw.rect(screen,(255,255,255),Rect((490,0),(20,500)))
        
        enx = 555 + random.randint(0,9) * 40
        eny = 75 + random.randint(0,9) * 40
        found = False
        for ship in enemyships:
            if ship[0] == enx and ship[1] == eny:
                found = True
        if found == False:
            enemyships.append([enx,eny])
            
    while len(playerships) < numberofships:
        shipplacepos = placex,placey
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(100,100,100),Rect((0,0),(490,50)))
        pygame.draw.rect(screen,(100,100,100),Rect((510,0),(490,50)))
        screen.blit(medfont.render("Place your ships!",True,(255,255,255)),(150,0))
        screen.blit(medfont.render("Your Shots:",True,(255,255,255)),(650,0))
        pygame.draw.rect(screen,(0,200,255),Rect((45,75),(400,400)))
        pygame.draw.rect(screen,(0,200,255),Rect((555,75),(400,400)))
        pygame.draw.rect(screen,(255,255,255),Rect((490,0),(20,500)))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN and event.key == K_w:
                if placey > 75:
                    placey -= 40
            elif event.type == KEYDOWN and event.key == K_s:
                if placey < 405:
                    placey += 40
            elif event.type == KEYDOWN and event.key == K_a:
                if placex > 45:
                    placex -= 40
            elif event.type == KEYDOWN and event.key == K_d:
                if placex < 380:
                    placex += 40
            elif event.type == KEYDOWN and event.key == K_RETURN:
                found = False
                for ship in playerships:
                    if ship[0] == placex and ship[1] == placey:
                        found = True
                if found == False:
                    playerships.append([placex,placey])
                    
        pygame.draw.rect(screen,(100,100,100),Rect(shipplacepos,(40,40)))
        for ship in playerships:
            pygame.draw.rect(screen,(100,100,100),Rect((ship[0],ship[1]),(40,40)))

        
        pygame.display.update()
    turn = 1
    playerhits = []
    playermisses = []
    enemyhits = []
    enemymisses = []
    shootpos = shootx,shooty = 555,75
    
    pygame.draw.rect(screen,(100,100,100),Rect((510,0),(490,50)))
    screen.blit(medfont.render("Your Ships",True,(255,255,255)),(650,0))
    while fighting == True:
        pygame.draw.rect(screen,(0,200,255),Rect((555,75),(400,400)))
        pygame.draw.rect(screen,(0,200,255),Rect((45,75),(400,400)))
        for ship in playerships:
            pygame.draw.rect(screen,(100,100,100),Rect((ship[0],ship[1]),(40,40)))
        for miss in playermisses:
            pygame.draw.rect(screen,(0,150,255),Rect((miss[0],miss[1]),(40,40)))
        for hit in playerhits:
            pygame.draw.rect(screen,(150,0,0),Rect((hit[0],hit[1]),(40,40)))
        pygame.display.update()
        for miss in enemymisses:
            pygame.draw.rect(screen,(0,150,255),Rect((miss[0],miss[1]),(40,40)))
        for hit in enemyhits:
            pygame.draw.rect(screen,(150,0,0),Rect((hit[0],hit[1]),(40,40)))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
        wait(0.2)
        if turn == 1:
            turn = 2
            enter = False
            while enter == False:
                shootpos = shootx,shooty
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit()
                    elif event.type == KEYDOWN and event.key == K_w:
                        if shooty > 75:
                            shooty -= 40
                    elif event.type == KEYDOWN and event.key == K_s:
                        if shooty < 405:
                            shooty += 40
                    elif event.type == KEYDOWN and event.key == K_a:
                        if shootx > 555:
                            shootx -= 40
                    elif event.type == KEYDOWN and event.key == K_d:
                        if shootx < 915:
                            shootx += 40
                    elif event.type == KEYDOWN and event.key == K_RETURN:
                        Found = False
                        for miss in playermisses:
                            if miss[0] == shootx and miss[1] == shooty:
                                Found = True
                        for hit in playerhits:
                            if hit[0] == shootx and hit[1] == shooty:
                                Found = True
                        if Found == False:
                            enter = True
                            found = False
                            for ship in enemyships:
                                if ship[0] == shootx and ship[1] == shooty:
                                    found = True
                            if found == False:
                                playermisses.append([shootx,shooty])
                            elif found == True:
                                playerhits.append([shootx,shooty])
                            
                pygame.draw.rect(screen,(0,200,255),Rect((555,75),(400,400)))
                for miss in playermisses:
                    pygame.draw.rect(screen,(0,150,255),Rect((miss[0],miss[1]),(40,40)))
                for hit in playerhits:
                    pygame.draw.rect(screen,(150,0,0),Rect((hit[0],hit[1]),(40,40)))
                pygame.draw.rect(screen,(255,255,0),Rect((shootx,shooty),(40,40)))
                pygame.display.update()
                if len(playerhits) == numberofships:
                    pygame.display.set_mode((width,height))
                    screen.fill((0,0,0))
                    screen.blit(largefont.render("You Win!",True,(255,255,255)),(100,100))
                    fighting = False
                wait(0.1)
        elif turn == 2:
            turn = 1
            choosing = True
            enshootx = 0
            enshooty = 0
            while choosing == True:
                enshootx = 45 + random.randint(0,9) * 40
                enshooty = 75 + random.randint(0,9) * 40
                found = False
                for miss in enemymisses:
                    if miss[0] == enshootx and miss[1] == enshooty:
                        found = True
                for hit in enemyhits:
                    if hit[0] == enshootx and hit[1] == enshooty:
                        found = True
                if found == False:
                    choosing = False
                    
            shiphit = False
            for ship in playerships:
                if ship[0] == enshootx and ship[1] == enshooty:
                    shiphit = True
            if shiphit == True:
                enemyhits.append([enshootx,enshooty])
            elif shiphit == False:
                enemymisses.append([enshootx,enshooty])
                
                if len(enemyhits) == numberofships:
                    pygame.display.set_mode((width,height))
                    screen.fill((0,0,0))
                    screen.blit(largefont.render("You Lose!",True,(255,255,255)),(100,100))
                    fighting = False
    pygame.display.update()
    wait(2)
    return False                   

def play_spaceinvaders():
    screen = pygame.display.set_mode((width,height))
    screen.fill((0,0,0))
    pygame.display.update()
    wait(1)
    alive = True
    score = 0
    level = 0
    # runs the script 40 times per second
    invadertime = 2 * 40
    mothershipwait = 30 * 40
    while alive == True:
        mothershiptime = 0
        speed = 5
        bulletspeed = 15
        position = 100
        player = pygame.draw.rect(screen,(0,255,0),Rect((position,360),(50,20)))
        bullets = []
        invaderbullettime = 0
        invaderbulletwait = 1 * 40
        invaderbullets = []
        bulletwait = 8
        rows_of_invaders = 6
        cols_of_invaders = int(((width / 30)/16)*11)  
        invaders = []
        
        
        
        for rownum in range(rows_of_invaders):
            for colnum in range(cols_of_invaders):
                invaders.append([(colnum - 1) * 30 + 40,rownum * 30 + 85])

        
        bullettime = 0
        invaderdirection = 1
        invadermove = 0
        level += 1
        direction = 0
        mothership = [-50,50]
        MSHIP = pygame.draw.rect(screen,(200,0,0),Rect((mothership[0],mothership[1]),(50,20)))
        while len(invaders)> 0:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                elif event.type == KEYDOWN and event.key == K_d:
                    direction += 1
                elif event.type == KEYUP and event.key == K_d:
                    direction -= 1
                elif event.type == KEYDOWN and event.key == K_a:
                    direction -= 1
                elif event.type == KEYUP and event.key == K_a:
                    direction += 1
                elif event.type == KEYDOWN and event.key == K_w:
                    if bullettime == bulletwait and len(bullets)==0: 
                        bullets.append([player.centerx,player.centery - 5])
                        bullettime = 0
                        if bulletwait > 22:
                            bulletwait -= 2
                if direction > 1:
                    direction = 1
                if direction < -1:
                    direction = -1
            position += speed * direction
            if position > width - 40:
                position = width - 40
            elif position < 10:
                position = 10
            player = pygame.draw.rect(screen,(0,255,0),Rect((position,height - 40),(30,10)))
            deletelist = []
            shotdown = []
            
            if invaderbulletwait == invaderbullettime:
                invadertoshoot = invaders[random.randint(0,len(invaders)-1)]
                invaderbullets.append([invadertoshoot[0],invadertoshoot[1]])
                invaderbullettime = 0

            for index in range(0,len(invaderbullets)):
                bullet = invaderbullets[index]
                if bullet[1] < 500:
                    b = pygame.draw.rect(screen,(255,255,255),Rect((bullet[0],bullet[1]+bulletspeed),(4,12)))
                    invaderbullets[index][1] += (bulletspeed) - (bulletspeed /5)*2
                    if b.colliderect(player) == True:
                        alive = False
                        invaders = []
                    
        
                
            for i in range(0,len(bullets)):
                bullet = bullets[i]
                b = pygame.draw.rect(screen,(0,255,0),Rect((bullet[0],bullet[1]-bulletspeed),(4,10)))
                if bullet[1] < 0:
                    deletelist.append(i)
                else:
                    bullets[i] = [bullet[0],bullet[1]-bulletspeed]
                for index in range(0,len(invaders)):
                    invaderpos = invaders[index]
                    invader = pygame.draw.rect(screen,(255,255,255),Rect((invaderpos[0],invaderpos[1]),(25,25)))
                    if invader.colliderect(b) == True:
                        bullets[i][1] = -20
                        score += 20
                        shotdown.append(index)
                if b.colliderect(MSHIP) == True:
                    mothershiptime = 0 + (mothershipwait - mothershiptime)
                    mothership = [-50,50]
                    bullets[i][1] = -20
                    score += random.randint(1,6) * 50
            for invader in shotdown:
                invaders.pop(invader)
            for bullet in deletelist:
                bullets.pop(bullet)
                break

            if mothershiptime == mothershipwait:
                mothership[0] += 4
                MSHIP = pygame.draw.rect(screen,(200,0,0),Rect((mothership[0],mothership[1]),(50,20)))
                if mothership[0] > 500:
                    mothership = [-50,50]
                    mothershiptime = 0
            
            newdirection = invaderdirection
            for invader in invaders:
                pygame.draw.rect(screen,(255,255,255),Rect((invader[0],invader[1]),(25,25)))
                if invadermove == invadertime:
                    invader[0] = invader[0] + (30 * invaderdirection)
                    if invader[0] < 40:
                        newdirection = 1
                    elif invader[0] > width - (40 + 30):
                        newdirection = -1
            if invaderdirection != newdirection:
                for invader in invaders:
                    invader[1] = invader[1] + 30
                    if invader[1] > 420:
                        alive = False
            invaderdirection = newdirection
            if invadermove == invadertime:
                invadermove = 0
            if alive == False:
                invaders = []
            
            
            pygame.draw.rect(screen,(0,0,0),Rect((0,0),(width,40)))
            screen.blit(smallfont.render("Score: "+str(score),True,(255,255,255)),(400,20))
            screen.blit(smallfont.render("Level"+str(level),True,(255,255,255)),(300,20))
            pygame.display.update()
            
            if bullettime < bulletwait:
                bullettime += 1
            if invadermove < invadertime:
                invadermove += 1
            if mothershiptime < mothershipwait:
                mothershiptime += 1
            if invaderbullettime < invaderbulletwait:
                invaderbullettime += 1

            wait(0.025)
        if invadertime > 30:
            invadertime -= 10
        invadermove = 0   
    screen.fill((0,0,0))
    screen.blit(largefont.render("GAME OVER",True,(255,255,255)),(100,50))
    screen.blit(medfont.render("You completed "+str(level-1)+" levels",True,(255,255,255)),(80,150))
    screen.blit(medfont.render("Your final score was: "+str(score),True,(255,255,255)),(80,250))
    pygame.display.update()
    wait(8)
    return False

numofgames = 3
selectedgame = numofgames
while True:
    screen = pygame.display.set_mode(size)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == KEYDOWN and event.key == K_w:
            if selectedgame < numofgames:
                selectedgame += 1
        elif event.type == KEYDOWN and event.key == K_s:
            if selectedgame > 1:
                selectedgame -= 1
        elif event.type == KEYDOWN and event.key == K_RETURN:
            if selectedgame == numofgames:
                play_snake()
            elif selectedgame == numofgames-1:
                play_battleship()
            elif selectedgame == numofgames-2:
                play_spaceinvaders()
          
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(100,100,100),Rect((0,0),(500,40)))
    screen.blit(medfont.render("Choose a game:",True,(255,255,255)),(140,0))
    #snake
    if selectedgame == numofgames:
        pygame.draw.rect(screen,(200,200,0),Rect((0,40),(100,50)))
    else:
        pygame.draw.rect(screen,(150,150,150),Rect((0,40),(100,50)))
    screen.blit(smallfont.render("Snake",True,(255,255,255)),(0,50))
    #battleship
    if selectedgame == numofgames-1:
        pygame.draw.rect(screen,(200,200,0),Rect((0,90),(100,50)))
    else:
        pygame.draw.rect(screen,(150,150,150),Rect((0,90),(100,50)))
    screen.blit(smallfont.render("Battleship",True,(255,255,255)),(0,100))
    if selectedgame == numofgames-2:
        pygame.draw.rect(screen,(200,200,0),Rect((0,130),(100,50)))
    else:
        pygame.draw.rect(screen,(150,150,150),Rect((0,130),(100,50)))
    screen.blit(smallfont.render("Space Invaders",True,(255,255,255)),(0,150))
    
    
    
    
    pygame.display.update()
