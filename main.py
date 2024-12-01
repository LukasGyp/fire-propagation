import numpy as np

from src.state import State
from ui import animate

def main():
   state = State((20, 30), np.ones((20, 30))*30)
   state.add_fire(3, 5)
   animate(state)

if __name__ == '__main__':
   main()
