'''extracting the temperature'''

import numpy as np

VX2 = np.loadtxt('VX2_data.txt',delimiter=',')
VY2 = np.loadtxt('VY2_data.txt',delimiter=',')
VZ2 = np.loadtxt('VZ2_data.txt',delimiter=',')

df = (3*108)-3

T_data = (2*(VX2+VY2+VZ2))/df
np.savetxt('T_data.txt',T_data,delimiter=',')





