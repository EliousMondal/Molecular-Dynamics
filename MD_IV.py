'''Author - MD ELIOUS ALI MONDAL
   Created - 16/5/2020
   Description - This file is used to generate a uniform random distribution of
                 velocities for atoms. The velocities are then scaled according
                 to the temperature
'''
from MD_IP import *

##==============================================================================
'''Initial velocities for the classical MD simulaion of 108 Argon atoms'''
VX = np.random.uniform(-0.5,0.5,size = len(cp))
VY = np.random.uniform(-0.5,0.5,size = len(cp))
VZ = np.random.uniform(-0.5,0.5,size = len(cp))

def com_0(vx,vy,vz):
    '''converts the velocity of center of mass to 0
       Input = Three arrays containing velocities along the axis
       Output = Three arrays with scaled velocities'''
    sx,sy,sz = np.mean(vx),np.mean(vy),np.mean(vz)
    s2 = sum(vx**2+vy**2+vz**2)                 #sum of squared velocities
    vsf = np.sqrt((3*(len(cp))-3)/s2)           #scaling factor at T* = 1
    vxn =(vx-sx)*vsf; vyn =(vy-sy)*vsf; vzn =(vz-sz)*vsf
    return (vxn,vyn,vzn)
    
VX,VY,VZ = com_0(VX,VZ,VZ)

V_dict = {0:np.array([VX,VY,VZ])}  #Storing velocity at each time step

##==============================================================================
