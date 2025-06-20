import pygame
import random
from core.config import PARTICLE_COLORS, PARTICLE_DAMPING

class Particle:
    def __init__(self, screen_width, screen_height, radius, type, mass):
        self.x = random.uniform(radius, screen_width - radius)
        self.y = random.uniform(radius, screen_height - radius)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.radius = radius
        self.mass = mass
        self.type = type
        self.color = PARTICLE_COLORS.get(type)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply_force(self, fx, fy):
        # F = m * a ⇒ a = F / m
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax
        self.vy += ay
        
    def update(self, damping):
        # decrease velocity
        self.vx *= damping
        self.vy *= damping
        
        self.x += self.vx
        self.y += self.vy

        # Reflect if touch the edge
        # if self.x < 0 or self.x > self.screen_width:
        #     self.vx *= -1
        # if self.y < 0 or self.y > self.screen_height:
        #     self.vy *= -1
        
        # Wrap-around x-axis 
        if self.x < 0:
            self.x += self.screen_width
        elif self.x > self.screen_width:
            self.x -= self.screen_width

        # Wrap-around y-axis
        if self.y < 0:
            self.y += self.screen_height
        elif self.y > self.screen_height:
            self.y -= self.screen_height

    
    def draw(self, surface):
        def draw_with_alpha(x, y, alpha):
            temp_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            r, g, b = self.color
            pygame.draw.circle(temp_surface, (r, g, b, alpha), (self.radius, self.radius), self.radius)
            surface.blit(temp_surface, (x - self.radius, y - self.radius))

        # Vẽ chính giữa
        draw_with_alpha(self.x, self.y, 255)

        margin = self.radius

        # Wrap theo chiều ngang
        if self.x < margin:
            draw_with_alpha(self.x + self.screen_width, self.y, 128)
        elif self.x > self.screen_width - margin:
            draw_with_alpha(self.x - self.screen_width, self.y, 128)

        # Wrap theo chiều dọc
        if self.y < margin:
            draw_with_alpha(self.x, self.y + self.screen_height, 128)
        elif self.y > self.screen_height - margin:
            draw_with_alpha(self.x, self.y - self.screen_height, 128)

        # Wrap chéo ở góc (nếu gần cả x và y mép)
        if self.x < margin and self.y < margin:
            draw_with_alpha(self.x + self.screen_width, self.y + self.screen_height, 64)
        elif self.x > self.screen_width - margin and self.y < margin:
            draw_with_alpha(self.x - self.screen_width, self.y + self.screen_height, 64)
        elif self.x < margin and self.y > self.screen_height - margin:
            draw_with_alpha(self.x + self.screen_width, self.y - self.screen_height, 64)
        elif self.x > self.screen_width - margin and self.y > self.screen_height - margin:
            draw_with_alpha(self.x - self.screen_width, self.y - self.screen_height, 64)
