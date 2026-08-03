import numpy as np
from pendulum import pendulum_derivs

def euler_step(state, dt):
    return state + dt * pendulum_derivs(state)

def simulate_euler(state0, dt, t_max):
    steps = int(t_max / dt)
    states = np.zeros((steps, 2))
    states[0] = state0
    for i in range(1, steps):
        states[i] = euler_step(states[i-1], dt)
    times = np.linspace(0, t_max, steps)
    return times, states

def rk4_step(state, dt):
    k1 = pendulum_derivs(state)
    k2 = pendulum_derivs(state + dt/2 * k1)
    k3 = pendulum_derivs(state + dt/2 * k2)
    k4 = pendulum_derivs(state + dt * k3)
    return state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

def simulate_rk4(state0, dt, t_max):
    steps = int(t_max / dt)
    states = np.zeros((steps, 2))
    states[0] = state0
    for i in range(1, steps):
        states[i] = rk4_step(states[i-1], dt)
    times = np.linspace(0, t_max, steps)
    return times, states