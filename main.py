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

    gravity = GRAVITY_DOWN

    Ball.containers = (updatables, drawables)

    for i in range(0, COUNT):
        ball = Ball("blue", pygame.Vector2(random.randint(math.floor(SCREEN_WIDTH//4), math.floor(SCREEN_WIDTH/1.5)), random.randint(math.floor(SCREEN_HEIGHT//4), math.floor(SCREEN_HEIGHT/1.5))), pygame.Vector2(0, 0))

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
            ball = Ball("blue", pygame.Vector2(RADIUS, SCREEN_HEIGHT/4), pygame.Vector2(50, 0))

        screen.fill("black")

        for updatable in updatables:
            updatable.update(gravity)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()