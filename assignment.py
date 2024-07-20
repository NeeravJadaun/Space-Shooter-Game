#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Neerav Jadaun
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
# I think this project deserves a level 4+ because I went above and beyond with my game by adding extra features and working efficiently
# To start off I completed my project planning in a timely manner, aswell as implemented anyy changes suggested after the project planning checkup to ensure sucsess
# I reached all my requirements for V3 except adding a Leaderboard and Power Ups, but which I made up for by adding other complex and sophisticated ideas
# I used class time effectively and made sure to make many commits as I progressed reaching the 20 commit requirement
# Looking at the rubric I made sure my code was efficient and met all of the requirements for a clean polished code
# My game has the replayablity feature and also has a factor of randomness to it as well
# Lastly I believe I made through comments throughout my code to explain my code well enough

#
# Features Added:
#   - Collision Detection
#   - Sound Effects
#   - Character Selection
#   - Map Selection
#   - Enemy Plane
#   - Enemy Plane Shooting
#   - Boss Fight
#   - Random Enemies and Random Bullets
#   - User Controlled Plane(SpaceBar)
#   - Scrolling Background
#   - Animations
#   - Score Display
#   - Main Menu, Difficulty Menu
#   - Health System
#-----------------------------------------------------------------------------
import pygame
import random

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSizeX = 700   # Desired physical surface size, in pixels.
    surfaceSizeY = 700
    clock = pygame.time.Clock()  # Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSizeX, surfaceSizeY))

    #-----------------------------Program Variable Initialization----------------------------#

    # source: https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=14s
    bg1 = pygame.image.load("images/bg1.png")
    bg1Hangar = pygame.image.load("images/bg1.png")
    bg1Hangar = pygame.transform.scale(bg1Hangar, (100,150))
    # source: https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=14s
    char1spriteSheet = pygame.image.load("images/char1spriteSheet.png")
    char1Hangar = pygame.image.load("images/char1Hangar.png")
    char1Hangar = pygame.transform.scale(char1Hangar, (100,100))
    # source: https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=14s
    bullet = pygame.image.load("images/bullet.png")
    bullet = pygame.transform.scale(bullet, (45,35))
    # source: https://www.pinterest.com/pin/618822805026737369/
    enemy1 = pygame.image.load("images/enemy1.png")
    enemy1 = pygame.transform.scale(enemy1, (50,40))
    # source: https://www.vecteezy.com/vector-art/13224424-animation-sprite-sheet-of-bomb-explosion-sequence
    blowup = pygame.image.load("images/blowup.png")
    blowup = pygame.transform.scale(blowup, (25,25))
    # source: https://www.europosters.eu/art-photo/dark-galaxy-background-v144889
    startScreenBg = pygame.image.load("images/startScreenbackground.jpg")
    startScreenBg = pygame.transform.scale(startScreenBg, (750,750))
    # source: https://www.hardcoredroid.com/1945-galaxy-shooter-review/
    spaceShootersLogo = pygame.image.load("images/spaceShootersLogo.png")
    spaceShootersLogo = pygame.transform.scale(spaceShootersLogo, (400,250))
    # source: https://github.com/shubamuzumaki/Space-Shooter
    startScreenButtons = pygame.image.load("images/startScreenButtons.png")
    startScreenButtons = pygame.transform.scale(startScreenButtons, (200,200))
    enemybullet = pygame.image.load("images/enemybullet.png")
    enemybullet = pygame.transform.scale(enemybullet, (25,30))
    hangarBg = pygame.image.load("images/hangarBg.png")
    hangarBg = pygame.transform.scale(hangarBg, (700,700))
    #source: https://ursarctosdev.medium.com/creating-a-retro-game-over-screen-c711a2894506
    gameOverScreenBg = pygame.image.load("images/gameOverScreenBg.png")
    gameOverScreenBg = pygame.transform.scale(gameOverScreenBg, (700,700))
    #source: https://commons.wikimedia.org/wiki/File:BackButton.svg
    backButton = pygame.image.load("images/backButton.png")
    backButton = pygame.transform.scale(backButton, (40,40))
    #source: https://www.pinterest.com/pin/space-shooter-2d-game-kit--675540012837337013/
    char2SpriteSheet = pygame.image.load("images/char2plane.png")
    char2Hangar = pygame.image.load("images/char2Hangar.png")
    char2Hangar = pygame.transform.scale(char2Hangar, (100,100))
    #source: https://ouya.cweiske.de/game/com.frimastudio.android.SpaceShooterFree.htm
    difficultySceneBg = pygame.image.load("images/difficultySceneBg.jpg")
    difficultySceneBg = pygame.transform.scale(difficultySceneBg, (700,700))
    #source:https://www.facebook.com/Space.Shooter.Fanpage/photos/a.863283490504259/2192050054294256/?type=3
    bossImage = pygame.image.load("images/boss.png")
    bossImage = pygame.transform.scale(bossImage, (300,300))
    #source: https://kingwel.artstation.com/projects/YaGlJw
    bg2 = pygame.image.load("images/bg2.jpg")
    bg2Hangar = pygame.image.load("images/bg2.jpg")
    bg2Hangar = pygame.transform.scale(bg2Hangar, (100,150))
    #source: https://opengameart.org/content/stars-parallax-backgrounds
    bg3 = pygame.image.load("images/bg3.jpg")
    bg3Hangar = pygame.image.load("images/bg3.jpg")
    bg3Hangar = pygame.transform.scale(bg3Hangar, (100,150))
    howToPlayLogo = pygame.image.load("images/howToPlayLogo.png")
    howToPlayLogo = pygame.transform.scale(howToPlayLogo, (300,100))
    #source: https://www.giantbomb.com/wasd-movement/3015-472/
    howToPlayWASD = pygame.image.load("images/howToPlayWASD.png")
    howToPlayWASD = pygame.transform.scale(howToPlayWASD, (200,200))
    howToPlayBg = pygame.image.load("images/howToPlayBg.jpg")
    howToPlayBg = pygame.transform.scale(howToPlayBg, (700,700))
    howToPlaySpaceBar = pygame.image.load("images/howToPlaySpaceBar.webp")
    howToPlaySpaceBar = pygame.transform.scale(howToPlaySpaceBar, (200,200))
    #source: https://mixkit.co/free-sound-effects/gun/
    shootSound = pygame.mixer.Sound('sounds/shoot.mp3')
    shootSound.set_volume(0.75)
    #source:
    backGroundSound = pygame.mixer.Sound('sounds/bgmusic.mp3')
    backGroundSound.set_volume(0.75)

    
# Initial positions for background images
    bgY = 0
    bgY2 = 700

    # Initial position for the character
    charPos = [325,650]

    # Lists to store positions of bullets, enemies, enemy bullets, and boss enemies
    bullet1PosList = []
    enemy1PosList = []
    enemybulletPosList = []
    bossEnemyPosList = []

    # Scale factors for character sprites
    char1scale = 0.4
    char2scale = 1


    # Character 1 sprite rectangle dimensions and animation parameters
    char1Rect = [250 * char1scale, 17 * char1scale, 130 * char1scale, 115 * char1scale]
    char1PatchNumber = 2
    char1NumPatches = 5

    # Character 2 sprite rectangle dimensions and animation parameters
    char2Rect = [char2scale * 36, char2scale * 0, char2scale * 36, char2scale * 50]
    char2PatchNumber = 1
    char2NumPatches = 3

    # Frame rate control variables
    framecount = 60

    char1fr = 10
    char2fr = 10

    # Counters for frames and various delays
    frameCount = 0
    storeCount = 0

    enemy_bullet_delay = 240  # Delay between each enemy bullet shot
    enemy_bullet_delay_counter = 0  # Counter to keep track of delay between enemy bullets

    bossBulletDelay = 60  # Delay between each enemy bullet shot
    bossBulletDelayCounter = 0  # Counter to keep track of delay between enemy bullets

    char1rectdim = [charPos[0] + 2.5, charPos[1], 105 * char1scale, 105 * char1scale]

    char1spriteSheet = pygame.transform.smoothscale(char1spriteSheet, (int(char1scale * char1spriteSheet.get_width()), int(char1scale * char1spriteSheet.get_height())))
    char2SpriteSheet = pygame.transform.smoothscale(char2SpriteSheet, (int(char2scale * char2SpriteSheet.get_width()), int(char2scale * char2SpriteSheet.get_height())))

    currentCharIndex = 0

    currentMapIndex = 0

    currentDiffIndex = 0

    playRectDim = [275, 320, 160, 60]
    hangarRectDim = [293, 420, 120, 60]
    backButtonDim = [600, 600, 40, 40]

    char1selectRectDim = [250, 180, 100, 100]

    char2selectRectDim = [450, 180, 100, 100]

    easyRectDim = [290,175,150,50]

    mediumRectDim = [290, 285, 150,50]

    hardRectDim = [290, 385, 150,50]

    bg1RectDim = [150,400,100,150]
    bg2RectDim = [330,400,100,150]
    bg3RectDim = [500,400,100,150]

    backRectDim = [75,625, 150,50]

    howToPlayRectDim = [210,500, 300,100]

    lives = 3
    score = 0

    bg = bg1

    boss_health = 100
    boss_max_health = 100
    health_bar_width = 100
    health_bar_height = 10

    player_health = 100
    player_max_health = 100
    player_health_bar_width = 100
    player_health_bar_height = 10

    charNumPatches = char1NumPatches
    charRect = char1Rect

    bossActive = False
    bossLives = 10
    bossPos = [200,-50]  # Start the boss off the screen
    bossBulletPosList = []
    timer = 0
    bossSpawnScore = 20
    bossHealthIncrease = 20  # Amount of health to increase for each boss fight

    programState = "startScene"
    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...

        # Inital Gamestate serves as the mainMenu for the game, to navigate through different features of the game.
        if programState == "startScene":
            playRect = pygame.Rect(playRectDim)
            hangarRect = pygame.Rect(hangarRectDim)
            howToPlayRect = pygame.Rect(howToPlayRectDim)

             # Set up font
            font = pygame.font.Font(None, 50)

            # Render the text
            howToPlayText = font.render("How to Play", True, (255, 105, 180))

            score = 0

            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            # Check for mouse clicks on buttons
            if (pointX > playRect.x and pointX < playRect.x + playRect.width):
                if(pointY > playRect.y and pointY < playRect.y + playRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "difficultyScene"

            if(pointX > hangarRect.x and pointX < hangarRect.x + hangarRect.width):
                if(pointY > hangarRect.y and pointY < hangarRect.y + hangarRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "hangarScene"

            if(pointX > howToPlayRect.x and pointX < howToPlayRect.x + howToPlayRect.width):
                if(pointY > howToPlayRect.y and pointY < howToPlayRect.y + howToPlayRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "howToPlay"

            # Blit elements to main surface
            mainSurface.blit(startScreenBg, (0, 0))
            mainSurface.blit(spaceShootersLogo, (150, 50))
            mainSurface.blit(startScreenButtons, (260, 300))
            mainSurface.blit(howToPlayLogo, (210, 500))
            mainSurface.blit(howToPlayText, (265, 530))


        elif programState == "howToPlay":
            backButtonRectDim1 = (500,500,40,40)
            backButtonRect1 = pygame.Rect(backButtonRectDim1)
            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]
            
            # Set up font
            font = pygame.font.Font(None, 50)

            if(pointX > backButtonRect1.x and pointX < backButtonRect1.x + backButtonRect1.width):
                if(pointY > backButtonRect1.y and pointY < backButtonRect1.y + backButtonRect1.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "startScene"

            # Render the text
            howToPlaySpaceBarText = font.render("Press SpaceBar to Shoot!", True, (255, 255, 255))

            mainSurface.blit(howToPlayBg, (0,0))
            mainSurface.blit(howToPlayWASD, (125, 250))
            mainSurface.blit(howToPlaySpaceBar, (400, 250))
            mainSurface.blit(howToPlaySpaceBarText, (150, 175))
            mainSurface.blit(backButton, (500, 500))


        elif programState == "hangarScene":
            char1HangarRect = pygame.Rect(char1selectRectDim)
            char2HangarRect = pygame.Rect(char2selectRectDim)
            backButtonRect = pygame.Rect(backButtonDim)
            bg1Rect = pygame.Rect(bg1RectDim)
            bg2Rect = pygame.Rect(bg2RectDim)
            bg3Rect = pygame.Rect(bg3RectDim)

            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            if(pointX > char1HangarRect.x and pointX < char1HangarRect.x + char1HangarRect.width):
                if(pointY > char1HangarRect.y and pointY < char1HangarRect.y + char1HangarRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        currentCharIndex = 0

            if (pointX > char2HangarRect.x and pointX < char2HangarRect.x + char2HangarRect.width):
                if(pointY > char2HangarRect.y and pointY < char2HangarRect.y + char2HangarRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        currentCharIndex = 1

            if(pointX > bg1Rect.x and pointX < bg1Rect.x + bg1Rect.width):
                if(pointY > bg1Rect.y and pointY < bg1Rect.y + bg1Rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        bg = bg1

            if(pointX > bg2Rect.x and pointX < bg2Rect.x + bg2Rect.width):
                if(pointY > bg2Rect.y and pointY < bg2Rect.y + bg2Rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        bg = bg2
            
            if(pointX > bg3Rect.x and pointX < bg3Rect.x + bg3Rect.width):
                if(pointY > bg3Rect.y and pointY < bg3Rect.y + bg3Rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        bg = bg3

            if currentCharIndex  == 0:
                charNumPatches = char1NumPatches
                charRect = char1Rect
            elif currentCharIndex == 1:
                charNumPatches = char2NumPatches
                charRect = char2Rect

            if(pointX > backButtonRect.x and pointX < backButtonRect.x + backButtonRect.width):
                if(pointY > backButtonRect.y and pointY < backButtonRect.y + backButtonRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "startScene"

            mainSurface.blit(hangarBg, (0, 0))
            if currentCharIndex == 0:
                 pygame.draw.rect(mainSurface, (255,0,0), (250,175,100,100))
            if currentCharIndex == 1:
                 pygame.draw.rect(mainSurface, (255,0,0), (450,175,100,100))


            if bg == bg1:
                 pygame.draw.rect(mainSurface, (255,0,0), (130, 390, 140, 170))
            if bg == bg2:
                 pygame.draw.rect(mainSurface, (255,0,0), (315,390,130,170))
            if bg == bg3:
                pygame.draw.rect(mainSurface, (255,0,0), (485, 390, 130, 170))


            mainSurface.blit(backButton, (600, 600))
            mainSurface.blit(char1Hangar, (250, 180))
            mainSurface.blit(char2Hangar, (450, 180))

            mainSurface.blit(bg1Hangar, (150,400))
            mainSurface.blit(bg2Hangar, (330,400))
            mainSurface.blit(bg3Hangar, (500,400))

        elif programState == "difficultyScene":
            easyRect = pygame.Rect(easyRectDim)
            mediumRect = pygame.Rect(mediumRectDim)
            hardRect = pygame.Rect(hardRectDim)
            backRect = pygame.Rect(backRectDim)

            # Set up font
            font = pygame.font.Font(None, 50)

            # Render the text
            easyText = font.render("Easy", True, (255,255,255))
            mediumText = font.render("Medium", True, (255, 255, 255))
            hardText = font.render("Hard", True, (255, 255, 255))

            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            if(pointX > easyRect.x and pointX < easyRect.x + easyRect.width):
                if(pointY > easyRect.y and pointY < easyRect.y + easyRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        currentDiffIndex = 0
                        backGroundSound.play()
                        programState = "game"

            if(pointX > mediumRect.x and pointX < mediumRect.x + mediumRect.width):
                if(pointY > mediumRect.y and pointY < mediumRect.y + mediumRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        currentDiffIndex = 1
                        backGroundSound.play()
                        programState = "game"

            if(pointX > hardRect.x and pointX < hardRect.x + hardRect.width):
                if(pointY > hardRect.y and pointY < hardRect.y + hardRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        currentDiffIndex = 2
                        backGroundSound.play()
                        programState = "game"

            if(pointX > backRect.x and pointX < backRect.x + backRect.width):
                if(pointY > backRect.y and pointY < backRect.y + backRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "startScene"  

            mainSurface.blit(hangarBg, (0, 0))

            mainSurface.blit(difficultySceneBg, (0,0))
            mainSurface.blit(easyText, (315, 185))
            mainSurface.blit(mediumText, (300, 295))
            mainSurface.blit(hardText, (315, 395))        
        

        elif programState == "game":
            frameCount += 1
            enemy_bullet_delay_counter += 1  # Increase the counter for enemy bullets as well
            bossBulletDelayCounter += 1  # Increase the counter for boss bullets as well
            
            #scrolling background moving down
            bgY += 10
            bgY2 += 10

            #scrolling background logic
            if bgY >= surfaceSizeY:
                bgY = -surfaceSizeY
            if bgY2 >= surfaceSizeY:
                bgY2 = -surfaceSizeY

            mainSurface.blit(bg, (0, bgY))
            mainSurface.blit(bg, (0, bgY2))

            if currentDiffIndex == 0:
                if frameCount % 120 == 0 and not bossActive:
                    enemy1PosList.append([random.randint(0, 675), -5])
            if currentDiffIndex == 1:
                if frameCount % 90 == 0 and not bossActive:
                    enemy1PosList.append([random.randint(0, 675), -5])
            if currentDiffIndex == 2:
                if frameCount % 60 == 0 and not bossActive:
                    enemy1PosList.append([random.randint(0, 675), -5])

            if bossActive:  # Only move down if the boss is active
                if bossPos[1] < 100:
                    bossPos[1] += 3  # Update the y-coordinate of boss until it reaches 100y position
                # Draw the health bar background
                pygame.draw.rect(mainSurface, (255, 0, 0), [bossPos[0] +120, bossPos[1] - 20, health_bar_width, health_bar_height])
                # Calculate the health bar width based on current health
                health_bar_fill = int((boss_health / boss_max_health) * health_bar_width)
                # Draw the health bar fill
                pygame.draw.rect(mainSurface, (0, 255, 0), [bossPos[0] +120, bossPos[1] - 20, health_bar_fill, health_bar_height])

            # Check if delay counter reached the delay threshold for enemy bullets
            if enemy_bullet_delay_counter >= enemy_bullet_delay:
                # Reset delay counter
                enemy_bullet_delay_counter = 0
                if enemy1PosList:  # Check if enemy1PosList is not empty
                    for enemyPos in enemy1PosList:  # Iterate through all enemies
                        enemybulletPosList.append([enemyPos[0] + 15, enemyPos[1] + 20])

            if bossBulletDelayCounter >= bossBulletDelay:
                # Reset delay counter
                bossBulletDelayCounter = 0
                if bossActive:  # Check if enemy1PosList is not empty
                    for pos in bossPos:  # Iterate through all bosses
                        enemybulletPosList.append([random.randint(200, 500), bossPos[1]+100])

            for enemybulletPos in enemybulletPosList:
                enemybulletPos[1] += 2  # Move each bullet downwards

            charRect = pygame.Rect(charPos[0], charPos[1], 130 * char1scale, 115 * char1scale)

            for bullet1Pos in bullet1PosList:
                bullet1Pos[1] -= 4  # Move each bullet upwards

            for enemy1Pos in enemy1PosList:
                enemy1rect = pygame.Rect(enemy1Pos[0] + 7, enemy1Pos[1] + 5, 37, 37)
                # pygame.draw.rect(mainSurface, (255, 0, 0), enemy1rect, 2)
                if charRect.colliderect(enemy1rect):  # A collision happens!
                    player_health -= 5  # Reduce player health by 5 on collision
                    enemy1PosList.remove(enemy1Pos)  # Remove the enemy that collided
                    if player_health <= 0:
                        programState = "gameOverScene"

                for bullet1Pos in bullet1PosList:
                    bulletrect = pygame.Rect(bullet1Pos[0] + 20, bullet1Pos[1] + 10, 7, 15)
                    # pygame.draw.rect(mainSurface, (255, 0, 0), bulletrect, 2)
                    if bulletrect.colliderect(enemy1rect):  # A collision happens!
                        score += 1
                        enemy1PosList.remove(enemy1Pos)
                        bullet1PosList.remove(bullet1Pos)
                        break

            for enemyPos in enemy1PosList:
                enemyPos[1] += 2  # Update the y-coordinate of each enemy plane position

            for enemybulletPos in enemybulletPosList:
                enemybulletPos[1] += 5  # Move each enemy bullet downwards
                enemybulletrect = pygame.Rect(enemybulletPos[0] + 5, enemybulletPos[1], 15, 30)
                if charRect.colliderect(enemybulletrect):  # A collision happens!
                    player_health -= 10  # Reduce player health by 10 on collision
                    enemybulletPosList.remove(enemybulletPos)  # Remove the enemy bullet that collided
                    if player_health <= 0:
                        programState = "gameOverScene"

            # timer += 1 # Increase the timer for boss spawn
            # if timer >= 1440 and not bossActive:
            if score >= bossSpawnScore and not bossActive:
                bossActive = True
                bossSpawnScore += 20
                boss_health += bossHealthIncrease  # Increase boss health for subsequent fights
                boss_max_health = boss_health  # Update max health to match current health

            if bossActive:
                bossRect = pygame.Rect(bossPos[0] + 5, bossPos[1], 300, 300)
                # pygame.draw.rect(mainSurface, (255, 0, 0), bossRect, 2)  # Draw the hitbox rectangle
                if charRect.colliderect(bossRect):  # A collision happens!
                    player_health -= 15  # Reduce player health by 15 on collision
                    if player_health <= 0:
                        programState = "gameOverScene"

                for bullet1Pos in bullet1PosList:
                    bulletrect = pygame.Rect(bullet1Pos[0] + 20, bullet1Pos[1] + 10, 7, 15)  # Define bulletrect here
                    # pygame.draw.rect(mainSurface, (255, 0, 0), bulletrect, 2)
                    if bulletrect.colliderect(bossRect):  # Check for collision
                        boss_health -= 5  # Decrease boss health by 1
                        bullet1PosList.remove(bullet1Pos)  # Remove the bullet that collided
                        if boss_health <= 0:  # Check if boss health is zero
                            # Reset boss and return to normal gameplay
                            bossActive = False
                            boss_health = 100
                            bossPos = [200, -50]
                            bossBulletPosList = []
                            # timer = 0
                            # Continue normal gameplay
                            programState = "game"

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_SPACE]:
                shootSound.play()
                # Add new bullet position when spacebar is pressed
                if (frameCount - storeCount) % 40 == 0:
                    bullet1PosList.append([charPos[0], charPos[1]])

            if keys_pressed[pygame.K_UP] and charPos[1] > 0:
                charPos[1] -= 3.5
                char1rectdim[1] -= 3.5
            elif keys_pressed[pygame.K_DOWN] and charPos[1] < surfaceSizeY - char1Rect[3]:
                charPos[1] += 3.5
                char1rectdim[1] += 3.5

            if keys_pressed[pygame.K_LEFT] and charPos[0] > 0:
                charPos[0] -= 3.5
                char1rectdim[0] -= 3.5
                if currentCharIndex == 0:
                    if framecount % char1fr == 0:
                        if char1PatchNumber > 0:  # Ensure we're not going beyond the first patch
                            char1PatchNumber -= 1
                            char1Rect[0] -= char1Rect[2]  # Shift the "display window" to the right along the sprite sheet by the width of the image
                    if framecount % char2fr == 0:
                        if char2PatchNumber > 0:  # Ensure we're not going beyond the first patch
                            char2PatchNumber -= 1
                            char2Rect[0] -= char2Rect[2]  # Shift the "display window" to the right along the sprite sheet by the width of the image
                else:
                    if framecount % char2fr == 0:
                        if char2PatchNumber > 0:  # Ensure we're not going beyond the first patch
                            char2PatchNumber -= 1
                            char2Rect[0] -= char2Rect[2]  # Shift the "display window" to the left along the sprite sheet by the width of the image

            elif keys_pressed[pygame.K_RIGHT] and charPos[0] < surfaceSizeX - char1Rect[3]:
                charPos[0] += 3.5
                char1rectdim[0] += 3.5
                if currentCharIndex == 0:
                    if framecount % char1fr == 0:
                        if char1PatchNumber < char1NumPatches - 1:
                            char1PatchNumber += 1
                            char1Rect[0] += char1Rect[2]  # Shift the "display window" to the right along the sprite sheet by the width of the image
                else:
                    if framecount % char2fr == 0:
                        if char2PatchNumber < char2NumPatches - 1:
                            char2PatchNumber += 1
                            char2Rect[0] += char2Rect[2]  # Shift the "display window" to the right along the sprite sheet by the width of the image
            else:
                if currentCharIndex == 0:
                    char1PatchNumber = 2  # Reset back to middle patch
                    char1Rect[0] = 250 * char1scale  # Reset the rect position of the rect back
                else:
                    char2PatchNumber = 1  # Reset back to middle patch
                    char2Rect[0] = 36*char2scale  # Reset the rect position of the rect back

            #-----------------------------Drawing Everything-------------------------------------#
            # We draw everything from scratch on each frame.

            if currentCharIndex == 0:
                mainSurface.blit(char1spriteSheet, charPos, char1Rect)
            elif currentCharIndex == 1:
                mainSurface.blit(char2SpriteSheet, charPos, char2Rect)

            for bullet1Pos in bullet1PosList:
                mainSurface.blit(bullet, bullet1Pos)

            for enemybulletPos in enemybulletPosList:
                mainSurface.blit(enemybullet, (enemybulletPos[0], enemybulletPos[1]))

            for enemy1Pos in enemy1PosList:
                mainSurface.blit(enemy1, (enemy1Pos[0], enemy1Pos[1]))

            if bossActive:
                mainSurface.blit(bossImage,(bossPos[0], bossPos[1]))
                for enemybulletPos in enemybulletPosList:
                    mainSurface.blit(enemybullet, (bossPos[0] + 100, bossPos[1] + 100))

            # Draw the player's health bar
            # Background
            pygame.draw.rect(mainSurface, (0, 0, 0), [10, 10, player_health_bar_width, player_health_bar_height])
            # Fill
            player_health_bar_fill = int((player_health / player_max_health) * player_health_bar_width)
            pygame.draw.rect(mainSurface, (0, 255, 0), [10, 10, player_health_bar_fill, player_health_bar_height])

            # Render and display the score
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            mainSurface.blit(score_text, (surfaceSizeX - score_text.get_width() - 10, 10))  # Position at top right

        #gamestate when the player loses all their lives
        elif programState == "gameOverScene":
            backButtonRect = pygame.Rect(backButtonDim)
            mainSurface.blit(gameOverScreenBg, (0, 0))
            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            if(pointX > backButtonRect.x and pointX < backButtonRect.x + backButtonRect.width):
                if(pointY > backButtonRect.y and pointY < backButtonRect.y + backButtonRect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        # Reset game state variables
                        programState = "startScene"  # Go directly back to the game
                        charPos = [325, 650]  # Reset player position
                        frameCount = 0  # Reset frame count
                        bullet1PosList = []  # Clear bullet list
                        enemy1PosList = []  # Clear enemy list
                        enemybulletPosList = []  # Clear enemy bullet list
                        lives = 5  # Reset lives
                        player_health = 100  # Reset player health to full
                        boss_health = 100  # Reset boss health to default
                        boss_max_health = 100  # Reset boss max health to default
                        bossActive = False  # Reset boss active flag
                        bossPos = [200, -50]  # Reset boss position
                        bossBulletPosList = []  # Clear boss bullet list
                        # timer = 0
                        score = 0 # Reset score
                        bossSpawnScore = 20 # Reset the bossSpawnScore back to its initial value

            mainSurface.blit(backButton, (600, 600))

            # Render and display the score on the game over screen
            score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
            mainSurface.blit(score_text, (350 - score_text.get_width() // 2, 400 - score_text.get_height() // 2))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

        clock.tick(60)  # Force frame rate to be slower

    pygame.quit()  # Once we leave the loop, close the window.

# Initialize Pygame font module
pygame.font.init()
font = pygame.font.Font(None, 36)

main()