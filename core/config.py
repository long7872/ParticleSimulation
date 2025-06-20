# General Config

PARTICLE_DAMPING = 0.999
MAX_FORCE = 0.05
PARTICLE_RADIUS = 5
PARTICLE_MASS = 1.0
INTERACTION_DISTANCE = 100
BACKGROUND_COLOR = (0, 0, 0)

# Types
PARTICLE_TYPES = ['red', 'green']

PARTICLE_COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
}

# Force type: 1 = repulsion, -1 = attraction, 0 = no interaction
#   red     green
INTERACTION_VALUES  = [
    [ -2, -6],   # red
    [ 8, -3],   # green
]