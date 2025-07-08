import pygame

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
GRAVITY_DOWN = pygame.Vector2(0, 1)
GRAVITY_UP = pygame.Vector2(0, -1)
GRAVITY_LEFT = pygame.Vector2(-1, 0)
GRAVITY_RIGHT = pygame.Vector2(1, 0)
ELASTICITY = 0.7
AIR_REST = 0.99
RADIUS = 8
COUNT = 0