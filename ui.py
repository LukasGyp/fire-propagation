import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def animate(state, interval=300, frames=100):
    fig = plt.figure()

    def update(i):
        if i: plt.cla()
        state.evolve()
        plt.imshow(state.intensity, cmap='afmhot', vmin=0, vmax=5)
        plt.title(f'frame {i}')
        
    anim = FuncAnimation(fig, update, interval=interval, frames=frames)
    anim.save('fire.gif', fps=60, writer='pillow')

