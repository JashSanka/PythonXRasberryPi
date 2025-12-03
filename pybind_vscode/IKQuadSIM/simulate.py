import ik_module
import numpy as np

# Link lengths
L1 = 10.0
L2 = 10.0

# Test target points
test_points = [
    (10, 10),
    (15, 5),
    (5, 15),
    (0, 20),
    (-5, 10),
]

for (x, y) in test_points:
    theta1, theta2 = ik_module.ik_2dof(x, y, L1, L2)
    print(f"Target ({x}, {y}) → θ1={np.degrees(theta1):.2f}°, θ2={np.degrees(theta2):.2f}°")
