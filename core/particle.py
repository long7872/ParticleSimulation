import pygame
import random
from core.config import PARTICLE_COLOR

class Particle:
    def __init__(self, screen_width, screen_height, radius, mass):
        self.x = random.uniform(radius, screen_width - radius)
        self.y = random.uniform(radius, screen_height - radius)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.radius = radius
        self.mass = mass
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply_force(self, fx, fy):
        # F = m * a ⇒ a = F / m
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax
        self.vy += ay
        
    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Reflect if touch the edge
        if self.x < 0 + self.radius or self.x > self.screen_width - self.radius:
            self.vx *= -1
        if self.y < 0 + self.radius or self.y > self.screen_height - self.radius:
            self.vy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, PARTICLE_COLOR, (int(self.x), int(self.y)), self.radius)
