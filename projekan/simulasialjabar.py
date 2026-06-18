import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Titik-titik persegi (pusat di origin)
square = np.array([
    [-1, -1],
    [ 1, -1],
    [ 1,  1],
    [-1,  1],
    [-1, -1]
])

fig, ax = plt.subplots(figsize=(6,6))
line, = ax.plot([], [], lw=2)

ax.set_xlim(-5, 15)
ax.set_ylim(-5, 10)
ax.set_aspect('equal')
ax.grid(True)

def rotate(points, angle):
    theta = np.radians(angle)

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    return points @ rotation_matrix.T

def update(frame):

    # Rotasi
    rotated = rotate(square, frame * 5)

    # Translasi
    tx = frame * 0.1
    ty = 0

    translated = rotated + np.array([tx, ty])

    line.set_data(translated[:,0], translated[:,1])

    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50,
    blit=True
)

plt.title("Simulasi Translasi dan Rotasi")
plt.show()