from simulations import simulation
import matplotlib.pyplot as plt
import numpy as np

###################### parameters ###########################

n = 8
N = n**2
nb_iterations = 100000
plot = False ## if true : plot the mean energies, magnetization, heat capacity and their values depending on the simulation step
            ## else : plot the mean energies, magnetization, heat capacity depending on the Temperature


'''
everything is normalized by the factor 1/2*J*mu**2,
and the Boltzmann constant k_B is attached to T_star
'''
B_star_norm = 0  # norm of the applied magnetic fiel, must be POSITIVE
T = [-4 + 0.2*i for i in range(18)]  # range of simulation temperatures

#############################################################

energies, capacities, magnetizations = [], [], []

for T_star in T : 

    energy, capacity, magnetization = simulation(B_star_norm, T_star, n, nb_iterations, plot)

    energies.append(energy)
    capacities.append(capacity)
    magnetizations.append(magnetization)



if not(plot) : 
    ### plots ###

    # Créer une figure avec 1 ligne et 3 colonnes de sous-graphiques
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))  # Ajuste la taille pour une meilleure lisibilité

    # Sous-graphe 1 : Évolution de l'énergie moyenne
    axs[0].plot(T, energies, label='Énergie moyenne', linestyle='--')
    axs[0].set_title("Évolution de l'énergie moyenne")
    axs[0].set_xlabel("Température")
    axs[0].set_ylabel("Énergie")
    axs[0].legend()

    # Sous-graphe 2 : Aimantation moyenne avec mise à l’échelle
    axs[2].plot(T, np.abs(magnetizations), label='Aimantation moyenne', linestyle='--')
    axs[2].set_title("Évolution de l'aimantation moyenne")
    axs[2].set_xlabel("Température")
    axs[2].set_ylabel("Aimantation")
    axs[2].set_ylim(0, 1)  # Limite l'échelle entre -1 et 1
    axs[2].legend()


    # Sous-graphe 3 : Chaleur spécifique
    axs[1].plot(T, capacities, label='Chaleur spécifique', linestyle='--')
    axs[1].set_title("Chaleur spécifique")
    axs[1].set_xlabel("Température")
    axs[1].set_ylabel("Capacité thermique")
    axs[1].legend()

    # Ajuster l'espacement entre les sous-graphiques
    plt.tight_layout()

    # Afficher la figure avec les sous-graphiques côte à côte
    plt.show()
