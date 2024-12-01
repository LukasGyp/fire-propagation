import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def animate(state, interval=300, frames=100):
    fig = plt.figure()

    def update(i):
        if i: plt.cla()
        state.evolve()
        plt.imshow(state.intensity, cmap='afmhot', vmin=0, vmax=70)
        plt.title(f'frame ({i}/{frames})')
        plt.xticks([])
        plt.yticks([])
        
    anim = FuncAnimation(fig, update, interval=interval, frames=frames)
    anim.save('docs/fire.gif', fps=60, writer='pillow')

