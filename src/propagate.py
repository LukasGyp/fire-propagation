import numpy as np
import scipy.signal as sg

distances = np.array([[np.sqrt(i**2 + j**2) for j in range(-2, 3)]for i in range(-2, 3)])        

def filter():
    return np.exp(-distances**2/2)

def calculate_interaction(intensity):
    return sg.convolve(intensity, filter(), mode='same') 

PROBABILITY_COEFFICIENT = 0.5
def _convert_interaction_to_probability(interaction):
    return 1 - np.exp(-interaction*PROBABILITY_COEFFICIENT)
convert_interaction_to_probability = np.frompyfunc(_convert_interaction_to_probability, 1, 1)
