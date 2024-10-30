### modules ###

from transition import transition, initial_energy
import numpy as np



### parameters ###

n = 3
N = n**2
nb_iterations = 1000

eps = 0.001  # stopping condition

# k_B = 
# mu = 
# J = 
# B =
# T =



### dimensionless quantities ###

B_star = 10
T_star = 100



### initialisation ###

#initial_state_matrix = np.random.choice([-1, 1], size=(n, n))
initial_state_matrix = np.ones((n,n))
energy = initial_energy(initial_state_matrix, B_star)

print(initial_state_matrix)
print("Initial energy is :", energy)



### loop ###

energies = np.array([energy]) # the energies of each state
mean_energies = np.array([energy]) # the mean energy of all the steps realized

magnetizations = np.array([np.sum(initial_state_matrix)/N]) # the magnetizations of each state
mean_magnetizations = np.array([np.sum(initial_state_matrix)/N]) # the mean magnetization of all the steps realized

state_matrix = initial_state_matrix



# first step

energy, state_matrix = transition(state_matrix, energy, T_star, n, B_star)
print(state_matrix)

# saving the energies
energies = np.append(energies, energy)
mean_energies = np.append(mean_energies, energies.mean())

i = 1
while i <= nb_iterations :

    energy, state_matrix = transition(state_matrix, energy, T_star, n, B_star)
    magnetization = np.sum(state_matrix)/N
    print(state_matrix)

    # saving the energies
    energies = np.append(energies, energy)
    mean_energies = np.append(mean_energies, energies.mean())

    # saving the magnetizations
    magnetizations = np.append(magnetizations, magnetization)
    mean_magnetizations = np.append(mean_magnetizations, magnetizations.mean())

    i += 1

print(energies)
print(mean_energies)
print(state_matrix)

if i == nb_iterations + 1:
    print("Stopping condition : Number of iterations")
else:
    print("Stopping condition : Optimal mean energy found ! Value :", mean_energies[-1])



### graphics ###

import matplotlib.pyplot as plt


# Plotting the data
plt.plot(energies, label='Energie')
plt.plot(mean_energies, label='Energie moyenne', linestyle='--')

# Add titles and labels
plt.title("Evolution de l'énergie")
plt.xlabel("Pas de simulation")
plt.ylabel("Energie")

plt.show()


plt.plot(mean_magnetizations, label='Aimantation moyenne', linestyle='--')

plt.title("Evolution de l'aimantation")
plt.xlabel("Pas de simulation")
plt.ylabel("Aimantation")

# Adding a legend
plt.legend()

# Show plot
plt.show()


