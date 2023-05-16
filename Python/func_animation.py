import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_data = []
y_data = []

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
line, = ax.plot([], [])

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), blit=True)

plt.show()
