import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def animate(state):
    fig = plt.figure()

    def update(i):
        if i: plt.cla()
        state.evolve()
        plt.imshow(state.intensity, cmap='afmhot', vmin=0, vmax=5)
        plt.title(f'frame {i}')
        
    anim = FuncAnimation(fig, update, interval=300, frames=30)
    anim.save('fire.gif', writer='pillow')

