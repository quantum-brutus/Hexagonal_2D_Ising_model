import numpy as np


def initial_energy(initial_state_matrix, B_star, T_star):  # initial_state is a nxn np array matrix

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
    
    
    fni_contribution*=0.6
    magnetic_contribution = -B_star*np.sum(S0)
    
    return np.sign(T_star)*fni_contribution + magnetic_contribution


def calculate_delta_energy(state_matrix, indexes, orientation, B_star):
    
    i,j = indexes
    S = state_matrix
    n = len(S)
    
    neigbors_config = S[i-1,j] + S[(i+1)%n,j] + S[i,j-1] + S[i,(j+1)%n]
    if orientation == -1 :
        delta_energy = -2*neigbors_config + 2*B_star
    else:
        delta_energy = 2*neigbors_config - 2*B_star
    
    print("config_voisins:", 2*neigbors_config)
    print("magnetic field", B_star)
    return delta_energy

    
    

def transition(state_matrix, current_energy, temperature, n, B_star):

    """
    Takes a state (square) matrix of magnetic spins in argument, associated with an Hamiltonian energy, at a given temperature in Kelvin.

    It takes in random a magnetic moment out of the n**2 numbers of magnetic moment of the square matrix and gives it a value of 1 with probability 1/2 and -1 with a probability -1/2.

    If the new matrix energy is lower, the state is accepted.

    If not, using random-object from the rand library, it determines whether that state is accepted or not using the probability acceptation.

    It then returns the new energy and the new state matrix. 
    """

    # generate the indexes of the magnetic moment we wanted to change (stored in the numpy array indexes),
    #  and value of that new magnetic moment (stored in the float value)
    
    indexes = np.random.randint(0, n, size=2)

    initial_matrix = np.copy(state_matrix)

    print("the spin chosen is :", indexes)

    orientation = -1*state_matrix[indexes[0], indexes[1]]

    print("with a new value of :", orientation)

    state_matrix[indexes[0], indexes[1]] = orientation

    value = initial_energy(state_matrix, B_star) - initial_energy(initial_matrix, B_star)
    print("test", value)

    delta_energy = calculate_delta_energy(state_matrix, indexes, orientation, B_star)

    if delta_energy < 0 : 

        print("newer energy smaller than the old one : delta = ", delta_energy)

        print("transition accepted")

        print("current energy is ", current_energy)
        print("new energy is ", delta_energy + current_energy)

        return(delta_energy + current_energy, state_matrix)

    else : 
        print("newer energy greater than the old one : delta = ", delta_energy)

        if np.random.uniform() <= np.exp(-delta_energy/temperature):
            
            print("transition accepted !")


            print("current energy is ", current_energy)
            print("new energy is ", delta_energy + current_energy)

            return(delta_energy + current_energy, state_matrix)

        else :

            print("transition rejected...")

            print("current energy is ", current_energy)
            print("new energy is ", current_energy)

            return(current_energy, initial_matrix)











