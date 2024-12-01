import numpy as np
import argparse

from src.state import State
from src.ui import animate

def get_args():
   parser = argparse.ArgumentParser(description='Simulate a fire')
   parser.add_argument('-s', '--size', type=int, nargs=2, default=[100, 100], help='Size of the grid')
   parser.add_argument('--fire', type=int, nargs=2, default=[10, 10], help='Initial fire position')
   parser.add_argument('-w', '--wood', type=int, nargs=1, default=1000, help='Initial wood')
   parser.add_argument('-o', '--output', action='store_true', help='Output file')
   parser.add_argument('-f', '--frames', type=int, default=300, help='Number of frames')
   return parser.parse_args()

def main():
   args = get_args()
   state = State(args.size, np.ones(args.size)*args.wood)
   state.add_fire(*args.fire)
   animate(state, interval=200, frames=args.frames, output=args.output)

if __name__ == '__main__':
   main()
