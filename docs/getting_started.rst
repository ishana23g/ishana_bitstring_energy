Getting Started
===============

This page details how to get started with bitstring_energy.

Usage
--------
Once installed, a simple use case of bitstring_energy can be seen as follows:

.. code-block:: python
    
    import bitstring_energy as bse
    import numpy as np

    conf = bse.BitString(N=N)
    conf.set_config([0, 0, 0, 0, 0, 0, 1, 1])
    Ei = ham.energy(conf)
    print(" Energy of      ", conf.config, " is ", Ei)