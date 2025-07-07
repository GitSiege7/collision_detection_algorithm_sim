from constants import *
import pygame
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    ball = {
        "pos" : pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
        "vel" : pygame.Vector2(0, 0),
        "radius" : 50
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #x boundary check
        if ball["pos"].x - ball["radius"] < 0:
            ball["vel"].x = -1 * ELASTICITY * ball["vel"].x
        elif ball["pos"].x + ball["radius"] > SCREEN_WIDTH:
            ball["vel"].x = -1 * ELASTICITY * ball["vel"].x

        #y boundary check
        if ball["pos"].y - ball["radius"] < 0:            
            ball["vel"].y = -1 * ELASTICITY * ball["vel"].y
        elif ball["pos"].y + ball["radius"] > SCREEN_HEIGHT:
            ball["vel"].y = -1 * ELASTICITY * ball["vel"].y

        ball["vel"] += GRAVITY
        ball["pos"] += ball["vel"]


        screen.fill("black")
        pygame.draw.circle(screen, "white", ball["pos"], ball["radius"])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()