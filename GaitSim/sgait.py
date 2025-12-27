import math
import matplotlib.pyplot as plt

# Gait parameters
L = 0.08
H = 0.04
beta = 0.6

def foot_trajectory(phi):
    if phi < beta:
        s = phi / beta
        x = +L/2 - L * s
        y = 0.0
    else:
        s = (phi - beta) / (1 - beta)
        x = -L/2 + L * (1 - math.cos(math.pi * s)) / 2
        y = H * math.sin(math.pi * s)
    return x, y

# Generate trajectory
phis = [i / 200 for i in range(200)]
xs, ys = [], []

for phi in phis:
    x, y = foot_trajectory(phi)
    xs.append(x)
    ys.append(y)

# Plot
plt.figure()
plt.plot(xs, ys)
plt.xlabel("x (forward/back)")
plt.ylabel("y (up)")
plt.title("Foot Trajectory (Stance + Swing)")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.show()
