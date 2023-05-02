import bitstring_energy as bse
import networkx as nx
import numpy as np


 # Create graph
def build_1d_graph(N, Jval):
    """
    Build a 1D graph with a single J value (Jval)
    """
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    return G

# Create another specific graph
def build_1d_graph_2(N, Jval):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    G.add_edge(2,5)
    G.add_edge(4,8)
    G.add_edge(4,0)
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    return G

# Now let's define a function that converts a graph into a simpler IsingHamiltonian object
def get_IsingHamiltonian(G, mus=None):
    if mus == None:
        mus = np.zeros(len(G.nodes()))

    if len(G.nodes()) != len(mus):
        raise Exception("DimensionMismatch")

    if len(G.nodes()) != len(mus):
        raise Exception("Dimension Mismatch")
    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    return bse.IsingHamiltonian(J,mus)

# Testing the energy function on a 1D Ising model
def test_energy():    
    N = 8
    Jval = 1
    G = build_1d_graph(N, Jval)
    ham = get_IsingHamiltonian(G, mus=[.1 for i in range(N)])

    conf = bse.BitString(N)
    conf.set_config([0, 0, 0, 0, 0, 0, 1, 1])
    Ei = ham.energy(conf)
    true_Ei = 3.6
    assert np.isclose(Ei, true_Ei), "Calculated Energy is not correct"

    conf.set_int_config(106)
    Ei = ham.energy(conf)
    true_Ei = -4.0
    assert np.isclose(Ei, true_Ei), "Calculated Energy is not correct"

    N = 10
    Jval = 1
    G2 = build_1d_graph_2(N, Jval)
    ham2 = get_IsingHamiltonian(G2, mus=[.1 for i in range(N)])

    conf.set_config(np.zeros(N))
    Ei = ham2.energy(conf)
    true_Ei = 11
    assert np.isclose(Ei, true_Ei), "Calculated Energy is not correct"

    conf.set_config(np.ones(N))
    Ei = ham2.energy(conf)
    true_Ei = 13
    assert np.isclose(Ei, true_Ei), "Calculated Energy is not correct"

    # NOT Testing the calculating all possible energy states
    # lowest_energy_state, = ham2.calculate_all_possible_energy(G, give_lowest_state=True, give_highest_state=False, give_graph=False)
    # expected_lowest_energy_state = bse.BitString([0,0,1,0,1,0,0,1,0,1])
    # assert lowest_energy_state == expected_lowest_energy_state, f"The lowest energy state should be {expected_lowest_energy_state}. However we got {lowest_energy_state}"
    
    # lowest_energy = bse.energy(lowest_energy_state, G)
    # assert lowest_energy == -9, f"The lowest energy should be -9. However we got {lowest_energy}"

def test_avg_values():
    # Define a new configuration instance for a 6-site lattice
    N = 6
    conf = bse.BitString(N=N)

    # Define a new hamiltonian values
    G = build_1d_graph(N, 2)
    ham = get_IsingHamiltonian(G, mus=[1.1 for i in range(N)])

    # Compute the average values for Temperature = 1
    E, M, HC, MS = ham.compute_average_values(conf, 1)

    assert np.isclose(E,  -11.90432015)
    assert np.isclose(M,  -0.02660820)
    assert np.isclose(HC, 0.59026994)
    assert np.isclose(MS, 0.05404295) 

def test_metropolis_montecarlo():

    import bitstring_energy as bse 
import networkx as nx
import numpy as np


def test_monte_carlo():
    # Initialize BitString
    N = 8
    Jval = 1
    G = build_1d_graph(N, Jval)
    ham = get_IsingHamiltonian(G, mus=[.1 for i in range(N)])

    # Initialize BitString
    conf = bse.BitString(N=N)
    conf.initialize(M=4)   # run montecarlo
    T = 2
    E, M, EE, MM = bse.metropolis_montecarlo(ham, conf, T=2, nsweep=8000, nburn=2000)     
    HC = (EE[-1] - E[-1]*E[-1])/T/T
    MS = (MM[-1] - M[-1]*M[-1])/T
    print("     E:  %12.8f" %(E[-1]))
    print("     M:  %12.8f" %(M[-1]))
    print("     HC: %12.8f" %(HC))
    print("     MS: %12.8f" %(MS))
    # Exact values
    # E:   -3.73231850
    # M:    0.14658168
    # EE:   1.64589165
    # MM:   1.46663062   
    assert np.isclose(E[-1], -3.73231850, rtol=1e+1), "Calculated Energy is not correct"
    assert np.isclose(M[-1], 0.14658168, rtol=1e+1), "Calculated Magnetization is not correct"
    assert np.isclose(HC, 1.64589165, rtol=1e+1),  "Calculated Heat Capacity is not correct"
    assert np.isclose(MS, 1.46663062, rtol=1e+1), "Calculated Magnetic Susceptibility is not correct"

    
   