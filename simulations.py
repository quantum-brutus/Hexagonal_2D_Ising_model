### modules ###

from transition import transition, initial_energy
import numpy as np
import matplotlib.pyplot as plt


def simulation(B_star_norm, T_star, n, nb_iterations):
    
    N = n**2
    B_star = np.sign(T_star)*B_star_norm

    ### initialisation ###

    initial_state_matrix = np.random.choice([-1, 1], size=(n, n))
    energy = initial_energy(initial_state_matrix, B_star, T_star)

    print(initial_state_matrix)
    print("Initial energy is :", energy)



    # energy
    energies = np.array([energy]) # the energies of each state
    mean_energies = np.array([energy]) # the mean energy of all the steps realized

    # magnetization
    magnetizations = np.array([np.sum(initial_state_matrix)/N]) # the magnetizations of each state
    mean_magnetizations = np.array([np.sum(initial_state_matrix)/N]) # the mean magnetization of all the steps realized

    # heat capacity
    heat_capacities = np.array([0])

    state_matrix = initial_state_matrix



    # first step

    energy, state_matrix = transition(state_matrix, energy, n, B_star, T_star)
    magnetization = np.sum(state_matrix)/N
    print(state_matrix)

    # saving the energies
    energies = np.append(energies, energy)
    mean_energies = np.append(mean_energies, energies.mean())
    heat_capacities = np.append(heat_capacities, np.var(energies, ddof=1))

    # saving the magnetizations
    magnetizations = np.append(magnetizations, magnetization)
    mean_magnetizations = np.append(mean_magnetizations, magnetizations.mean())

    ### loop ###

    i = 1
    while i <= nb_iterations :

        energy, state_matrix = transition(state_matrix, energy, n, B_star, T_star)
        magnetization = np.sum(state_matrix)/N
        print(state_matrix)

        # saving the energies
        energies = np.append(energies, energy)
        mean_energies = np.append(mean_energies, energies.mean())
        heat_capacities = np.append(heat_capacities, np.var(energies, ddof=1))

        # saving the magnetizations
        magnetizations = np.append(magnetizations, magnetization)
        mean_magnetizations = np.append(mean_magnetizations, magnetizations.mean())

        i += 1

    heat_capacities/=T_star**2



    # ### graphics ###


    # # Plotting the data

    # plt.plot(energies, label='Energie')
    # plt.plot(mean_energies, label='Energie moyenne', linestyle='--')

    # # Add titles and labels
    # plt.title("Evolution de l'énergie")
    # plt.xlabel("Pas de simulation")
    # plt.ylabel("Energie")

    # # Adding a legend
    # plt.legend()

    # plt.show()

    # plt.plot(magnetizations, label='Aimantation')
    # plt.plot(mean_magnetizations, label='Aimantation moyenne', linestyle='--')

    # plt.title("Evolution de l'aimantation")
    # plt.xlabel("Pas de simulation")
    # plt.ylabel("Aimantation")

    # # Adding a legend
    # plt.legend()

    # # Show plot
    # plt.show()


    # plt.plot(heat_capacities, label='Chaleur spécifique', linestyle='--')

    # plt.title("Chaleur spécifique")
    # plt.xlabel("Pas de simulation")
    # plt.ylabel("C_p")

    # # Adding a legend
    # plt.legend()

    # # Show plot
    # plt.show()

    return mean_energies[-1], heat_capacities[-1], mean_magnetizations[-1]




