import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def differential(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


if __name__ == "__main__":

    N = 1000
    ndays = 50
    beta = 1.0
    D = 4.0
    gamma = 1.0 / D

    S0, I0, R0 = N - 1, 1, 0

    t = np.linspace(0, ndays - 1, ndays)  # x-axis, time points
    y0 = S0, I0, R0  # initial conditions

    # Integrate the SIR equations over t
    ret = odeint(differential, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T

    # Plot results
    f, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(t, S, 'b', linewidth=2, label='(S)usceptible')
    ax.plot(t, I, 'r', linewidth=2, label='(I)nfected')
    ax.plot(t, R, 'g', linewidth=2, label='(R)ecovered')
    ax.set_xlabel('days')
    ax.legend()
    plt.show()
