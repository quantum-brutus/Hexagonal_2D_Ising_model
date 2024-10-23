# modules

import numpy as np


# parameters

n = 3
N = n**2

eps = 0.001  # stopping condition

k_B = 1
mu = 1
J = 1
B = 1



# dimensionless quantities

B_star = B/(J*mu)



    
def initial_energy(initial_state_matrix):  # initial_state is a nxn np array matrix

    """
    Takes an initial state (nxn matrix) of values 0 (spin down) and 1 (spin up) 
    and a magnetic field in arguments and computes the Hamiltonian energy 
    of this initial state of the system.
    """
    
    S0 = initial_state_matrix
    n = len(S0)

    fni_contribution = 0   # 'fni' for 'first neighbor interaction'
    
    for i in range(n):
        for j in range(n):
            
            m = S0[i,j]
            fni_contribution += m*(S0[i-1,j] + S0[(i+1)%n,j] + S0[i,j-1] + S0[i,(j+1)%n])
    
    
    fni_contribution*=0.5
    magnetic_contribution = -B_star*np.sum(S0)
    
    return fni_contribution + magnetic_contribution

res = initial_energy(np.random.randint(2,size = (n,n)))



def calculate_delta_energy(state_matrix, current_energy, indexes, orientation):
    
    i,j = indexes
    S = state_matrix
    delta_energy = 0
    
    neigbors_config = S[i-1,j] + S[(i+1)%n,j] + S[i,j-1] + S[i,(j+1)%n]
    if orientation == -1 :
        delta_energy += -neigbors_config + 2*B_star
    else:
        delta_energy += neigbors_config - 2*B_star
    
    return delta_energy

    
    