from constants import *
import math
import threading

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
        
    def update(self, gravity, balls):
        #CHECK X BOUNDARIES
        if self.pos.x + self.radius >= SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH - self.radius
            self.vel.x *= -ELASTICITY
        elif self.pos.x - self.radius <= 0:
            self.pos.x = self.radius
            self.vel.x *= -ELASTICITY

        #CHECK Y BOUNDARIES
        if self.pos.y + self.radius >= SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT - self.radius
            self.vel.y *= -ELASTICITY
        elif self.pos.y - self.radius <= 0:
            self.pos.y = self.radius
            self.vel.y *= -ELASTICITY

        #APPLY AIR RESISTANCE & GRAVITY
        self.vel.x *= AIR_RES
        self.vel.y *= AIR_RES
        self.vel.x += gravity.x
        self.vel.y += gravity.y

        visited = []
        #COLLISION & REPULSION
        for other in balls:
            #DON'T CHECK CONDITION AGAINST SELF
            if other == self or other in visited:
                continue
            
            dist = pygame.Vector2.distance_to(self.pos, other.pos)
            if dist <= self.radius * 2:
                dist_v = other.pos - self.pos
                normal = dist_v.normalize()
                tangent = pygame.Vector2(-normal.y, normal.x)

                v1n = normal.dot(self.vel)
                v1t = tangent.dot(self.vel)
                v2n = normal.dot(other.vel)
                v2t = tangent.dot(other.vel)

                v1n_after = v2n
                v2n_after = v1n

                v1_after = v1n_after * normal + v1t * tangent
                v2_after = v2n_after * normal + v2t * tangent

                self.vel = v1_after
                other.vel = v2_after

                #OVERLAP RESOLUTION
                overlap = self.radius * 2 - dist
                if overlap > 0:
                    correction = normal * (overlap / 2)
                    self.pos -= correction
                    other.pos += correction


            visited.append(other)


        #UPDATE POS
        self.pos += self.vel

        #UPDATE COLOR
        #self.color = self.get_color()


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