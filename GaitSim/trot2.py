from vpython import *
import math
import time


# Scene Setup
scene = canvas(title="Quadruped Trot Gait Simulation",
               width=1000, height=600,
               center=vector(0, -0.1, 0),
               background=color.white)

# Robot Parameters
L1 = 0.10   # upper leg length
L2 = 0.10   # lower leg length

BODY_HEIGHT = 0.15
STEP_LENGTH = 0.08
STEP_HEIGHT = 0.04

CYCLE_TIME = 1.0
DUTY_FACTOR = 0.55

# Body
body = box(pos=vector(0, 0, 0),
           size=vector(0.25, 0.05, 0.15),
           color=color.gray(0.6))

# Leg Base Positions
LEG_BASES = {
    "FL": vector( 0.10, 0,  0.07),
    "FR": vector( 0.10, 0, -0.07),
    "RL": vector(-0.10, 0,  0.07),
    "RR": vector(-0.10, 0, -0.07),
}

PHASE_OFFSETS = {
    "FL": 0.0,
    "RR": 0.0,
    "FR": 0.5,
    "RL": 0.5
}

# Leg Visuals
legs = {}
for leg in LEG_BASES:
    upper = cylinder(radius=0.01, color=color.blue)
    lower = cylinder(radius=0.008, color=color.red)
    foot  = sphere(radius=0.012, color=color.black)
    legs[leg] = (upper, lower, foot)

# Inverse Kinematics
def leg_ik(x, y):
    r = math.sqrt(x*x + y*y)
    r = min(r, L1 + L2 - 1e-5)

    cos_knee = (L1**2 + L2**2 - r**2) / (2*L1*L2)
    knee = math.pi - math.acos(cos_knee)

    alpha = math.atan2(y, x)
    cos_hip = (L1**2 + r**2 - L2**2) / (2*L1*r)
    hip = alpha - math.acos(cos_hip)

    return hip, knee

# Foot Trajectory
def foot_trajectory(phase):
    if phase < DUTY_FACTOR:  # stance
        x = STEP_LENGTH/2 - STEP_LENGTH * (phase / DUTY_FACTOR)
        y = 0
    else:  # swing
        s = (phase - DUTY_FACTOR) / (1 - DUTY_FACTOR)
        x = -STEP_LENGTH/2 + STEP_LENGTH*(1 - math.cos(math.pi*s))/2
        y = STEP_HEIGHT * math.sin(math.pi*s)
    return x, y

# Simulation Loop
start_time = time.time()

while True:
    rate(60)

    t = time.time() - start_time
    base_phase = (t / CYCLE_TIME) % 1.0

    for leg, base in LEG_BASES.items():
        phase = (base_phase + PHASE_OFFSETS[leg]) % 1.0

        x, y = foot_trajectory(phase)
        hip, knee = leg_ik(x, -BODY_HEIGHT + y)

        # Hip joint position
        hip_pos = body.pos + base

        # Knee position
        knee_pos = hip_pos + vector(
            L1 * math.cos(hip),
            L1 * math.sin(hip),
            0
        )

        # Foot position
        foot_pos = knee_pos + vector(
            L2 * math.cos(hip + knee),
            L2 * math.sin(hip + knee),
            0
        )

        upper, lower, foot = legs[leg]

        upper.pos = hip_pos
        upper.axis = knee_pos - hip_pos

        lower.pos = knee_pos
        lower.axis = foot_pos - knee_pos

        foot.pos = foot_pos
