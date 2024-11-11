###################### imports ###########################
from simulations import simulation
import matplotlib.pyplot as plt
import numpy as np


###################### parameters ###########################
# everything is normalized by the factor 1/2*J*mu**2,
# and the Boltzmann constant k_B is attached to T_star

n = [10]
N = [n**2 for n in n]
nb_iterations = 50000


import time

start = time.time()

hexagonal = False
plot = False  ## if true : plot the mean energies, magnetization, heat capacity and their values depending on the simulation step
            ## else : plot the mean energies, magnetization, heat capacity depending on the Temperature

B_star_norm = 0  # norm of the applied magnetic field, must be POSITIVE
T = [0.1*i for i in range(1,45)]  # range of simulation temperatures. A negative value of temperature means a negative coupling coefficient between spins

#############################################################


energies, capacities, magnetizations = [[] for i in n], [[] for i in n], [[] for i in n]

for index, number_of_atoms in enumerate(n) : 

    for T_star in T : 

        energy, capacity, magnetization = simulation(B_star_norm, T_star, number_of_atoms, nb_iterations, plot, hexagonal)

        energies[index].append(energy)
        capacities[index].append(capacity)
        magnetizations[index].append(magnetization)



if not(plot) : 
    ### plots ###

    # Create a figure with 1 row and 3 columns of subplots
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Define colors and styles for each plot
    colors = ["royalblue", "darkorange", "seagreen"]
    linestyles = ["--", "--", "--"]
    linewidth = 1.5

    if T[0] <0 : 
        T_corrected = [-1*i for i in T]

    else : 
        T_corrected = [i for i in T]


    # Loop over each index and value of n to plot data for each n
    for idx, n_values in enumerate(n):
        color = colors[idx % len(colors)]
        linestyle = linestyles[idx % len(linestyles)]
        
        # Subplot 1: Evolution of Average Energy for each n
        axs[0].plot(T_corrected, energies[idx], '.', label=f'n={n_values}', linestyle=linestyle, color=color, linewidth=linewidth)
        
        # Subplot 2: Average Magnetization for each n
        axs[1].plot(T_corrected, np.abs(magnetizations[idx]), '.',label=f'n={n_values}', linestyle=linestyle, color=color, linewidth=linewidth)
        
        # Subplot 3: Specific Heat Capacity for each n
        axs[2].plot(T_corrected, capacities[idx], '.',label=f'n={n_values}', linestyle=linestyle, color=color, linewidth=linewidth)

    # Subplot settings for titles, labels, legends, and grids
    axs[0].set_title("Évolution de l'énergie moyenne", fontsize=14, fontweight='bold')
    axs[0].set_xlabel("Température adimensionnée", fontsize=12)
    axs[0].set_ylabel("Énergie adimensionnée", fontsize=12)
    axs[0].legend(loc="best", fontsize=7)
    axs[0].grid(True, linestyle=":", color="grey", alpha=0.6)

    axs[1].set_title("Évolution de l'aimantation moyenne", fontsize=14, fontweight='bold')
    axs[1].set_xlabel("Température adimensionnée", fontsize=12)
    axs[1].set_ylabel("Aimantation (en valeur absolue) adimensionnée", fontsize=10)
    axs[1].set_ylim(0, 1)
    axs[1].legend(loc="best", fontsize=7)
    axs[1].grid(True, linestyle=":", color="grey", alpha=0.6)

    axs[2].set_title("Capacité thermique", fontsize=14, fontweight='bold')
    axs[2].set_xlabel("Température adimensionnée", fontsize=12)
    axs[2].set_ylabel("Capacité thermique adimensionnée", fontsize=11)
    axs[2].legend(loc="best", fontsize=7)
    axs[2].grid(True, linestyle=":", color="grey", alpha=0.6)

    # Adjust layout and add a main title for the figure
    fig.suptitle("Analyse Thermodynamique", fontsize=18, fontweight='bold')


    # Subtitle positioned slightly below the main title
    # plt.text(0.5, 0.9, "Cas ferromagnétique : J<0 ", 
    #         ha='center', va='top', fontsize=14, transform=fig.transFigure)
    
    # Adjust layout to prevent overlap
    plt.tight_layout(pad=3)   



    end = time.time()

    time = end-start 

    print("TIME WAS ", time)

    # Show the figure
    plt.show()