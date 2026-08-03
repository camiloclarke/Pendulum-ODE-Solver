import numpy as np

g = 9.81
L = 1.0
b = 0.2

def pendulum_derivs(state):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta) - b * omega
    return np.array([dtheta_dt, domega_dt])