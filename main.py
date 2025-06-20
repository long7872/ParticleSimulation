import pygame
import random
import sys
from core.particle import Particle
from core.physics import (
    resolve_collision, 
    compute_force, 
    get_interaction,
)
from core.config import (
    PARTICLE_DAMPING,
    PARTICLE_RADIUS,
    PARTICLE_MASS,
    INTERACTION_DISTANCE,
    BACKGROUND_COLOR,
    PARTICLE_TYPES
)

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 300

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")
clock = pygame.time.Clock()

particles = [
    Particle(
        WIDTH, HEIGHT, PARTICLE_RADIUS,
        random.choice(PARTICLE_TYPES),
        PARTICLE_MASS
    ) 
    for _ in range(NUM_PARTICLES)
]

running = True
while running: 
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i, p1 in enumerate(particles):
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            ## collision
            resolve_collision(p1, p2)
            
            ## interaction force
            interaction = get_interaction(p1.type, p2.type)
            if interaction != 0:
                compute_force(p1, p2, interaction, INTERACTION_DISTANCE)
    
    for p in particles:
        p.update(PARTICLE_DAMPING)
        p.draw(screen)
        
    pygame.display.flip()
    
pygame.quit()
