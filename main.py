import numpy as np

from src.state import State
from ui import animate

def main():
   state = State((100, 100), np.ones((100, 100))*1000)
   state.add_fire(10, 10)
   animate(state, interval=200, frames=500)

if __name__ == '__main__':
   main()
