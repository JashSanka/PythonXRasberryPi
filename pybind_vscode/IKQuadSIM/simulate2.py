import ik_module
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L1 = 10.0
L2 = 10.0

trajectory = [
    (10, 10),
    (15, 5),
    (5, 15),
    (0, 20),
    (-5, 10),
]

def compute_positions(x, y):
    theta1, theta2 = ik_module.ik_2dof(x, y, L1, L2)
    hip = np.array([0, 0])
    knee = hip + np.array([L1*np.cos(theta1), L1*np.sin(theta1)])
    foot = knee + np.array([L2*np.cos(theta1+theta2), L2*np.sin(theta1+theta2)])
    return hip, knee, foot

fig, ax = plt.subplots()
ax.set_xlim(-5, 25)
ax.set_ylim(-5, 25)
ax.set_aspect('equal')
ax.grid(True)

line, = ax.plot([], [], 'o-', lw=4, color='blue')

def update(frame):
    x, y = trajectory[frame % len(trajectory)]
    hip, knee, foot = compute_positions(x, y)
    xs = [hip[0], knee[0], foot[0]]
    ys = [hip[1], knee[1], foot[1]]
    line.set_data(xs, ys)
    ax.set_title(f"Target Foot: ({x}, {y})")
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(trajectory), interval=1000, blit=True)
plt.show()
