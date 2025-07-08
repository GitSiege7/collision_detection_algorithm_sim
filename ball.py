from constants import *
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, pos, vel):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.radius = RADIUS
        self.color = color
        self.pos = pos
        self.vel = vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        
    def update(self, gravity):
        #X BOUNDARY
        if self.pos.x + self.radius >= SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH - self.radius
            self.vel.x *= -1 * ELASTICITY
            self.vel.x += gravity.x
        elif self.pos.x - self.radius <= 0:
            self.pos.x = self.radius
            self.vel.x *= -1 * ELASTICITY
            self.vel.x += gravity.x
        else:
            self.vel.x += gravity.x

        self.vel.x *= AIR_REST

        #Y BOUNDARY
        if self.pos.y + self.radius >= SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT - self.radius
            self.vel.y *= -1 * ELASTICITY
            self.vel.y += gravity.y
        elif self.pos.y - self.radius <= 0:
            self.pos.y = self.radius
            self.vel.y *= -1 * ELASTICITY
            self.vel.y += gravity.y
        else:
            self.vel.y += gravity.y

        self.vel.y *= AIR_REST

        self.pos += self.vel

        self.color = self.get_color()


    def get_color(self):
        velocity = math.sqrt(pow(self.vel.x, 2) + pow(self.vel.y, 2))
        
        if (velocity > 60):
            return (175, 175, 255)
        elif (velocity > 55):
            return (160, 160, 255)
        elif (velocity > 50):
            return (145, 145, 255)
        elif (velocity > 45):
            return (130, 100, 255)
        elif (velocity > 40):
            return (115, 115, 255)
        elif (velocity > 35):
            return (100, 100, 255)
        elif (velocity > 30):
            return (85, 85, 255)
        elif (velocity > 25):
            return (70, 70, 255)
        elif (velocity > 20):
            return (55, 55, 255)
        elif (velocity > 15):
            return (40, 40, 255)
        elif (velocity > 10):
            return (25, 25, 255)
        elif (velocity > 5):
            return (10, 10, 255)
        else:
            return (0, 0, 255)