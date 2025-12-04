# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 11:17:12 2025

@author: Charlotte
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def stateSpace(x, t):
    dxdt = [-x[0] - 3*x[1], 
            3*x[0] - x[1]]
    return dxdt;

x0 = np.linspace(-2, 2, 20);
x1 = np.linspace(-2, 3, 20);

X0,X1 = np.meshgrid(x0, x1);

# project trajectory tangent vector
dX0 = np.zeros(X0.shape);
dX1 = np.zeros(X1.shape);

shape1,shape2 = X1.shape;

# compute projections
for indexShape1 in range(shape1):
    for indexShape2 in range(shape2):
        dxdtAtX = stateSpace([X0[indexShape1, indexShape2],
                              X1[indexShape1, indexShape2]],
                             0);
        dX0[indexShape1, indexShape2] = dxdtAtX[0];
        dX1[indexShape1, indexShape2] = dxdtAtX[1];
        
# solution state
initialState = np.array([-1,1]);
simulationTime = np.linspace(0,2,200);
solutionState = odeint(stateSpace, initialState, simulationTime);
        
# plot
plt.figure(figsize=(8,8));
plt.quiver(X0, X1, dX0, dX1, color='b');
plt.xlim(-2,2);
plt.ylim(-2,2);

# solution state
plt.plot(solutionState[:,0], solutionState[:,1], color='r', linewidth=3);

plt.title('Phase Portrait', fontsize=14);
plt.xlabel('x1', fontsize=14);
plt.ylabel('x2', fontsize=14);
plt.tick_params(axis='both', which='major', labelsize=14);
plt.show();