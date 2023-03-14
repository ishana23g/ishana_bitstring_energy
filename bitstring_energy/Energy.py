"""Provide the primary functions."""

import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from .BitString import BitString

def energy(bs: BitString, G: nx.Graph) -> float:
    """
    Compute energy of configuration, given a bit string

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : nx.Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """

    # convert bit string such that for 0 -> -1 and 1 -> 1
    array = np.array(bs.return_array())
    bitString = (array * 2) - 1

    energy = 0
    for (i, j) in G.edges:
        energy += G.edges[i, j]["weight"] * bitString[i] * bitString[j]
    return energy


def calculate_all_possible_energy(G: nx.Graph, 
                                  give_lowest_state: bool = True, 
                                  give_highest_state: bool = False,
                                  give_graph: bool = True) -> tuple:
    """
    Calculates all the possible energy states of a graph and plots them as a line graph
    If provided, it will also return the minimum and maximum energy of the graph

    Parameters
    ----------
    G : nx.Graph
        Input graph defining the Hamiltonian
    give_lowest_state : bool
        Whether to return the lowest energy state
    give_highest_state : bool
        Whether to return the highest energy state
    give_graph : bool
        Whether to plot the graph

    Returns
    -------
    (lowest, highest) : tuples
        The lowest and highest energy states of the graph
        But if one or more of them are not requested, it will be `None` for that state
    """
    x_y_dict = dict() # Store the indices and energies in a dictionary
    num_nodes = G.number_of_nodes()
    my_bs = BitString([0] * num_nodes)
    min_bs = BitString([0] * num_nodes)
    max_bs = BitString([0] * num_nodes)

    # x = []
    # y = []

    for b in range(0,  2**num_nodes+1):
        my_bs.set_int(b, digits=num_nodes)
        # x.append(b)
        # y.append(energy(my_bs, G))
        x_y_dict[b] = energy(my_bs, G)

    # Print out all the energies
    if give_graph:
        plt.plot(*zip(*sorted(x_y_dict.items())))
        plt.show()

    if give_lowest_state:
        xmin = min(x_y_dict, key=x_y_dict.get)
        emin = x_y_dict[xmin]
        min_bs.set_int(xmin,digits=num_nodes)
        print(f"Lowest energy {emin}: {min_bs}")

    if give_highest_state:
        xmax = max(x_y_dict, key=x_y_dict.get)
        emax = x_y_dict[xmax]
        max_bs.set_int(xmax,digits=num_nodes)
        print(f"Highest energy {emax}: {max_bs}")

    if give_lowest_state and give_highest_state:
        return (min_bs, max_bs)
    elif give_lowest_state:
        return (min_bs, None)
    elif give_highest_state:
        return (None, max_bs)
    else:
        return (None, None)
