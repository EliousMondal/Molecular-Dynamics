'''Author - MD ELIOUS ALI MONDAL
   Created - 19/5/2020
   Description - This file carries out the whole simulation in the specified
                 time steps and also stores the data generated at each time step
                 in different .txt files
'''
from MD_EVOLVE import *

##==============================================================================
'''Doing the MD simulation'''
dt = 0.005                #time step size
t = 0                     #initialising time counter
nts = 100000              #number of time steps
PE = np.zeros(nts)        #array to store Potential energy at each time step

for i in range(nts):
    
    #calling the evolve function to simulate each time step
    EV = evolution(RX,RY,RZ,VX,VY,VZ,FX,FY,FZ,dt)
    RX,RY,RZ,VX,VY,VZ,FX,FY,FZ,PE[i] = EV
    
    #updating the time counter
    t = t + dt
    print('time = ',t,' done')
    
    #stroing positions,velocities,forces at each time step in a dictionary
    R_dict[t] = np.array([RX,RY,RZ])
    V_dict[t] = np.array([VX,VY,VZ])
    F_dict[t] = np.array([FX,FY,FZ])
    
##==============================================================================
end = time.clock()
tt = end- start
print('The code took ',tt,' seconds.')

##==============================================================================
'''Storing the positions, velocities ,forces and potential data in files'''
RX_array = np.array([R_dict[its][0] for its in list(R_dict.keys())])
RX_data = np.vstack([i for i in RX_array])
np.savetxt('RX_data.txt',RX_data,delimiter=',')

RY_array = np.array([R_dict[its][1] for its in list(R_dict.keys())])
RY_data = np.vstack([i for i in RY_array])
np.savetxt('RY_data.txt',RY_data,delimiter=',')

RZ_array = np.array([R_dict[its][2] for its in list(R_dict.keys())])
RZ_data = np.vstack([i for i in RZ_array])
np.savetxt('RZ_data.txt',RZ_data,delimiter=',')

VX_array = np.array([V_dict[its][0] for its in list(V_dict.keys())])
VX_data = np.vstack([i for i in VX_array])
np.savetxt('VX_data.txt',VX_data,delimiter=',')

VY_array = np.array([V_dict[its][1] for its in list(V_dict.keys())])
VY_data = np.vstack([i for i in VY_array])
np.savetxt('VY_data.txt',VY_data,delimiter=',')

VZ_array = np.array([V_dict[its][2] for its in list(V_dict.keys())])
VZ_data = np.vstack([i for i in VZ_array])
np.savetxt('VZ_data.txt',VZ_data,delimiter=',')

FX_array = np.array([F_dict[its][0] for its in list(F_dict.keys())])
FX_data = np.vstack([i for i in FX_array])
np.savetxt('FX_data.txt',FX_data,delimiter=',')

FY_array = np.array([F_dict[its][1] for its in list(F_dict.keys())])
FY_data = np.vstack([i for i in FY_array])
np.savetxt('FY_data.txt',FY_data,delimiter=',')

FZ_array = np.array([F_dict[its][2] for its in list(F_dict.keys())])
FZ_data = np.vstack([i for i in FZ_array])
np.savetxt('FZ_data.txt',FZ_data,delimiter=',')

np.savetxt('Potential_data.txt',PE,delimiter=',')

##==============================================================================

