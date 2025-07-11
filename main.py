from constants import *
from ball import *
import random
import pygame
import sys
from text import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    balls = pygame.sprite.Group()

    update = brute_update
    gravity = GRAVITY_DOWN
    text_font = pygame.font.SysFont("Arial", 30)
    hud = True

    dt = 0

    Ball.containers = (updatables, drawables, balls)

    count = 0
    for i in range(RADIUS, SCREEN_HEIGHT - RADIUS, 3 * RADIUS):
        for j in range(RADIUS, SCREEN_WIDTH - RADIUS, 3 * RADIUS):
            if count < COUNT:
                Ball("blue", pygame.Vector2(j, i), pygame.Vector2(0, 0))
                count += 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            gravity = GRAVITY_UP
        elif keys[pygame.K_DOWN]:
            gravity = GRAVITY_DOWN
        elif keys[pygame.K_LEFT]:
            gravity = GRAVITY_LEFT
        elif keys[pygame.K_RIGHT]:
            gravity = GRAVITY_RIGHT
        elif keys[pygame.K_SPACE]:
            gravity = ZERO
        elif keys[pygame.K_0]:
            hud = not hud

        for _ in range(SUBSTEPS):
            subdt = dt / SUBSTEPS

            #UPDATES DESIRED DETECTION ALGORITHM BASED ON KEYBOARD INPUT
            if keys[pygame.K_1]:
                update = brute_update
            elif keys[pygame.K_2]:
                update = sweep_update
            elif keys[pygame.K_3]:
                update = grid_update

            for updatable in updatables:
                updatable.update(gravity, subdt)

            if update == brute_update:
                update(balls)
                on = 1
            elif update == sweep_update:
                update(sweep_and_prune(balls))
                on = 2
            else:
                update(gridform(balls))
                on = 3

        screen.fill((20, 20, 20))
        for drawable in drawables:
            drawable.draw(screen)

        if hud:
            draw_text(screen, "B-F", text_font, (255, 0, 0) if on == 1 else (100, 0, 0), 10, 0)
            draw_text(screen, "S&P", text_font, (0, 255, 0) if on == 2 else (0, 100, 0), 10, 30)
            draw_text(screen, "GRID", text_font, (0, 0, 255) if on == 3 else (0, 0, 100), 10, 60)

        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()