# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 10:08:37 2025

@author: Charlotte
"""

import matplotlib.pyplot as plt

N = 100
I = 1
S = 100 - I
alpha = 0.5
MAX_TIME = 100

susceptible = []
infected = []

def simulate(S, I, N):
    for t in range (0, MAX_TIME):
        dIdt = (alpha / N) * S * I;
        S = S - dIdt;
        I = I + dIdt;
        susceptible.append(S);
        infected.append(I);

simulate(S, I, N);

figure = plt.figure();
infected_line,    = plt.plot(infected, label='I(t)');
susceptible_line, = plt.plot(susceptible, label='S(t)');
plt.legend(handles=[infected_line, susceptible_line]);

plt.show();