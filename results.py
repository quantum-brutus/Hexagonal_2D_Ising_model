from simulations import simulation
import matplotlib.pyplot as plt
import numpy as np

###################### parameters ###########################

n = 4
N = n**2
nb_iterations = 1000


'''
everything is normalized by the factor 1/2*J*mu**2,
and the Boltzmann constant k_B is attached to T_star
'''
B_star_norm = 0  # norm of the applied magnetic fiel, must be POSITIVE
T = [10, 50, 100, 200, 500]  # range of simulation temperatures

#############################################################

energies, capacities, magnetizations = [], [], []

for T_star in T : 

    energy, capacity, magnetization = simulation(B_star_norm, T_star, n, nb_iterations)

    energies.append(energy)
    capacities.append(capacity)
    magnetizations.append(magnetization)




### plots ###

plt.plot(T, energies, label='Energie moyenne', linestyle='--')
plt.legend()
plt.show()

plt.plot(T, capacities, label='Chaleur spécifique', linestyle='--')
plt.legend()
plt.show()

plt.plot(T, magnetizations, label='Aimantation moyenne', linestyle='--')
plt.legend()
plt.show()