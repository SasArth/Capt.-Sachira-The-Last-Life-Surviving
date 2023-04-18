import pygame
import math
import random
import sys
import os

#exe conv
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#assets
BackMusic = resource_path('assets\Background.wav')
FireSnd = resource_path('assets\FireSound.flac')
Exp1Snd = resource_path('assets\Explosion.wav')
Exp2Snd = resource_path('assets\explosion2.wav')
fnt = resource_path('assets\space age.ttf')
plyr = resource_path('assets\player.png')
enmy= resource_path('assets\enemy.png')
pr = resource_path('assets\proj.png')
stsc1 = resource_path('assets\strscr1.png')
stsc2 = resource_path('assets\strscr2.png')
bd = resource_path('assets\cod.png')
govr = resource_path('assets\Gameover.png')
lvs = resource_path('assets\Lives.png')

pygame.init()

#'''
# Add sound
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load(BackMusic)
pygame.mixer.music.play(-1)

firesound = pygame.mixer.Sound(FireSnd) 
def fire():
    pygame.mixer.Sound.play(firesound)

explosionsound = pygame.mixer.Sound(Exp1Snd)
def explosion():
    pygame.mixer.Sound.play(explosionsound)

explosionsound2 = pygame.mixer.Sound(Exp2Snd)
def explosion2():
    pygame.mixer.Sound.play(explosionsound2)

# Set up the display window
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 780
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Capt. Sachira: Last Life Remaining")

# Set up the font
font = pygame.font.Font(fnt, 40)
font2 = pygame.font.Font(fnt, 80)
font3 = pygame.font.Font(fnt, 20)

# Load the player sprite
player_image = pygame.image.load(plyr)
#player_rect = player_image.get_rect()

# Set the starting position and speed of the player sprite
playerini_x = WINDOW_WIDTH / 2
playerini_y = WINDOW_HEIGHT - 50
player_x = playerini_x
player_y = playerini_y
player_cruisespeed = 1
player_speed = player_cruisespeed
player_highspeed = 1.5
player_lowspeed = 0.5
player_ini_rotation = 0
player_rotation = player_ini_rotation
rotation_speed = 0.6
score = 0         

#setting up enemy
enemy_sprite = pygame.image.load(enmy)
# set the enemy's initial position and speed
#enemy_pos = [random.randint(0, WINDOW_WIDTH - enemy_sprite.get_width()), random.randint(0, WINDOW_HEIGHT - enemy_sprite.get_height())]
enemy_speed = 0.5
enemy_rotation = random.randint(0, 360)
enemy_rotation_speed = 0.2
enemies = []
enrec = []
burec = []
NoOfEnemy = 1
eKill = 0

# Set up the bullets list
bullets = []
bullet_speed = 5

# Load the projectile sprite
bullet_image =  pygame.image.load(pr).convert_alpha()
#projectile_rect = bullet_image.get_rect()

# Set up the clock
clock = pygame.time.Clock()

# Set the rotation and speed step values
rotation_step = 5
speed_step = 1

# Set the projectile speed and cooldown values
projectile_speed = 10
projectile_cooldown = 30
projectile_timer = 0
projectile_speed = []

strscr1 = pygame.image.load(stsc1)
strscr2 = pygame.image.load(stsc2).convert()
strscr1_rect = strscr1.get_rect()
strscr2_rect = strscr2.get_rect()
redbod = pygame.image.load(bd)
redbod_rect = redbod.get_rect()
gmovrscr = pygame.image.load(govr)
gmovrscr_rect = gmovrscr.get_rect()
lives = pygame.image.load(lvs).convert()
#lives = lives.get_rect()
greenColor = (0,255,0)
redColor = (255,0,0)
lghtredColor = (240, 128, 128)
yellowColor = (255,255,0)
OHColor = greenColor
shtsfrd = 0
shtsmul = 50
shtscldwn = 0.6
OHLimit = False
OhBrWidth = 0


showstartscreen1 = True
showstartscreen2 = True
running = True
game = True
while showstartscreen1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            showstartscreen1 = False
            showstartscreen2 = False
            game = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_SPACE):
                showstartscreen1 = False
    screen.fill((0, 0, 0)) 
    screen.blit(strscr1, strscr1_rect)
    pygame.display.flip()


#showstartscreen2 = True
while showstartscreen2:
    #screen.blit(strscr2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            showstartscreen1 = False
            showstartscreen2 = False
            game = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_SPACE):
                showstartscreen2 = False
    screen.fill((0, 0, 0)) 
    screen.blit(strscr2, strscr2_rect)
    pygame.display.flip()


# Game loop
#running = True

while game:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
                gameover = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_KP0) or (event.key == pygame.K_RSHIFT) or (event.key == pygame.K_LSHIFT):
                    player_speed = player_cruisespeed
            '''
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
            # Create a new bullet and add it to the list
                    bullets.append({
                        "pos": [player_x, player_y],  # copy the player's current position
                        "angle": player_rotation
                    })
                    #shsound.play()
                    # Decrement the projectile cooldown timer
                '''



        # Update the game state
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rotation += rotation_speed
        if keys[pygame.K_RIGHT]:
            player_rotation -= rotation_speed
        if keys[pygame.K_UP]:
            player_speed *= 2
            if player_speed > player_highspeed:
                player_speed = player_highspeed
        if keys[pygame.K_DOWN]:
            player_speed /= 2
            if player_speed<player_lowspeed:
                player_speed = player_lowspeed
        '''
        if keys[pygame.K_SPACE] and projectile_timer <= 0:
            bullet_rect = bullet_image.get_rect()
            bullet_rect.midbottom = player_rect.midtop
            bullets.append(bullet_rect)
            projectile_timer = projectile_cooldown
        '''
        if keys[pygame.K_SPACE] and projectile_timer <= 0 and OHLimit == False:
            # Create a new bullet and add it to the list
                    bullets.append({
                        "pos": [player_x, player_y],  # copy the player's current position
                        "angle": player_rotation
                    })
                    fire()
                    projectile_timer = projectile_cooldown
                    shtsfrd = shtsfrd + shtsmul
                    # Decrement the projectile cooldown timer
        if projectile_timer > 0:
            projectile_timer -= 1
        if shtsfrd > 0:
            shtsfrd -= shtscldwn
        if shtsfrd >800:
            OHLimit = True
            OHColor = redColor
        if shtsfrd >600 and OHLimit==False:
            OHColor = lghtredColor

        if shtsfrd<600 and shtsfrd>300 and OHLimit==False:
            OHColor = yellowColor
        
        if shtsfrd<300:
            OHColor = greenColor
            OHLimit = False
        OhBrWidth = shtsfrd*0.25
        

            

        
        

        # Fill the background with black
        screen.fill((0, 0, 0))

            
        # Move the bullets
        burec.clear()
        for bullet in bullets:
            bullet["pos"][0] += bullet_speed * -math.sin(math.radians(bullet["angle"]))
            bullet["pos"][1] -= bullet_speed * math.cos(math.radians(bullet["angle"]))
        # Render the bullet sprite
            bullet_rect = bullet_image.get_rect(center=bullet["pos"])
            burec.append(bullet_rect)
            screen.blit(bullet_image, bullet_rect)

            # Remove the bullet from the list if it has gone off-screen
            if bullet_rect.left > WINDOW_WIDTH or bullet_rect.right < 0 or bullet_rect.top > WINDOW_HEIGHT or bullet_rect.bottom < 0:
                bullets.remove(bullet)
        # Move the player sprite based on its current rotation and speed
        player_x += player_speed * -math.sin(math.radians(player_rotation))
        if player_x < 0:
            player_x=0
            screen.blit(redbod,redbod_rect)
        if player_x > WINDOW_WIDTH:
            player_x=WINDOW_WIDTH
            screen.blit(redbod,redbod_rect)
        player_y += player_speed * -math.cos(math.radians(player_rotation))
        if player_y < 0:
            player_y = 0
            screen.blit(redbod,redbod_rect)
        if player_y > WINDOW_HEIGHT:
            player_y=WINDOW_HEIGHT
            screen.blit(redbod,redbod_rect)

        # Add enemies randomly
        #if len(enemies) < 1 and random.randint(0, 100) < 10:
        if len(enemies) <NoOfEnemy and random.randint(0, 100 )<1:
            enemies.append({
                        "pos": random.choice([[random.choice([random.randint(-3, 0),random.randint(WINDOW_WIDTH , WINDOW_WIDTH + 3)]), random.randint(0,WINDOW_HEIGHT)],
                                                [random.randint(0,WINDOW_HEIGHT), random.choice([random.randint(-3, 0),random.randint(WINDOW_HEIGHT , WINDOW_HEIGHT + 3)])]]),  # copy the player's current position
                        "angle": random.randint(0,360)
                    })
            
            '''
            enemy_rect = enemy_sprite.get_rect()
            enemy_rect.x = random.randint(0, WINDOW_WIDTH - enemy_rect.width)
            enemy_rect.y = random.randint(0, WINDOW_HEIGHT - enemy_rect.height)
            enemies.append(enemy_rect)
            print(enemies)
            '''

        # Move the enemies and check for collisions with bullets
        enrec.clear()
        for enemy in enemies:
            enemy_vel = pygame.math.Vector2(player_x - enemy["pos"][0], player_y - enemy["pos"][1]).normalize() * enemy_speed
            enemy["pos"][0] += enemy_vel.x
            enemy["pos"][1] += enemy_vel.y
            enemy_angle = math.degrees(math.atan2(enemy_vel.x, enemy_vel.y)) +180
            enemy_rect = enemy_sprite.get_rect(center=enemy["pos"])
            enrec.append(enemy_rect)
            screen.blit(pygame.transform.rotate(enemy_sprite, enemy_angle),enemy_rect )

        for enemy_rect in enrec:
            for bullet_rect in burec:
                if enemy_rect.colliderect(bullet_rect):
                    bullets.pop(burec.index(bullet_rect))
                    burec.remove(bullet_rect)
                    enemies.pop(enrec.index(enemy_rect))
                    enrec.remove(enemy_rect)
                    score = score + 10
                    eKill = eKill + 1
                    explosion2()
                    #print(score)


                    #print("likill")
        #'''

        #increasing No. of enemies
        if eKill>19:
            NoOfEnemy = NoOfEnemy + 1
            eKill = 0


        for enemy_rect in enrec:
            if enemy_rect.colliderect(player_rect):
                enemies.pop(enrec.index(enemy_rect))
                enrec.remove(enemy_rect)
                player_rect
                explosion()

                running = False
                gameover = True
        #''' 
        # Draw the screen
        #screen.fill((0, 0, 0))  # Fill the screen with black
        rotated_player_image = pygame.transform.rotate(player_image, player_rotation)
        player_rect = rotated_player_image.get_rect(center=(player_x, player_y))
        screen.blit(rotated_player_image, player_rect)  # Draw the player sprite
        # Draw score
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        GHText = font3.render("Gun OverHeat", True, (255, 255, 255))
        screen.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10, 10))
        screen.blit(lives, (WINDOW_WIDTH - score_text.get_width() - 10, 80))
        screen.blit(GHText, (25, 25))
        pygame.draw.rect(screen, OHColor, pygame.Rect(25,25 + GHText.get_height() , OhBrWidth, 20))
        pygame.display.flip()  # Update the display
        #print(len(enrec))
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                gameover=False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_SPACE):
                    gameover=False
                    running = True
                    score = 0
                    player_x = playerini_x
                    player_y = playerini_y
                    player_rotation = player_ini_rotation
                    NoOfEnemy = 1
                    player_speed = player_cruisespeed
                    enrec.clear()
                    enemies.clear()
                    burec.clear()
                    bullets.clear()
                    shtsfrd = 0
                    
        screen.fill((0, 0, 0)) 
        screen.blit(gmovrscr, gmovrscr_rect)
        score_text = font2.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, ((WINDOW_WIDTH - score_text.get_width())/2 , WINDOW_HEIGHT/2))
        creator = font3.render("Creators:- Atharva Sasane and Ruchira Purohit", True, (255, 255, 255))
        screen.blit(creator, ((WINDOW_WIDTH - creator.get_width()-10) , WINDOW_HEIGHT-80))
        pygame.display.flip()
pygame.quit()
  
    

