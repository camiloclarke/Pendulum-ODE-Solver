import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pendulum import pendulum_derivs
from solvers import simulate_euler, simulate_rk4

state0 = np.array([np.pi / 4, 0.0])  # start at 45 degrees, no initial velocity

# --- Plot 1: Euler vs RK4 at dt=0.01 (close agreement) ---
t_e, s_e = simulate_euler(state0, dt=0.01, t_max=10)
t_r, s_r = simulate_rk4(state0, dt=0.01, t_max=10)

plt.figure(figsize=(10, 6))
plt.plot(t_e, s_e[:, 0], label='Euler (θ)', linestyle='--')
plt.plot(t_r, s_r[:, 0], label='RK4 (θ)')
plt.xlabel('Time (s)')
plt.ylabel('Angle θ (rad)')
plt.title('Damped Pendulum: Euler vs RK4 (dt=0.01)')
plt.legend()
plt.grid(True)
plt.savefig('euler_vs_rk4_dt0.01.png')
plt.show()

# --- Plot 2: Euler instability at dt=0.05 ---
t_e2, s_e2 = simulate_euler(state0, dt=0.05, t_max=10)
t_r2, s_r2 = simulate_rk4(state0, dt=0.05, t_max=10)

plt.figure(figsize=(10, 6))
plt.plot(t_e2, s_e2[:, 0], label='Euler (θ)', linestyle='--')
plt.plot(t_r2, s_r2[:, 0], label='RK4 (θ)')
plt.xlabel('Time (s)')
plt.ylabel('Angle θ (rad)')
plt.title('Damped Pendulum: Euler Instability (dt=0.05)')
plt.legend()
plt.grid(True)
plt.savefig('euler_instability_dt0.05.png')
plt.show()

# --- Plot 3: RK4 validated against SciPy ---
def scipy_derivs(t, state):
    return pendulum_derivs(state)

sol = solve_ivp(scipy_derivs, [0, 10], state0, t_eval=np.linspace(0, 10, 1000))

plt.figure(figsize=(10, 6))
plt.plot(t_r, s_r[:, 0], label='My RK4', linewidth=2)
plt.plot(sol.t, sol.y[0], label='SciPy solve_ivp', linestyle=':', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Angle θ (rad)')
plt.title('My RK4 vs SciPy Reference Solver (validation)')
plt.legend()
plt.grid(True)
plt.savefig('rk4_vs_scipy_validation.png')
plt.show()