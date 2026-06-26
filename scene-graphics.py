# Scence Creation and Graphics Module
# 2D scene (house, tree, and sun) 
# A sky, sun, grass, house, and tree are created using rectangles, circles, and polygons.

import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("2DScene") 

# Colors
SKY_BLUE = (135,206,235)
GRASS_GREEN = (34,139,34) 
SUN_YELLOW = (255,255,0) 
HOUSE_BROWN = (139,69,19)
ROOF_RED = (178,34,34)
TREE_BROWN = (101,67,33)
TREE_GREEN = (0,100,0)


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # Draw sky
    screen.fill(SKY_BLUE) 

    # Draw sun
    pygame.draw.circle(screen, SUN_YELLOW,(700,100),50) 

    # Draw grass 
    pygame.draw.rect(screen, GRASS_GREEN, (0,400,800,200)) 

    # Draw house
    pygame.draw.rect(screen, HOUSE_BROWN, (300,300,200,150)) 
    pygame.draw.polygon(screen, ROOF_RED, [(300,300),(400,250),(500,300)]) 
    pygame.draw.rect(screen, (0,0,0),(380,380,40,70)) # Door  
    pygame.draw.rect(screen, (135,206,250),(320,320,40,30)) # Window 
    pygame.draw.rect(screen, (135,206,250),(440,320,40,30)) # Window 

    # Draw tree
    pygame.draw.rect(screen, TREE_BROWN, (150,350,30,100)) # Trunk 
    pygame.draw.circle(screen, TREE_GREEN, (165,300),50) # Leaves 
    pygame.draw.circle(screen, TREE_GREEN, (120,320),40) # Leaves 
    pygame.draw.circle(screen, TREE_GREEN, (210,320),40) # Leaves 

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
# END 



# FULL FINAL SCENE 
import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Advanced Animated 2D Scene")
clock = pygame.time.Clock()

# COLORS
DAY_SKY = (135, 206, 235)
NIGHT_SKY = (15, 20, 60)
GRASS_GREEN = (34, 139, 34)
SUN_YELLOW = (255, 255, 0)
MOON_WHITE = (220, 220, 220)
STAR_WHITE = (255, 255, 255)
CLOUD_WHITE = (245, 245, 245)
CHAR_COLOR = (0, 0, 0)

# VARIABLES
sun_x = 0
cloud_x = 0
bird_x = -100

char_x, char_y = 380, 420
char_speed = 4
leg_angle = 0
leg_dir = 1

time_val = 0

# Stars
stars = [(random.randint(0, 800), random.randint(0, 300)) for _ in range(60)]

# Rain / Snow
particles = [[random.randint(0, 800), random.randint(0, 600)] for _ in range(100)]

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- DAY–NIGHT CYCLE --------
    time_val += 0.002
    t = (math.sin(time_val) + 1) / 2

    sky = (
        int(DAY_SKY[0] * t + NIGHT_SKY[0] * (1 - t)),
        int(DAY_SKY[1] * t + NIGHT_SKY[1] * (1 - t)),
        int(DAY_SKY[2] * t + NIGHT_SKY[2] * (1 - t))
    )
    screen.fill(sky)

    # -------- STARS (NIGHT ONLY) --------
    if t < 0.4:
        for s in stars:
            pygame.draw.circle(screen, STAR_WHITE, s, 2)

    # -------- SUN / MOON --------
    sun_x += 0.5
    if sun_x > 900:
        sun_x = -100

    if t > 0.5:
        pygame.draw.circle(screen, SUN_YELLOW, (int(sun_x), 100), 40)
    else:
        pygame.draw.circle(screen, MOON_WHITE, (int(sun_x), 100), 30)

    # -------- CLOUDS --------
    cloud_x += 0.3
    if cloud_x > 900:
        cloud_x = -200

    pygame.draw.circle(screen, CLOUD_WHITE, (int(cloud_x), 130), 25)
    pygame.draw.circle(screen, CLOUD_WHITE, (int(cloud_x + 30), 120), 30)
    pygame.draw.circle(screen, CLOUD_WHITE, (int(cloud_x + 60), 130), 25)

    # -------- BIRDS --------
    bird_x += 1
    if bird_x > 900:
        bird_x = -100

    pygame.draw.arc(screen, (0, 0, 0), (bird_x, 180, 20, 10), math.pi, 2*math.pi, 2)
    pygame.draw.arc(screen, (0, 0, 0), (bird_x + 15, 180, 20, 10), math.pi, 2*math.pi, 2)

    # -------- RAIN / SNOW --------
    for p in particles:
        if t > 0.5:  # rain (day)
            pygame.draw.line(screen, (180, 180, 255), (p[0], p[1]), (p[0], p[1] + 8))
            p[1] += 8
        else:  # snow (night)
            pygame.draw.circle(screen, (255, 255, 255), p, 2)
            p[1] += 2

        if p[1] > 600:
            p[0] = random.randint(0, 800)
            p[1] = random.randint(-50, 0)

    # -------- GROUND --------
    pygame.draw.rect(screen, GRASS_GREEN, (0, 450, 800, 150))

    # -------- CHARACTER MOVEMENT --------
    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        char_x -= char_speed
        moving = True
    if keys[pygame.K_RIGHT]:
        char_x += char_speed
        moving = True

    # Walking animation
    if moving:
        leg_angle += 5 * leg_dir
        if abs(leg_angle) > 20:
            leg_dir *= -1
    else:
        leg_angle = 0

    # Body
    pygame.draw.rect(screen, CHAR_COLOR, (char_x, char_y, 20, 30))
    pygame.draw.circle(screen, CHAR_COLOR, (char_x + 10, char_y - 10), 8)

    # Legs
    pygame.draw.line(screen, CHAR_COLOR,
                     (char_x + 5, char_y + 30),
                     (char_x + 5 + leg_angle, char_y + 50), 3)
    pygame.draw.line(screen, CHAR_COLOR,
                     (char_x + 15, char_y + 30),
                     (char_x + 15 - leg_angle, char_y + 50), 3)

    pygame.display.flip()

pygame.quit()
# END 


