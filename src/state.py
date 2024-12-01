import numpy as np
from .propagate import calculate_interaction, convert_interaction_to_probability

FIRE_GROWTH_RATE = 0.25

class State:
    def __init__(self, size, wood_distribution):
        self.size = size
        self.intensity = np.zeros(size)
        self.wood = wood_distribution
        self.initial_wood = wood_distribution.copy()

    def add_fire(self, x, y):
        self.intensity[y][x] += 1

    def evolve(self):
        self._burn_wood()
        self._catch_fire()
        self._burn_out()
    
    def _catch_fire(self):
        interaction = calculate_interaction(self.intensity)
        probability = convert_interaction_to_probability(interaction)
        self.intensity = np.where((self.intensity == 0) & (self.wood > 0) & (np.random.rand(*self.size) < probability), self.intensity + 1, self.intensity)
        
    def _burn_wood(self):
        self.intensity = FIRE_GROWTH_RATE * self.wood * (1 - (self.wood - self.intensity) / self.initial_wood)
        self.wood -= self.intensity
        self.wood = np.where(self.wood <= 0, 0, self.wood)

    def _burn_out(self):
        self.intensity = np.where(self.wood == 0, 0, self.intensity)
