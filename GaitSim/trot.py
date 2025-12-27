import numpy as np
import matplotlib.pyplot as plt
import time

# Time → Phase
# Phase → Stance/Swing
# Stance → Linear push
# Swing → Sinusoidal lift
# Phase offsets → Trot gait
# Anchors → Rigid body


# Paramters

step_length= 3
step_height= 2
cycle_time=1.0

# When each leg should start its cycle.

phase = {
    "FL": 0.0,
    "BR": 0.0,
    "FR": 0.5,
    "BL": 0.5
}

# leg anchor postitons

anchors = {
    "FL": np.array([ 5,  5]),
    "FR": np.array([ 5, -5]),
    "BL": np.array([-5,  5]),
    "BR": np.array([-5, -5])
}

def foot_trajectory(t):
    # t => time inside one gait cycle for a leg.
    # Normalization Formula
    # t = (now - start) % cycle_time
    # norm_t = t / cycle_time

    t = t % 1.0  # normalize
# 0.0–0.5 stance

# 0.5–1.0 swing

# 0 → foot at ground

# 0.5 → highest

# 1.0 → back to ground
    if t < 0.5:
        # stance - moving forward low(basically pushing against the ground)
        x = -step_length/2 + step_length * (t / 0.5)
        y = 0
    else:
        # swing phase — moving backward but lifted(hawe main hain pair)
        swing_t = (t - 0.5) / 0.5
        x = step_length/2 - step_length * swing_t
        y = step_height * np.sin(np.pi * swing_t)

    return np.array([x, y])

# simulating with matplotlib
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.set_title("Quadruped Gait Simulation (Real-Time)")
ax.grid(True)

leg_dots = {leg: ax.plot([], [], "o")[0] for leg in anchors}
body_plot, = ax.plot([], [], "k-", linewidth=2)

print("Running real-time gait simulation...")
start = time.time()

while True:
    now = time.time()
    t = (now - start) % cycle_time
    norm_t = t / cycle_time

    # Draw legs
    for leg in anchors:
        foot = foot_trajectory(norm_t + phase[leg]) + anchors[leg]
        leg_dots[leg].set_data([foot[0]], [foot[1]])


    # Draw body rectangle
    body_x = [anchors["FL"][0], anchors["FR"][0], anchors["BR"][0], anchors["BL"][0], anchors["FL"][0]]
    body_y = [anchors["FL"][1], anchors["FR"][1], anchors["BR"][1], anchors["BL"][1], anchors["FL"][1]]
    body_plot.set_data(body_x, body_y)

    plt.draw()
    plt.pause(0.01)
