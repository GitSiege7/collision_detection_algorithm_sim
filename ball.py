from constants import *

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
        
    def update(self):
        #X BOUNDARY
        if self.pos.x - self.radius <= 0 or self.pos.x + self.radius >= SCREEN_WIDTH:
            self.vel.x *= -1 * ELASTICITY

        #Y BOUNDARY
        if self.pos.y + self.radius >= SCREEN_HEIGHT:
            if abs(self.vel.y) < 0.2:
                self.vel.y = 0
            else:
                self.pos.y = SCREEN_HEIGHT - self.radius
                self.vel.y *= -1 * ELASTICITY
                self.vel += GRAVITY
        elif self.pos.y - self.radius <= 0:
            self.vel.y *= -1 * ELASTICITY
            self.vel += GRAVITY
        else:
            self.vel += GRAVITY

        self.pos += self.vel