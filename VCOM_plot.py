'''plotting the com velocities'''

import numpy as np
import matplotlib.pyplot as plt

VXC = np.loadtxt('VXC_data.txt',delimiter=',')
VYC = np.loadtxt('VYC_data.txt',delimiter=',')
VZC = np.loadtxt('VZC_data.txt',delimiter=',')

t = np.array([(0.005*i) for i in range(len(VXC))])

plt.figure()
plt.plot(t,VXC,label=r'$V^{com}_X$')
plt.plot(t,VYC,label=r'$V^{com}_Y$')
plt.plot(t,VZC,label=r'$V^{com}_Z$')
plt.xlabel('Time(reduced units) ----->')
plt.ylabel(r'$V_{com}$ (reduces units x$10^{-15}$) ----->')
plt.legend()
plt.title(r'$V_{com}$ vs time for 100000 steps')
plt.show()
