'''Plotting the energies'''

import numpy as np
import matplotlib.pyplot as plt

KE = np.loadtxt('KE_data.txt',delimiter=',')
PE = np.loadtxt('PE_data.txt',delimiter=',')
TE = np.loadtxt('TE_data.txt',delimiter=',')

t = np.array([(0.005*i) for i in range(1,len(TE)+1)])

plt.figure()
plt.title('Energy vs time for 100000 time seps')
plt.plot(t,KE,label='KE')
plt.plot(t,PE,label='PE')
plt.plot(t,TE,label='TE')
plt.xlabel('Time(reduced units) ----->')
plt.ylabel('Energy(reduced units) ----->')
plt.legend()
plt.show()
