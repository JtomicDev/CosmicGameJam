import pygame
import random
import sys
import time
from pygame import draw

from pygame.constants import K_KP_ENTER, K_RETURN, K_a, K_d, WINDOWRESTORED
from pygame.mixer import Sound
from pygame.time import Clock

pygame.mixer.init()



#window variables
WIDTH, HEIGHT = 1200, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic")

#Game colours
BGCol = ((161, 70, 161))

#Game images
BGIMG = pygame.image.load("BackGround.jpg")
ROCKETIMG = pygame.image.load("RocketOutput.png")
ROCKETIMG2 = pygame.image.load("RocketOutput2Pix.png")
ROCKETIMG3 = pygame.image.load("RocketOutput3Pix.png")
StarImg1 = pygame.image.load("Star-1.png")
StarImg2 = pygame.image.load("Star-1.png")
WarningImg = pygame.image.load("warning.png")
Warning = pygame.transform.scale(WarningImg, (51, 51))

DEDimg = pygame.image.load("ded.png")
DED = pygame.transform.scale(DEDimg, (500, 250))

ENEMYIMG = pygame.image.load("Enemy.png")
Enemy = pygame.transform.scale(ENEMYIMG, (200, 100))

RandomRocket = random.choice([1, 2, 3])

FPS = 60

RocketTrail = pygame.transform.scale(ROCKETIMG, (120, 120))

RocketTrail2 = pygame.transform.scale(ROCKETIMG2, (120, 120))

RocketTrail3 = pygame.transform.scale(ROCKETIMG3, (120, 120))


#SOUNDS
SpawnSound = pygame.mixer.Sound("AsteroidSpawn.wav")
DedSound = pygame.mixer.Sound("DED.wav")


BG = pygame.transform.scale(BGIMG, (WIDTH, HEIGHT))



PlayerX = 150
VEL = 8
BULLET_VEL = VEL + 5
MAX_BULLETS = 3
ASTEROID_VELOCITY = 5
ASTEROID_RESET = random.randrange(50, 1000)
particles = []

SPACESHIP_HIT = pygame.USEREVENT + 1


PlayerImg = pygame.image.load("RocketThing.png")
PlayerImgNoThrust = pygame.image.load("RocketNT.png")
PlayerLeft = pygame.image.load("RocketRotateLeft.png")
PlayerRight = pygame.image.load("RocketRotateRight.png")
Player = pygame.transform.scale(PlayerImg, (150, 300))
PlayerNoThrust = pygame.transform.scale(PlayerImgNoThrust, (150, 300))
PlayerL = pygame.transform.scale(PlayerLeft, (150, 300))
PlayerR = pygame.transform.scale(PlayerRight, (150, 300))

ICON = pygame.image.load("SPLONK.png")

pygame.display.set_icon(ICON)

#Asteroid stuff
AsteroidImg = pygame.image.load("Asteroid1.png")
Asteroid = pygame.transform.scale(AsteroidImg, (120, 120))
AsteroidPosition = random.randrange(200, 1000)
Asteroid3 = pygame.transform.scale(AsteroidImg, (120, 120))
Asteroid4 = pygame.transform.scale(AsteroidImg, (120, 120))
Asteroid5 = pygame.transform.scale(AsteroidImg, (120, 120))

MissleImg = pygame.image.load("Missle.png")
Missle = pygame.transform.scale(MissleImg, (100, 200))

MissleSpawn = pygame.mixer.Sound("MissleSpawn.wav")
#laser stuff
LaserImg = pygame.image.load("laser.png")
Laser = pygame.transform.scale(LaserImg, (40, 90))


#TutorialStuff
TutorialImg = pygame.image.load("TutorialRocket.png")
TutorialImg2 = pygame.image.load("TutorialRocket2.png")
Tutorial1 = pygame.transform.scale(TutorialImg, (300, 300))
Tutorial2 = pygame.transform.scale(TutorialImg2, (300, 300))

def lose(DED):
    WINDOW.blit(DED, (350, 250))
    pygame.display.update()
    pygame.time.delay(5000)



      

play = pygame.Rect(600, 350, 150, 150)
def draw_window(Spaceship, Asteroid2, Tutorial, Tutorial2Pos, Star_Rect1, STAR, Star_Rect2, STAR2, Star_Rect3, STAR3, run, clock, Asteroid3s, Asteroid4s, Asteroid5, Asteroid5s, MissleRect, Asteroid6s):
        keys_pressed = pygame.key.get_pressed()
        WINDOW.fill(BGCol)
        WINDOW.blit(BG, (0, 0))
        WINDOW.blit(STAR, (Star_Rect1.x, Star_Rect1.y))
        WINDOW.blit(STAR2, (Star_Rect2.x, Star_Rect2.y))
        WINDOW.blit(STAR3, (Star_Rect3.x, Star_Rect3.y))
        WINDOW.blit(Asteroid, (Asteroid2.x, Asteroid2.y))
        WINDOW.blit(Asteroid3, (Asteroid3s.x, Asteroid3s.y))
        WINDOW.blit(Asteroid4, (Asteroid4s.x, Asteroid4s.y))
        WINDOW.blit(Asteroid5, (Asteroid6s.x, Asteroid6s.y))
        WINDOW.blit(Missle, (MissleRect.x, MissleRect.y))
        WINDOW.blit(Tutorial1, (Tutorial.x, Tutorial.y))
        WINDOW.blit(Tutorial2, (Tutorial2Pos.x, Tutorial2Pos.y))
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d]:
            if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d]:
                if keys_pressed[pygame.K_a]:
                    WINDOW.blit(PlayerL, (Spaceship.x, Spaceship.y))  
                if keys_pressed[pygame.K_d]:
                    WINDOW.blit(PlayerR, (Spaceship.x, Spaceship.y))

            else:
                WINDOW.blit(Player, (Spaceship.x, Spaceship.y))
        else:
            WINDOW.blit(PlayerNoThrust, (Spaceship.x, Spaceship.y))
        if Spaceship.colliderect(Asteroid2):
                print("collision")
                WINDOW.blit(DED, (350, 250))
                pygame.time.delay(5000)

        if Spaceship.colliderect(Asteroid3s):
                print("collision")
                WINDOW.blit(DED, (350, 250))
                pygame.time.delay(5000)

        if Spaceship.colliderect(Asteroid4s):
                print("collision")
                WINDOW.blit(DED, (350, 250))
                pygame.time.delay(5000)

        pygame.display.update()

#def tutorial(Tutorial1, Tutorial)




def Star_Spawn(Star_Rect1, STAR):
    WINDOW.blit(STAR, (Star_Rect1.x, Star_Rect1.y))
    time.sleep(random.randrange(3, 10))
    WINDOW.blit(STAR, (Star_Rect1.x, Star_Rect1.y))


    
def rocket_handle_movement(keys_pressed, Spaceship):
    if keys_pressed[pygame.K_a]:
            Spaceship.x -= VEL
    if keys_pressed[pygame.K_d]:
            Spaceship.x += VEL
    if keys_pressed[pygame.K_s]:
            Spaceship.y += VEL
    if keys_pressed[pygame.K_w]:
            Spaceship.y -= VEL



def AsteroidMovement(Asteroid2, AsteroidPosition):
    time.sleep(1)


STAR = pygame.transform.scale(StarImg1, (100, 100))
STAR2 = pygame.transform.scale(StarImg1, (200, 200))
STAR3 = pygame.transform.scale(StarImg1, (300, 300))


#def RotateLeft(Player, Spaceship):

def handle_asteroids(Spaceship, Asteroid2):
     if Spaceship.colliderect(Asteroid2):
         pygame.event.post(pygame.event.Event(SPACESHIP_HIT))

AsteroidPosition = random.randrange(200, 1000)

Soundtrack = pygame.mixer.Sound("Soundtrack.OGG")
Soundtrack.set_volume(0.2)
Soundtrack.play()


def main():
    global VEL
    Spaceship = pygame.Rect(500, 500, 150, 150)
    bullets = []
    Asteroid2 = pygame.Rect(random.randrange(200, 1000), -100, 50, 50)
    Asteroid3S = pygame.Rect(random.randrange(200, 1000), -600, 50, 50)
    Asteroid4s = pygame.Rect(random.randrange(200, 1000), -1200, 50, 50)
    Asteroid5s = pygame.Rect(random.randrange(200, 1000), -2000, 50, 50)
    Asteroid6s = pygame.Rect(random.randrange(200, 1000), -2000, 50, 50)
    Tutorial = pygame.Rect(20, -50, 100, 100)
    Tutorial2Pos = pygame.Rect(20, -2000, 100, 100)
    BillboardTutorial = pygame.Rect
    Star_Rect1 = pygame.Rect((random.randrange(20, 1200), -10, 100, 100))
    Star_Rect2 = pygame.Rect((random.randrange(20, 1200), -10, 100, 100))
    Star_Rect3 = pygame.Rect((random.randrange(20, 1200), -10, 100, 100)) 
    MissleRect = pygame.Rect(2000, Spaceship.y, 100, 100)

    clock = pygame.time.Clock()
    run = True

 
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    
            

        keys_pressed = pygame.key.get_pressed()
        if Spaceship.x >= 1100:
                print("hello")



        

        if keys_pressed[pygame.K_a]:
            Spaceship.x -= VEL
            VEL = 7
        if keys_pressed[pygame.K_d]:
            Spaceship.x += VEL
            VEL = 7
        if keys_pressed[pygame.K_s]:
            Spaceship.y += VEL
            VEL = 7
        if keys_pressed[pygame.K_w]:
            VEL = 7
            Spaceship.y -= VEL

        AstVEL= random.randrange(5, 10)
        AstVEL1= random.randrange(5, 10)
        AstVEL2= random.randrange(5, 10)
        AstVEL3= random.randrange(5, 10)
            

        if Asteroid2.y < 1000:
            Asteroid2.y += AstVEL
        else:
            Asteroid2.y = random.randrange(-100, -1)
            Asteroid2.x = random.randrange(0, 1200)
            SpawnSound.play()
            print("Asteroid Spawn")

            print(AstVEL)

        if Asteroid3S.y < 1000:
            Asteroid3S.y += AstVEL1
        else:
            Asteroid3S.y = random.randrange(-100, -1)
            Asteroid3S.x = random.randrange(0, 1200)
            SpawnSound.play()
            print("Asteroid Spawn")

            print(AstVEL1)

        if Asteroid4s.y < 1000:
            Asteroid4s.y += AstVEL2
        else:
            Asteroid4s.y = random.randrange(-100, -1)
            Asteroid4s.x = random.randrange(0, 1200)
            SpawnSound.play()
            print("Asteroid Spawn")

            print(AstVEL2)

        if Asteroid5s.y < 1000:
            Asteroid5s.y += AstVEL3
        else:
            Asteroid5s.y = random.randrange(-100, -1)
            Asteroid5s.x = random.randrange(0, 1200)
            SpawnSound.play()
            print("Asteroid Spawn")

            print(AstVEL3)


        if Asteroid6s.y < 1000:
            Asteroid6s.y += AstVEL3
        else:
            Asteroid6s.y = random.randrange(-100, -1)
            Asteroid6s.x = random.randrange(0, 1200)
            SpawnSound.play()
            print("asteroid6")

            print(AstVEL3)




        if MissleRect.y < random.randrange(3000, 6000):
            MissleRect.y += 10
        else:
            MissleRect.x = random.randrange(0, 1200)
            MissleRect.y = 0
            MissleSpawn.play()
            print("missle spawn")

            print(AstVEL)

        Random = 1
    
        if Star_Rect1.y < 1000:
            Star_Rect1.y += Random
        else:
            Star_Rect1.y = -100
            Star_Rect1.x = random.randrange(-100, 1200)
            print("Star Spawn")
    

        if Star_Rect2.y < 1000:
            Star_Rect2.y += Random
        else:
            Star_Rect2.y = -100
            Star_Rect2.x = random.randrange(-100, 1200)
            print("Star Spawn")

        if Star_Rect3.y < 1000:
            Star_Rect3.y += Random
        else:
            Star_Rect3.y = -100
            Star_Rect3.x = random.randrange(-100, 1000)
            print("Star Spawn")


    
    
        Tutorial.y += 2
        Tutorial2Pos.y += 2  
        Star_Rect1.y += 0
        Star_Rect2.y += 0
        Star_Rect3.y += 0

        if Spaceship.colliderect(Asteroid2):
            print("collision")
            WINDOW.blit(DED, (350, 250))
            time.sleep(2)
            sys.exit()
        if Spaceship.colliderect(Asteroid3S):
            print("collision")
            WINDOW.blit(DED, (350, 250))
            time.sleep(2)
            sys.exit()
        if Spaceship.colliderect(Asteroid4s):
            print("collision")
            WINDOW.blit(DED, (350, 250))
            time.sleep(2)
            sys.exit()

        if Spaceship.colliderect(Asteroid6s):
            print("collision")
            WINDOW.blit(DED, (350, 250))
            time.sleep(2)
            sys.exit()

        if Spaceship.colliderect(MissleRect):
            print("collision")
            WINDOW.blit(DED, (350, 250))
            time.sleep(2)
            sys.exit()
        WINDOW.blit(Warning, (MissleRect.x, 0))
#tutorial2pos = tutorial2 really, i'm just dumb and can't name my variables properly
        draw_window(Spaceship, Asteroid2, Tutorial, Tutorial2Pos, Star_Rect1, STAR, Star_Rect2, STAR2, Star_Rect3, STAR3, run, clock, Asteroid3S, Asteroid4s, Asteroid5, Asteroid5, MissleRect, Asteroid6s)
        #handle_asteroids(Asteroid2, Spaceship)
    pygame.display.update()
    while run:
        time.sleep(1)
        ASTEROID_VELOCITY + 1
    pygame.quit()
    sys.exit()

 




if __name__ == "__main__":
    main()








