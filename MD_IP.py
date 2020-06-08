'''Author - MD ELIOUS ALI MONDAL
   Created - 16/5/2020
   Description - This file generates 108 fcc lattice positions and scales them
                 such that each site is occupied by an Argon atom
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.clock()
##==============================================================================
'''Initial positions for the classical MD simulaion of 108 Argon atoms'''
n = int(input('Enter the no. of unit cells: '))

c1 = [0,0,0]
c2 = [0.5*1/n,0.5*1/n,0]
c3 = [0,0.5*1/n,0.5*1/n]
c4 = [0.5*1/n,0,0.5*1/n]
c = [c1,c2,c3,c4]                                              ##first unit cell

cp = []                                   ##collection of all the lattice points

##construction of lattice from the unit cell
for Iz in range(0,n):
    for Iy in range(0,n):
        for Ix in range(0,n):
            for ref in c:
                rx = ref[0] + Ix/n
                ry = ref[1] + Iy/n
                rz = ref[2] + Iz/n
                cp.append([rx,ry,rz])

BOXL = len(cp)**(1/3)
RX = np.array([i[0] for i in cp])*BOXL
RY = np.array([j[1] for j in cp])*BOXL
RZ = np.array([k[2] for k in cp])*BOXL

R_dict = {0:np.array([RX,RY,RZ])}   #storing position at each time step
#==============================================================================
