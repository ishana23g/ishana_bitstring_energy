# ham, conf, T=2, nsweep=8000, nburn=2000

from .BitString import BitString as bs
from .Energy import IsingHamiltonian as ham
import numpy as np

def metropolis_montecarlo(hamiltonian: ham,
                          configuration: bs,
                          T: int, nsweep: int,
                          nburn: int) -> tuple:
    """
    This function performs the Metropolis Monte Carlo algorithm to sample the
    energy and magnetization of a given Ising Hamiltonian.

    Parameters
    ----------
    hamiltonian : IsingHamiltonian
        The Ising Hamiltonian that we are sampling
    configuration : BitString
        The initial configuration of the system
    T : int
        The temperature of the system
    number_sweep : int
        The number of sweeps to perform
    number_burn : int
        The number of sweeps to burn

    Returns
    -------
    tuple
        The energy, magnetization, energy squared, and magnetization squared
    """
    for j in range(nburn):
        configuration = metropolis_step(hamiltonian, configuration, T)

    E_array = np.zeros(nsweep)
    M_array = np.zeros(nsweep)
    EE_array = np.zeros(nsweep)
    MM_array = np.zeros(nsweep)
    E_array[0], M_array[0] = hamiltonian.compute_energy_and_mag(configuration, T)
    EE_array[0] = E_array[0]*E_array[0]
    MM_array[0] = M_array[0]*M_array[0]
    for i in range(1, nsweep):
        configuration = metropolis_step(hamiltonian, configuration, T)
        E, M = hamiltonian.compute_energy_and_mag(configuration, T)

        # E_array[i] = E
        E_array[i]  = (E_array[i-1]*(i) + E)/(i+1)
        EE_array[i] = (EE_array[i-1]*(i) + E*E)/(i+1)

        #M_array[i]  = M
        M_array[i]  = (M_array[i-1]*(i) + M)/(i+1)
        MM_array[i] = (MM_array[i-1]*(i) + M*M)/(i+1)
    return E_array, M_array, EE_array, MM_array


def metropolis_step(hamiltonian: ham,
                    configuration: bs,
                    T: int,) -> bs:
    """
    Taking a single step forward in the Metropolis Monte Carlo algorithm

    Parameters
    ----------
    hamiltonian : IsingHamiltonian
        The Ising Hamiltonian that we are sampling
    configuration : BitString
        The initial configuration of the system
    T : int
        The temperature of the system

    Returns
    -------
    BitString
        The new configuration of the system
    """

    # for i in range (len(configuration)):
    #     e_alpha = hamiltonian.energy(configuration)
    #     # possible flip
    #     if configuration.config[i] == 1:
    #         configuration.flip(i)
    #     e_beta = hamiltonian.energy(configuration)

    #     # compute the probability of flipping
    #     e_delta = np.exp (-(e_beta - e_alpha)/T)
    #     random_flip = np.random.rand()
    #     if random_flip > e_delta:
    #         # flip back to original configuration
    #         configuration.flip(i)

    # return configuration

    for site_i in range(configuration.n):
            delta_e = 0.0
            del_si = 2
            if configuration.config[site_i] == 1:
                del_si = -2

            for j in hamiltonian.J[site_i]:
                delta_e += (2.0*configuration.config[j[0]]-1.0) * j[1] * del_si

            delta_e += hamiltonian.mu[site_i] * del_si

            accept = True
            if delta_e > 0.0:
                rand_comp = np.random.random()
                if rand_comp > np.exp(-delta_e/T):
                    accept = False
            if accept:
                if configuration.config[site_i] == 0:
                    configuration.config[site_i] = 1
                else:
                    configuration.config[site_i] = 0
    return configuration


