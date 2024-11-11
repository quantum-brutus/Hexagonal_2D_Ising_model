import numpy as np


def initial_energy(initial_state_matrix, B_star, T_star, hexagonal = False):  # initial_state is a nxn np array matrix

    """
    Takes an initial state (nxn matrix) of values 0 (spin down) and 1 (spin up) 
    and a magnetic field in arguments and computes the Hamiltonian energy 
    of this initial state of the system.
    """
    if not(hexagonal) : 
        S0 = initial_state_matrix
        n = len(S0)

        fni_contribution = 0   # 'fni' for 'first neighbor interaction'
        
        for i in range(n):
            for j in range(n):
                
                m = S0[i,j]
                fni_contribution += m*(S0[i-1,j] + S0[(i+1)%n,j] + S0[i,j-1] + S0[i,(j+1)%n])
        
        
        fni_contribution*=0.5
        magnetic_contribution = -B_star*np.sum(S0)
        
        return np.sign(T_star)*(fni_contribution + magnetic_contribution)

    else : 
        S0 = initial_state_matrix
        n = len(S0)

        fni_contribution = 0   # 'fni' for 'first neighbor interaction'
        
        for i in range(n):
            for j in range(n):
                
                m = S0[i,j]
                fni_contribution += m*(S0[i-1,j] + S0[i-1,(j+1)%n] + S0[(i+1)%n,j] + S0[(i+1)%n,(j+1)%n] + S0[i,j-1] + S0[i,(j+1)%n])
        
        
        fni_contribution*=0.5
        magnetic_contribution = -B_star*np.sum(S0)
        
        return np.sign(T_star)*(fni_contribution + magnetic_contribution)



def calculate_delta_energy(state_matrix, indexes, orientation, B_star, T_star, hexagonal = False):
    
    if not(hexagonal) : 

        i,j = indexes
        S = state_matrix
        n = len(S)
        
        neigbors_config = S[i-1,j] + S[(i+1)%n,j] + S[i,j-1] + S[i,(j+1)%n]
        if orientation == -1 :
            delta_energy = -2*neigbors_config + 2*B_star
        else:
            delta_energy = 2*neigbors_config - 2*B_star
        
        return np.sign(T_star)*delta_energy

    else : 
        
        i,j = indexes
        S = state_matrix
        n = len(S)
        
        neigbors_config = S[i-1,j] + S[i-1,(j+1)%n] +S[(i+1)%n,j] + S[i,j-1] + S[i,(j+1)%n] + S[(i+1)%n,(j+1)%n]

        if orientation == -1 :
            delta_energy = -2*neigbors_config + 2*B_star
        else:
            delta_energy = 2*neigbors_config - 2*B_star
        
        return np.sign(T_star)*delta_energy


    
    

def transition(state_matrix, current_energy, n, B_star, T_star, hexagonal = False):

    """
    Takes a state (square) matrix of magnetic spins in argument, associated with an Hamiltonian energy, at a given temperature in Kelvin.

    It takes in random a magnetic moment out of the n**2 numbers of magnetic moment of the square matrix and gives it a value of 1 with probability 1/2 and -1 with a probability -1/2.

    If the new matrix energy is lower, the state is accepted.

    If not, using random-object from the rand library, it determines whether that state is accepted or not using the probability acceptation.

    It then returns the new energy and the new state matrix, as well as the new orientation. 
    """

    # generate the indexes of the magnetic moment we wanted to change (stored in the numpy array indexes),
    #  and value of that new magnetic moment (stored in the float value)
    
    indexes = np.random.randint(0, n, size=2)

    initial_matrix = np.copy(state_matrix)

    print("the spin chosen is :", indexes)

    orientation = -1*state_matrix[indexes[0], indexes[1]]

    print("with a new value of :", orientation)

    state_matrix[indexes[0], indexes[1]] = orientation

    delta_energy = calculate_delta_energy(state_matrix, indexes, orientation, B_star, T_star, hexagonal)

    if delta_energy < 0 : 

        print("newer energy smaller than the old one : delta = ", delta_energy)
        print("the theoretical delta should be ", initial_energy(state_matrix, B_star, T_star, hexagonal = hexagonal)-initial_energy(initial_matrix, B_star, T_star, hexagonal = hexagonal))

        print("transition accepted")

        print("current energy is ", current_energy)
        print("new energy is ", delta_energy + current_energy)

        return(delta_energy + current_energy, state_matrix, orientation, 1, indexes)

    else : 
        print("newer energy greater than the old one : delta = ", delta_energy)
        print("the theoretical delta should be ", initial_energy(state_matrix, B_star, T_star, hexagonal = hexagonal)-initial_energy(initial_matrix, B_star, T_star, hexagonal = hexagonal))

        if np.random.uniform() <= np.exp(-delta_energy/abs(T_star)):
            
            print("transition accepted !")


            print("current energy is ", current_energy)
            print("new energy is ", delta_energy + current_energy)

            return(delta_energy + current_energy, state_matrix, orientation, 1, indexes)

        else :

            print("transition rejected...")

            print("current energy is ", current_energy)
            print("new energy is ", current_energy)

            return(current_energy, initial_matrix, -1*orientation, 0, indexes)











# a = np.array([[ -1, -1, -1, -1,  -1],
# [ -1,  1,  -1,  -1,  -1],
# [ -1,  -1,  -1,  -1,  1],
# [ -1,  -1,  1, 1,  1],
# [-1,  1, 1,  -1,  1]])



# # [[-1 -1 -1 -1 -1]
# #  [-1  1 -1 -1 -1]
# #  [-1 -1 -1 -1  1]
# #  [-1 -1  1  1  1]
# #  [-1  1  1 -1  1]]


# print(initial_energy(a, 0, -1, hexagonal = False))

# a[1,0]= -1

# print(initial_energy(a, 0, -1, hexagonal = True))
