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
        
        random_angle = random.uniform(20,50)
        left_direction = self.velocity.rotate(random_angle)
        right_direction = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left_direction * 1.2
        right_asteroid.velocity = right_direction * 1.2