import bitstring_energy as bse
import networkx as nx


# Testing the energy function on a 1D Ising model
def test_energy():
    pass
    # G = nx.Graph()
    # G.add_nodes_from([i for i in range(10)])
    # G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(10)])
    # G.add_edge(2,5)
    # G.add_edge(4,8)
    # G.add_edge(4,0)
    # for e in G.edges:
    #     G.edges[e]['weight'] = 1.0

    # energy_of_all_0s =  bse.energy(bse.BitString([0]*10), G)
    # assert energy_of_all_0s == 13.0, f"Energy of all 0s should be 13.0 given the input state. However we got {energy_of_all_0s}"

    # energy_of_all_1s =  bse.energy(bse.BitString([1]*10), G)
    # assert energy_of_all_1s == 13.0, f"Energy of all 1s should be 13.0 given the input state. However we got {energy_of_all_1s}"

    # lowest_energy_state, higest_energy = bse.calculate_all_possible_energy(G, give_lowest_state=True, give_highest_state=False, give_graph=False)
    # expected_lowest_energy_state = bse.BitString([0,0,1,0,1,0,0,1,0,1])
    # assert lowest_energy_state == expected_lowest_energy_state, f"The lowest energy state should be {expected_lowest_energy_state}. However we got {lowest_energy_state}"
    
    # lowest_energy = bse.energy(lowest_energy_state, G)
    # assert lowest_energy == -9, f"The lowest energy should be -9. However we got {lowest_energy}"