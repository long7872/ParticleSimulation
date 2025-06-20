import pygame
from core.particle import Particle
from core.physics import resolve_collision, compute_repulsion
from core.config import (
    PARTICLE_RADIUS,
    PARTICLE_MASS,
    REPULSION_DISTANCE,
    BACKGROUND_COLOR,
)

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")
clock = pygame.time.Clock()

particles = [
    Particle(WIDTH, HEIGHT, PARTICLE_RADIUS, PARTICLE_MASS) 
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
        total_fx, total_fy = 0, 0
        for j, p2 in enumerate(particles):
            if i != j:
                ## collision
                resolve_collision(p1, p2)
                
                ## repulsion force
                compute_repulsion(p1, p2, REPULSION_DISTANCE)
                # fx, fy = compute_repulsion(p1, p2, REPULSION_DISTANCE)
                # total_fx += fx
                # total_fy += fy
        # p1.apply_force(total_fx, total_fy)
        # for j in range(i + 1, len(particles)):
        #     p2 = particles[j]
        #     resolve_collision(p1, p2)
    
    for p in particles:
        p.update()
        p.draw(screen)
        
    pygame.display.flip()
    
pygame.quit()
