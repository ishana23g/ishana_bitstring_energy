"""Provide the primary functions."""

import numpy as np
import networkx as nx
from .BitString import BitString


class IsingHamiltonian:
    def __init__(self, J:np.array, mu:np.array) -> None:
        """
        Initialize the Ising Hamiltonian
        Convert the J array into a matrix 
        
        Parameters
        ----------
        J : np.array
            Coupling constant between a set of two spins
        mu : np.array
            Magnetic field that acts on each spin
        """
        self.J = J
        self.mu = mu
        J_matrix = np.zeros((len(J), len(J)))
        for row_i in range(len(J)):
            # row_i : int
            for col_i in range(row_i, len(J)):
                # col_i : int
                if (row_i == col_i):
                    J_matrix[row_i][col_i] = mu[row_i]
                else:
                    for neighbor in J[row_i]:
                        if (neighbor[0] == col_i):
                            J_matrix[row_i][col_i] = neighbor[1]
        self.J_matrix = J_matrix


    # def energy(self, bs: BitString, G: nx.Graph) -> float:
    #     """
    #     Compute energy of configuration, given a bit string

    #         .. math::
    #             E = \\left<\\hat{H}\\right>

    #     Parameters
    #     ----------
    #     bs   : Bitstring
    #         input configuration
    #     G    : nx.Graph
    #         input graph defining the Hamiltonian
    #     Returns
    #     -------
    #     energy  : float
    #         Energy of the input configuration
    #     """

    #     # convert bit string such that for 0 -> -1 and 1 -> 1
    #     array = np.array(bs.return_array())
    #     bitString = (array * 2) - 1

    #     energy = 0
    #     for (i, j) in G.edges:
    #         energy += G.edges[i, j]["weight"] * bitString[i] * bitString[j]
    #     return energy

    def energy(self, bs: BitString) -> float:
        """
        Given a bitstring, compute the energy of the configuration 
        using the Ising Hamiltonian (Js and mus) defined by the class

        Parameters
        ----------
        bs : BitString
            Input bitstring
        Returns
        -------
        energy : float
            Energy of the configuration
        """

        # convert bit string such that for 0 -> -1 and 1 -> 1
        bitString = (np.array(bs.config) * 2) - 1

        # J: [[(1, 1.0), (2, 1.0)], [(0, 1.0), (2, 1.0)], [(0, 1.0), (1, 1.0)]]
        energy = np.dot(self.mu, bitString)
        for i in range(bs.n):
            for neighbor in self.J[i]:
                if (neighbor[0] < i):
                    continue
                energy += neighbor[1] * bitString[neighbor[0]] * bitString[i]
        return energy
    

        # take the dot product of the J matrix and the bitstring
        # return bitString.T @ self.J_matrix @ bitString
    
    def compute_average_values(self, bs: BitString, temp: float) -> tuple:
        """
        Compute the average values of the 
        Energy, Magnetization, Heat Capacity, and Magnetic Susceptibility

        Parameters
        ----------
        bs : BitString
            Input bitstring
        temp : float
            Temperature of the system
        """

        E = 0
        M = 0
        EE = 0
        MM = 0
        Z = 0

        for b in range(0, 2**bs.n):
            bs.set_int_config(b, digits=bs.n)
            Ei, Mi = self.compute_energy_and_mag(bs, temp)
            Zi = np.exp(-Ei/temp)
            E += Ei * Zi

            # Ei = self.energy(bs)
            # Mi = np.sum(2*bs.config - 1)
            M += Mi * Zi

            EE += Ei**2 * Zi
            MM += Mi**2 * Zi

            Z += Zi
        
        E /= Z
        M /= Z
        EE /= Z
        MM /= Z

        HC = (EE - E**2) / temp**2
        MS = (MM - M**2) / temp
        return (E, M, HC, MS)

    def compute_energy_and_mag(self, bs: BitString, temp: float) -> tuple:
        """
        Compute the values of
        Energy and Magnetization for a given temperature

        Parameters
        ----------
        bs : BitString
            Input bitstring
        temp : float
            Temperature of the system
        """
        Ei = self.energy(bs)
        Mi = np.sum(2*bs.config - 1)
        return (Ei, Mi)
    
    
# def calculate_all_possible_energy(self, G: nx.Graph, 
#                                 give_lowest_state: bool = True, 
#                                 give_highest_state: bool = False,
#                                 give_graph: bool = True) -> tuple:
#     """
#     Calculates all the possible energy states of a graph and plots them as a line graph
#     If provided, it will also return the minimum and maximum energy of the graph

#     Parameters
#     ----------
#     G : nx.Graph
#         Input graph defining the Hamiltonian
#     give_lowest_state : bool
#         Whether to return the lowest energy state
#     give_highest_state : bool
#         Whether to return the highest energy state
#     give_graph : bool
#         Whether to plot the graph

#     Returns
#     -------
#     (lowest, highest) : tuple
#         The lowest and highest energy states of the graph
#         But if one or more of them are not requested, it will be `None` for that state
#     """
#     x_y_dict = dict() # Store the indices and energies in a dictionary
#     num_nodes = G.number_of_nodes()
#     current_bs = BitString([0] * num_nodes)
#     min_bs = BitString([0] * num_nodes)
#     max_bs = BitString([0] * num_nodes)

#     # x = []
#     # y = []

#     for b in range(0,  2**num_nodes+1):
#         current_bs.set_int_config(b, digits=num_nodes)
#         # x.append(b)
#         # y.append(energy(my_bs, G))
#         x_y_dict[b] = self.energy(current_bs)

#     # Print out all the energies
#     if give_graph:
#         plt.plot(*zip(*sorted(x_y_dict.items())))
#         plt.show()

#     if give_lowest_state:
#         index_min = min(x_y_dict, key=x_y_dict.get)
#         energy_min = x_y_dict[index_min]
#         min_bs.set_int(index_min,digits=num_nodes)
#         print(f"Lowest energy {energy_min}: {min_bs}")

#     if give_highest_state:
#         index_max = max(x_y_dict, key=x_y_dict.get)
#         energy_max = x_y_dict[index_max]
#         max_bs.set_int(index_max,digits=num_nodes)
#         print(f"Highest energy {energy_max}: {max_bs}")

#     if give_lowest_state and give_highest_state:
#         return (min_bs, max_bs)
#     elif give_lowest_state:
#         return (min_bs, None)
#     elif give_highest_state:
#         return (None, max_bs)
#     else:
#         return (None, None)
