import numpy as np

distances = np.array([[np.sqrt(i**2 + j**2) for j in range(-2, 3)]for i in range(-2, 3)])        

def filter():
    return np.exp(-distances**2/2)

print(proba_distribution())

