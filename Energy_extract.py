'''extracting the energies from the data'''

import numpy as np

print('Loading VX')
VX = np.loadtxt('VX_data.txt',delimiter=',')
print('Loading VY')
VY = np.loadtxt('VY_data.txt',delimiter=',')
print('Loading VZ')
VZ = np.loadtxt('VZ_data.txt',delimiter=',')
print('VX,VY,VZ loaded')

print('Generating VX2')
VX2 = np.array([sum(np.array([i**2 for i in j])/2) for j in VX])
print('Generating VY2')
VY2 = np.array([sum(np.array([i**2 for i in j])/2) for j in VY])
print('Generating VZ2')
VZ2 = np.array([sum(np.array([i**2 for i in j])/2) for j in VZ])
print('VX2,VY2,VZ2 generated')

KE_data = VX2 + VY2 + VZ2

np.savetxt('Kinetic_data.txt',KE_data,delimiter=',')
np.savetxt('VX2_data.txt',VX2,delimiter=',')
np.savetxt('VY2_data.txt',VY2,delimiter=',')
np.savetxt('VZ2_data.txt',VZ2,delimiter=',')

PE = np.loadtxt('PE_data.txt',delimiter=',')
KE = np.array([KE_data[i] for i in range(1,len(KE_data))])

TE_data = KE + PE

np.savetxt('TE_data.txt',TE_data,delimiter=',')
np.savetxt('KE_data.txt',KE,delimiter=',')
print('PE,KE,TE generated')

