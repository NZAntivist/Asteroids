import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(angle)
        new_direction_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_direction_1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_direction_2 * 1.2
