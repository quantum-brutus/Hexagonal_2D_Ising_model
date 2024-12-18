### modules ###

from transition import transition, initial_energy
import numpy as np
import matplotlib.pyplot as plt


def simulation(B_star_norm, T_star, n, nb_iterations, plot, hexagonal = False, state = None):
    
    N = n**2
    B_star = np.sign(T_star)*B_star_norm

    ### initialisation ###
    if state.any() == None :
            
        initial_state_matrix = np.random.choice([-1, 1], size=(n, n))
        initialenergy = initial_energy(initial_state_matrix, B_star, T_star, hexagonal)

    else : 
        initial_state_matrix = state
        initialenergy = initial_energy(initial_state_matrix, B_star, T_star, hexagonal)

    print(initial_state_matrix)
    print("Initial energy is :", initialenergy)

    # energy
    energies = np.array([initialenergy]) # the energies of each state
    mean_energies = np.array([initialenergy]) # the mean energy of all the steps realized

    # magnetization
    if T_star<0 : ##ferromagnetic case

        initial_magnetization = np.sum(initial_state_matrix)/N
        magnetizations = np.array([initial_magnetization]) # the magnetizations of each state
        mean_magnetizations = np.array([initial_magnetization]) # the mean magnetization of all the steps realized
    
    elif T_star>0 : ##antiferromagnetic case, we want to observe the alternated sum of the magnetic moments
         # Calculate the alternating magnetization

        initial_magnetization = np.sum(initial_state_matrix)/N
        magnetizations = np.array([initial_magnetization]) # the magnetizations of each state
        mean_magnetizations = np.array([initial_magnetization]) # the mean magnetization of all the steps realized
    
        # rows, cols = initial_state_matrix.shape
        
        # initial_magnetization = 0

        # for i in range(rows):
        #     for j in range(cols):
        #         # Alternate sign based on the sum of indices
        #         sign = (-1) ** (i + j)
        #         initial_magnetization += sign * initial_state_matrix[i, j]
        
        # initial_magnetization /= N

        # magnetizations = np.array([initial_magnetization]) # the magnetizations of each state
        # mean_magnetizations = np.array([initial_magnetization]) # the mean magnetization of all the steps realized


    # heat capacity
    heat_capacities = np.array([0])

    state_matrix = initial_state_matrix

    # first step

    energy, state_matrix, new_orientation, transition_accepted, spin_chosen = transition(state_matrix, initialenergy, n, B_star, T_star, hexagonal)
    
    if transition_accepted == 0 : 
        

        magnetization = initial_magnetization 
        mean_magnetization = magnetization
        magnetizations = np.append(magnetizations, magnetization)
        mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)


    else : 

        if T_star<0 : ##ferromagnetic case

            magnetization = initial_magnetization + new_orientation*2/N
            magnetizations = np.append(magnetizations, magnetization)
            mean_magnetization = (initial_magnetization*(len(magnetizations)-1) + magnetization)/len(magnetizations)
            mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)

        elif T_star>0 : ##antiferromagnetic case, we want to observe the alternated sum of the magnetic moments
            # magnetization = initial_magnetization + ((-1) ** (spin_chosen[0] + spin_chosen[1]))*new_orientation*2/N
            # magnetizations = np.append(magnetizations, magnetization)
            # mean_magnetization = (initial_magnetization*(len(magnetizations)-1) + magnetization)/len(magnetizations)
            # mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)


            magnetization = initial_magnetization + new_orientation*2/N
            magnetizations = np.append(magnetizations, magnetization)
            mean_magnetization = (initial_magnetization*(len(magnetizations)-1) + magnetization)/len(magnetizations)
            mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)

    print(state_matrix)

    # saving the energies
    energies = np.append(energies, energy)
    mean_energy = (initialenergy+energy)/2
    mean_energies = np.append(mean_energies, mean_energy)

    ### loop ###

    i = 1

    while i <= nb_iterations :

        energy, state_matrix, new_orientation, transition_accepted, spin_chosen = transition(state_matrix, energy, n, B_star, T_star, hexagonal)

        print(state_matrix)

        if transition_accepted == 0 : 

                    
            magnetizations = np.append(magnetizations, magnetization)
                
            mean_magnetization = (mean_magnetizations[-1]*(len(magnetizations)-1) + magnetization)/len(magnetizations)

            mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)

        else : 
                
            if T_star<0 : ##ferromagnetic case


                magnetization = magnetization + new_orientation*2/N

                magnetizations = np.append(magnetizations, magnetization)

                mean_magnetization = (mean_magnetizations[-1]*(len(magnetizations)-1) + magnetization)/len(magnetizations)

                mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)

            elif T_star>0 : ##antiferromagnetic case, we want to observe the alternated sum of the magnetic moments
                
                # magnetization = magnetization + ((-1) ** (spin_chosen[0] + spin_chosen[1]))*new_orientation*2/N

                # magnetizations = np.append(magnetizations, magnetization)
                
                # mean_magnetization = (mean_magnetization*(len(magnetizations)-1) + magnetization)/len(magnetizations)

                # mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)

                magnetization = magnetization + new_orientation*2/N

                magnetizations = np.append(magnetizations, magnetization)

                mean_magnetization = (mean_magnetizations[-1]*(len(magnetizations)-1) + magnetization)/len(magnetizations)

                mean_magnetizations = np.append(mean_magnetizations, mean_magnetization)


        # saving the energies
        energies = np.append(energies, energy)
        mean_energy = (mean_energies[-1]*(len(energies)-1) + energy)/len(energies)
        mean_energies = np.append(mean_energies, mean_energy)

        window_size = 15000  # Définit la taille de la tranche pour plus de précision (ajuster selon besoin)
        if i < window_size:
            heat_capacities = np.append(heat_capacities, 0)  # Pas de calcul au début
        else:
            truncated_energies = [energies[i] for i in range(window_size-1000, len(energies))]  # Garder seulement les derniers `window_size` éléments
            heat_capacity = np.var(truncated_energies, ddof=1) / (T_star**2)
            heat_capacities = np.append(heat_capacities, heat_capacity)

        i += 1


    if plot == True : 

        # ### graphics ###
        # Créer une figure avec 3 sous-graphiques (3 lignes, 1 colonne)
        fig, axs = plt.subplots(1, 3, figsize=(18, 5))  # Ajustez la taille si nécessaire

        # Sous-graphe 1 : Évolution de l'énergie
        axs[0].plot(energies, label='Energie')
        axs[0].plot(mean_energies, label='Energie moyenne', linestyle='--')
        axs[0].set_title("Evolution de l'énergie")
        axs[0].set_xlabel("Pas de simulation")
        axs[0].set_ylabel("Energie")
        axs[0].legend()

        # Sous-graphe 2 : Évolution de l'aimantation
        axs[1].plot(magnetizations, label='Aimantation')
        axs[1].plot(np.abs(mean_magnetizations), label='Aimantation moyenne', linestyle='--')
        axs[1].set_title("Evolution de l'aimantation")
        axs[1].set_xlabel("Pas de simulation")
        axs[1].set_ylabel("Aimantation")
        axs[1].legend()

        # Sous-graphe 3 : Chaleur spécifique
        axs[2].plot(heat_capacities, label='Chaleur spécifique', linestyle='--')
        axs[2].set_title("Chaleur spécifique")
        axs[2].set_xlabel("Pas de simulation")
        axs[2].set_ylabel("C_p")
        axs[2].legend()

        # Ajuster l'espacement entre les sous-graphiques
        plt.tight_layout()

        # Afficher la figure avec les sous-graphiques
        plt.show()

    print("MAGNETIZATION ARE", magnetizations)

    if state.any() == None : 

        return mean_energies[-1], heat_capacities[-1], magnetizations.mean()

    else : 
        return mean_energies[-1], heat_capacities[-1], magnetizations.mean(), state_matrix




