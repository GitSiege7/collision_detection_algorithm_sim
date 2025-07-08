from constants import *
from ball import *
import pygame
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Ball.containers = (updatables, drawables)

    ball = Ball("white", pygame.Vector2(SCREEN_WIDTH/2, RADIUS), pygame.Vector2(3, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")

        for updatable in updatables:
            updatable.update()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()