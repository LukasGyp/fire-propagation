import numpy as np
from propagate import calculate_interaction, convert_interaction_to_probability

class State:
    def __init__(self, size):
        self.intensity = np.zeros(size)
        self.wood = np.zeros(size)

    def add_fire(self, x, y):
        self.intensity[y][x] += 1

    def evolve(self):
        interaction = calculate_interaction(self.intensity)
        probability = convert_interaction_to_probability(interaction)

