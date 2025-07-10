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
        
    def update(self, gravity, sweep):
        #CHECK SCREEN BOUNDS
        self.check_bounds(gravity)

        #COLLISION CHECK AND RESOLUTION
        for list in sweep:
            for i in range (0, len(list)):
                for j in range(i, len(list)):
                    list[i].collision(list[j])


        #UPDATE POS
        self.update_pos()

        #UPDATE COLOR
        self.update_color()


    def collision(self, other):
        if other == self:
            return
            
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


    def check_bounds(self, gravity):
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


    def update_pos(self):
        self.pos += self.vel


    def update_color(self):
        velocity = math.sqrt(pow(self.vel.x, 2) + pow(self.vel.y, 2))
        
        if (velocity > 60):
            self.color = (175, 175, 255)
        elif (velocity > 55):
            self.color = (160, 160, 255)
        elif (velocity > 50):
            self.color = (145, 145, 255)
        elif (velocity > 45):
            self.color = (130, 100, 255)
        elif (velocity > 40):
            self.color = (115, 115, 255)
        elif (velocity > 35):
            self.color = (100, 100, 255)
        elif (velocity > 30):
            self.color = (85, 85, 255)
        elif (velocity > 25):
            self.color = (70, 70, 255)
        elif (velocity > 20):
            self.color = (55, 55, 255)
        elif (velocity > 15):
            self.color = (40, 40, 255)
        elif (velocity > 10):
            self.color = (25, 25, 255)
        elif (velocity > 5):
            self.color = (10, 10, 255)
        else:
            self.color = (0, 0, 255)

        return


def sweep_and_prune(balls):
    balls_sorted = sorted(balls, key=lambda ball: ball.pos.x)
    
    sweep = [[]]
    sweep_i = 0
    for i in range(0, len(balls_sorted)):
        j = i + 1

        for j in range(i + 1, len(balls_sorted)):
            if (balls_sorted[j].pos.x - RADIUS) < (balls_sorted[i].pos.x + RADIUS):
                if balls_sorted[i] not in sweep[sweep_i]:
                    sweep[sweep_i] = [balls_sorted[i], balls_sorted[j]]
                    i += 1
                    j += 1
                else:
                    sweep[sweep_i].append(balls_sorted[j])
        sweep_i += 1
        i = j + 1

        sweep.append([])

    return sweep