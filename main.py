from constants import *
from ball import *
import random
import pygame
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    balls = pygame.sprite.Group()

    gravity = GRAVITY_DOWN

    dt = 0

    Ball.containers = (updatables, drawables, balls)

    count = 0
    for i in range(math.floor(SCREEN_HEIGHT/4), math.floor(SCREEN_HEIGHT/1.5), 3 * RADIUS):
        for j in range(math.floor(SCREEN_WIDTH/4), math.floor(SCREEN_WIDTH/1.5), 3 * RADIUS):
            if count < COUNT:
                Ball("blue", pygame.Vector2(j, i), pygame.Vector2(0, 0))
                count += 1

    while True:
        dt = clock.tick(60)/1000

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
        elif keys[pygame. K_SPACE]:
            gravity = ZERO

        for _ in range(SUBSTEPS):
            sweep = sweep_and_prune(balls)

            subdt = dt / SUBSTEPS

            for updatable in updatables:
                updatable.update(gravity, subdt)

            update(sweep)

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()