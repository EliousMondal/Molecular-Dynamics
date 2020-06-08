'''Author - MD ELIOUS ALI MONDAL
   Created - 16/5/2020
   Description - This file defines a function to give the forces on each atom
                 in a given arrangement of atoms
'''
from MD_IV import *

##==============================================================================
'''Initialising the forces on each atom'''
na = len(RX)
FX = np.zeros(na); FY = np.zeros(na); FZ = np.zeros(na)    #Force initialisation
F_dict = {0:np.array([FX,FY,FZ])}               #Storing force at each time step

##==============================================================================
'''Defining a function to calculate forces on each atom for a given arrangement
   of atoms'''
def force(x,y,z):
    '''Input:
       x,y,z = positions coordinates of the atoms
       FX,FY,FZ = forces acting initially on atoms i.e. beofre (x,y,z)
       Outout:
       FX,FY,FZ = Final forces acting on each particle at (x,y,z)
       epot = final potential energy of the configuration (x,y,z)'''
    na = len(x)
    epot = 0    #initialising the potential energy
    FX = np.zeros(na); FY = np.zeros(na); FZ = np.zeros(na)
    for i in range(na-1):
        for j in range(i+1,na):
            #Calculating distances with minimum image condition
            X = x[i] - x[j]; X = X - BOXL*round(X/BOXL)
            Y = y[i] - y[j]; Y = Y - BOXL*round(Y/BOXL)
            Z = z[i] - z[j]; Z = Z - BOXL*round(Z/BOXL)
            
            R2 = X**2 + Y**2 + Z**2
            RC = BOXL/2    #cutoff radius
            RC2 = RC**2
            #updating the forces if patricle inside the cutoff radius
            if R2 <= RC2 :
                R2I = 1/R2
                R6I = R2I**3
                FF = 48*R2I*R6I*(R6I-0.5)
                FX[i] = FX[i] + FF*X; FX[j] = FX[j] - FF*X
                FY[i] = FY[i] + FF*Y; FY[j] = FY[j] - FF*Y
                FZ[i] = FZ[i] + FF*Z; FZ[j] = FZ[j] - FF*Z
                epot = epot + 4*R6I*(R6I-1)

    return (FX,FY,FZ,epot)
    
##==============================================================================
