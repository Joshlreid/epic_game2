import pygame
import pygame.time
import sys
import random
from settings import *
from plane import Plane
from planes import Enemies, planes
from bullet import Bullet

pygame.init()

# background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 80)
score_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 40)
pygame.display.set_caption("Planes!")
mountain = pygame.image.load("assets/images/mountain1.png").convert()
point_mountain = pygame.image.load("assets/images/pointy_mountains.png").convert()
mountain.set_colorkey((0, 0, 0))
point_mountain.set_colorkey((0, 0, 0))

gunshot = pygame.mixer.Sound('assets/sounds/gun-gunshot-01.wav')
explosion = pygame.mixer.Sound('assets/sounds/explosion.wav')
lose = pygame.mixer.Sound('assets/sounds/lose.wav')
win = pygame.mixer.Sound('assets/sounds/win.wav')
background_sound = pygame.mixer.Sound('assets/sounds/background.wav')
background_sound.play()

score = 0
death = 0


# time

# moving objects
main_plane = Plane(300, 300)
for _ in range(NUM_PLANES):
    planes.add(Enemies(random.randint(0, SCREEN_WIDTH),
                      random.randint(0, SCREEN_HEIGHT)))

# drawing background
background = screen.copy()
def draw_background():
    background.fill(SKY_COLOR)
    background.blit(point_mountain, (0, 432))
    background.blit(mountain, (250, 294))

draw_background()

shot_group = pygame.sprite.Group()

# looking for events while alive and score is less than amount of enemy planes
while death == 0 and score < NUM_PLANES:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("no mo play")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                main_plane.moving_left = True
            if event.key == pygame.K_d:
                main_plane.moving_right = True
            if event.key == pygame.K_w:
                main_plane.moving_up = True
            if event.key == pygame.K_s:
                main_plane.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                main_plane.moving_left = False
            if event.key == pygame.K_d:
                main_plane.moving_right = False
            if event.key == pygame.K_w:
                main_plane.moving_up = False
            if event.key == pygame.K_s:
                main_plane.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gunshot.play()
            x = Bullet(-200, 0)
            x.shoot(main_plane.rect.center, pygame.mouse.get_pos())
            shot_group.add(x)

    # getting time for top left screen
    screen.blit(background, (0, 0))
    time = pygame.time.get_ticks() // 1000
    text = score_font.render(f"{time}", True, (0, 0, 0))
    screen.blit(text, (0, 0))

    main_plane.update()
    planes.update()
    shot_group.update()

    killed_planes = pygame.sprite.groupcollide(shot_group, planes, True, True)
    score += len(killed_planes)

    if len(killed_planes) > 0:
        explosion.play()
        print(f'You have killed {score} planes!')


    hits = pygame.sprite.spritecollide(main_plane, planes, False)
    death += len(hits)

    if time < 2:
        score = 0
        death = 0

    main_plane.draw(screen)
    planes.draw(screen)
    shot_group.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# win and lose
if death > 0:
    print('You Lose!')
    lose.play()
    background_sound.set_volume(0.0001)
    lose_text = game_font.render("You Lose!", True, (255, 69, 0))
    screen.blit(lose_text, (160, 220))

else:
    print('You Win!')
    win.play()
    background_sound.set_volume(0.0001)
    win_text = game_font.render("You Win!", True, (255, 69, 0))
    screen.blit(win_text, (160, 220))
pygame.display.update()

main_plane.draw(screen)
planes.draw(screen)
shot_group.draw(screen)

pygame.display.flip()
pygame.time.Clock().tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("no mo play")
            pygame.quit()
            sys.exit()

