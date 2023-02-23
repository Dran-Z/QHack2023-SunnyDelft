# QHack2023-SunnyDelft
This is Team SunnyDelft's repo for the [QHack2023 Hackathon](https://github.com/XanaduAI/QHack2023/issues/10). 

## Project Description

Finding the ground state energy for Hamiltonians is a core task in Quantum Chemistry and Quantum Simulation. Despite that Quantum Phase Estimation can find the ground state energy with superior complexity than classical algorithms, it's prone to noise and of no practical use for the NISQ era. On the Contrary, Variational Quantum Algorithms (VQAs) have been proposed to extract quantum power on NISQ devices. Nevertheless, VQAs are suffering from the noise-induced barren plateau and no performance guarantee can be made due to their variational nature.

Recently, there is a novel algorithm [(PRX Quantum 3, 010318)](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.010318) that claims it will reach the Heisenberg limit on NISQ devices. The Hybrid algorithm requires coefficient calculation on classical routine and sampling on quantum routine and is tolerant to noisy sampling. A follow-up work further improved the algorithm with randomly-compiled Hamiltonian and more precise coefficient calculation [(Phys. Rev. Lett. 129, 030503)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.030503). However, there has been no experimental demonstration so far and it's not clear how the algorithms will actually perform in a real noisy environment.

In this project, We aim to:
-  replicate the result in the paper
-  demonstrate the algorithm on real devices
-  develop error-mitigation techniques for it