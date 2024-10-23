def transition(state_matrix, current_energy, temperature, J, N, n):

    """
    Takes a state (square) matrix of magnetic spins in argument, associated with an Hamiltonian energy, at a given temperature in Kelvin.

    It takes in random a magnetic moment out of the n**2 numbers of magnetic moment of the square matrix and gives it a value of 1 with probability 1/2 and -1 with a probability -1/2.

    If the new matrix energy is lower, the state is accepted.

    If not, using random-object from the rand library, it determines whether that state is accepted or not using the probability acceptation.

    It then returns the new energy and the new state matrix. 
    """

    import random

    ## generate the indexes of the magnetic moment we wanted to change (stored in the numpy array indexes),
    #  and value of that new magnetic moment (stored in the float value)
    
    indexes = np.array(random.uniform(0, n**2-1),random.uniform(0, n**2-1))

    initial_matrix = state_matrix.deepcopy()

    print("the spin chosen is :", indexes)
    print("with a new value of :", orientation)

    orientation = -1*state_matrix[indexes[0], indexes[1]]

    state_matrix[indexes[0], indexes[1]] = value

    delta_energy = calculate_new_energy(state_matrix, current_energy, indexes, orientation)

    if delta_energy < 0 : 
        print("transition accepted")

        return(delta_energy + current_energy, state_matrix)

    else : 
        print("newer energy greater than the old one : delta = ", delta_energy)

        if numpy.random.uniform() <= np.exp(-delta_energy/temperature):
            
            print("transition accepted !")

            return(delta_energy + current_energy, state_matrix)

        else :

            print("transition rejected...")

            return(current_energy, intial_matrix)


            











