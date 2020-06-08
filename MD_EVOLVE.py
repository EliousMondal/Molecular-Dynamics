'''Author - MD ELIOUS ALI MONDAL
   Created - 16/5/2020
   Description - This file defines a function which can update the positions,
                 velocities, forces and potential energy at each time step
'''

from MD_FORCES import *

##==============================================================================
'''Defining function to evolve the system classicaly using velocity-verlet
   algorihm'''
def evolution(RX,RY,RZ,VX,VY,VZ,FX,FY,FZ,dt):
    '''Input :Initial coordinates,velocities and forces of(/on) atoms
       Output :Final coordinates,velocities and forces of(/on) atoms'''
    #updating positions and applying PBC
    RX = (RX + dt*VX + 0.5*(dt**2)*FX)%BOXL
    RY = (RY + dt*VY + 0.5*(dt**2)*FY)%BOXL
    RZ = (RZ + dt*VZ + 0.5*(dt**2)*FZ)%BOXL
    #updating velocities(first update in velocity-verlet)
    VX = VX + 0.5*dt*FX
    VY = VY + 0.5*dt*FY
    VZ = VZ + 0.5*dt*FZ
    #updating force for the present RX,RY,RZ
    Fr = force(RX,RY,RZ)
    FX,FY,FZ,epot = Fr
    #updating velocities(second update in velocity-verlet)
    VX = VX + 0.5*dt*FX
    VY = VY + 0.5*dt*FY
    VZ = VZ + 0.5*dt*FZ
    
    return (RX,RY,RZ,VX,VY,VZ,FX,FY,FZ,epot)

##==============================================================================
