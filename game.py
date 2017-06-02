import pygame
import random

def main():
    pygame.init()
    height = 800
    width = 800
    psize = 100
    screen = pygame.display.set_mode((height,width))
    clock = pygame.time.Clock()
    done = False
    x0 = 0
    y0 = 15
    x1 = height - 20
    y1 = width - 95
    x2 = 15
    y2 = 0
    x3 = width - 95
    y3 = height - 20
    color = (0,128,251)
    bcolor = (100,120,25)
    bx = random.randint(50, height - 50)
    by = random.randint(50, width - 50)
    left = True
    up = True
    score = 0
    font = pygame.font.SysFont("comicsansms",24)
    font1 = pygame.font.SysFont("comicsansms",36)
    bSpeedy = 3
    bSpeedx = 3
    collide = False
    highScore = get_high_score()
    pygame.mixer.music.load("sound.mp3")
    while not done:
        title = font1.render("4-Way Pong",True,(255,255,255))
        text1 = font.render("High Score: "+str(highScore),True, (255,255,255))
        text = font.render("Score: "+ str(score), True, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                done = True
        pressed = pygame.key.get_pressed()
        #left and up paddle movement
        if pressed[pygame.K_UP]:
            if y0 - 13 >= 0: 
                y0 -= 13
                x2 -= 13
        if pressed[pygame.K_DOWN]:
            if y0 + 13 <= height - psize: 
                y0 += 13
                x2 += 13
        #right and bottom paddle movement
        if pressed[pygame.K_RIGHT]:
            if y1 + 13 <= height - psize: 
                y1 += 13
                x3 += 13
        if pressed[pygame.K_LEFT]:
            if y1 - 13 >= 0: 
                y1 -= 13
                x3 -= 13

        #move the ball
        if left:
            if( bx - bSpeedx <= 20):
                bx = 19
            else:    
                bx -= bSpeedx
            #check if hit paddle
            if( by >= y0 and by <= y0+psize ):
                if( bx <= 20):
                    score += 1
                    left = False
                    bx += random.randint(1, 10)
                    bSpeedx += 1
                    pygame.mixer.music.play()
            #check if hit wall
            else:
                if( bx <= 20 ): 
                    left = False
                    if( score > highScore):
                        save_high_score(score)
                        highScore = score
                    score = 0
                    bx = random.randint(50, height - 50)
                    by = random.randint(50, width - 50)
                    bSpeedx = 3
        else:
            if( bx + bSpeedx >= width-20):
                bx = width-19
            else:    
                bx += bSpeedx
            #if hit paddle
            if( by >= y1 and by <= y1 + psize ):
                if( bx >= width-20 ):
                    score += 1
                    left = True
                    bx -= random.randint(1, 10)
                    bSpeedx += 1
                    pygame.mixer.music.play()
            #check if hit wall
            else:
                if( bx >= width-20 ): 
                    left = True
                    if( score > highScore):
                        save_high_score(score)
                        highScore = score                        
                    score = 0
                    bx = random.randint(50, height - 50)
                    by = random.randint(50, width - 50)
                    bSpeedx = 3
        if up:
            if( by - bSpeedy <= 19):
                by = 20
            else:    
                by -= bSpeedy
            #check if hit paddle
            if( bx >= x2 and bx <= x2+psize ):
                if( by <= 20 ):
                    score += 1
                    pygame.mixer.music.play()
                    up = False
                    by += random.randint(1, 10)
                    bSpeedy += 1
            #check if hit wall
            else:
                if( by <= 20 ):
                    up = False
                    if( score > highScore):
                        save_high_score(score)
                        highScore = score                        
                    score = 0
                    bx = random.randint(50, height - 50)
                    by = random.randint(50, width - 50)
                    bSpeedy = 3
        else:
            if( by + bSpeedy >= height-20):
                by = height-19
            else:    
                by += bSpeedy
            #check if hit paddle
            if( bx >= x3 and bx <= x3+psize ):
                if( by >= height-20 ):
                    score += 1
                    pygame.mixer.music.play()
                    up = True
                    by -= random.randint(1, 10)
                    bSpeedy += 1
            #check if hit wall
            else:
                if( by >= height - 20 ):
                    if( score > highScore):
                        save_high_score(score)
                        highScore = score
                    score = 0
                    bx = random.randint(50, height - 50)
                    by = random.randint(50, width - 50)
                    bSpeedy = 3
        #reset the screen
        screen.fill((0,0,0))
        #paddle on the left        
        pygame.draw.rect(screen, color, pygame.Rect(x0, y0, 20, psize))
        #paddle on the right
        pygame.draw.rect(screen, color, pygame.Rect(x1, y1, 20, psize))
        #paddle on top
        pygame.draw.rect(screen, color, pygame.Rect(x2, y2, psize, 20))
        #paddle on bottom
        pygame.draw.rect(screen, color, pygame.Rect(x3, y3, psize, 20))
        #draw ball
        pygame.draw.circle(screen, bcolor, (bx,by), 9)
        screen.blit(title,(400 - text.get_width() // 2, (400 - text.get_height() // 2)-100 ))
        screen.blit(text,(400 - text.get_width() // 2, 400 - text.get_height() // 2))
        screen.blit(text1,(400 - text.get_width() // 2, (400 - text.get_height() // 2)-50 ))
        pygame.display.flip()
        clock.tick(120)

def get_high_score():
    # Default high score
    high_score = 0
    # Try to read the high score from a file
    try:
        file = open("High_Score.txt", "r")
        high_score = int(file.read())
        file.close()
        print("The high score is", high_score)
    except IOError:
        print("No value.")
    except ValueError:
        print("Error in number")
 
    return high_score

def save_high_score(new_high_score):
    try:
        # Write the file to disk
        file = open("high_score.txt", "w")
        file.write(str(new_high_score))
        file.close()
    except IOError:
        print("error saving highscore")

if __name__ == "__main__":
    main()