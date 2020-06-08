'''calculating the com at each time step'''
import numpy as np

VX = np.loadtxt('VX_data.txt',delimiter=',')
VY = np.loadtxt('VY_data.txt',delimiter=',')
VZ = np.loadtxt('VZ_data.txt',delimiter=',')

VXC = np.array([sum(i) for i in VX])/len(VX[0])
VYC = np.array([sum(i) for i in VY])/len(VX[0])
VZC = np.array([sum(i) for i in VZ])/len(VX[0])

VXC_data = np.savetxt('VXC_data.txt',VXC,delimiter=',')
VYC_data = np.savetxt('VYC_data.txt',VYC,delimiter=',')
VZC_data = np.savetxt('VZC_data.txt',VZC,delimiter=',')

