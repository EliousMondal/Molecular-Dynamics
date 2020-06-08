'''Plotting the temperature'''
import matplotlib.pyplot as plt
import numpy as np

T_data = np.loadtxt('T_data.txt',delimiter=',')
t = np.array([(0.005*i) for i in range(len(T_data))])

plt.figure()
plt.plot(t,T_data)
plt.xlabel('time(reduced units) ----->')
plt.ylabel('Temperature(reduced units) ----->')
plt.title('T vs t for 100000 steps')
plt.show()
