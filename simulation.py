# modules

from transition import transition, initial_energy, calculate_delta_energy
import numpy as np 

# parameters

n = 3
N = n**2
nb_iterations = 100

eps = 0.001  # stopping condition

k_B = 1
mu = 1
J = -10
B = 0

T = 0.001


# dimensionless quantities

B_star = B/(J*mu)
T_star = -0.001

initial_state_matrix = np.random.choice([-1, 1], size=(n, n))

#np.ones((n,n))

energy = initial_energy(initial_state_matrix, B)

state_matrix = initial_state_matrix

print("Initial energy is :", energy)

print(state_matrix)

energies = np.array([energy])
mean_energies = np.array([energy])

##mean_energies

i = 1
while i <= nb_iterations : 

    energy, state_matrix = transition(state_matrix, energy, T_star, n, B_star)
    print(state_matrix)

    energies = np.append(energies, energy)

    mean_energies = np.append(mean_energies, energies.mean())

    i += 1

print(energies)
print(mean_energies)
print(state_matrix)


import matplotlib.pyplot as plt


# Plotting the data
plt.plot(energies, label='Energies')
plt.plot(mean_energies, label='Mean Energies', linestyle='--')

# Add titles and labels
plt.title("Energies and Mean Energies")
plt.xlabel("Index")
plt.ylabel("Energy Value")

# Adding a legend
plt.legend()

# Show plot
plt.show()


