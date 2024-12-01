import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

import glob
import os

def get_gif_name():
    if not os.path.exists('out'):
        os.makedirs('out')

    files = glob.glob('out/*.gif')
    return f'out/fire_{len(files)}.gif'

def animate(state, interval=20, frames=100, output=False):
    fig = plt.figure()

    def update(i):
        if i: plt.cla()
        state.evolve()
        plt.imshow(state.intensity, cmap='afmhot', vmin=0, vmax=70)
        plt.title(f'frame ({i}/{frames})')
        plt.xticks([])
        plt.yticks([])
        
    anim = FuncAnimation(fig, update, interval=interval, frames=frames)
    if output:
        anim.save(get_gif_name(), fps=60, writer='pillow')
    else:
        plt.show()

