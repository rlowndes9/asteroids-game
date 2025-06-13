from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(velocity)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, newRadius, (velocity * 1.2))
        Asteroid(self.position.x, self.position.y, newRadius, (velocity2 * 1.2))