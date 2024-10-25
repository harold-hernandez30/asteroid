
import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20, 50)
            firstSplitVelocity = self.velocity.rotate(random_angle) * 1.2
            secondSplitVelocity = self.velocity.rotate(-random_angle) * 1.2
            firstSplitAsteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            firstSplitAsteroid.velocity = firstSplitVelocity
            secondSplitAsteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            secondSplitAsteroid.velocity = secondSplitVelocity
            self.kill()