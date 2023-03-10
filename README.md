# QHack2023-SunnyDelft
This is Team SunnyDelft's repo for the [QHack2023 Hackathon](https://github.com/XanaduAI/QHack2023/issues/59). 

## Project Description

Finding the ground state energy for Hamiltonians is a core task in Quantum Chemistry and Quantum Simulation. Despite that Quantum Phase Estimation can find the ground state energy with superior complexity than classical algorithms, it's prone to noise and of no practical use for the NISQ era. On the Contrary, Variational Quantum Algorithms (VQAs) have been proposed to extract quantum power on NISQ devices. Nevertheless, VQAs are suffering from the noise-induced barren plateau and no performance guarantee can be made due to their variational nature.

Recently, there is a novel algorithm [(PRX Quantum 3, 010318)](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.3.010318) that claims it will reach the Heisenberg limit on NISQ devices. The Hybrid algorithm requires coefficient calculation on classical routine and sampling on quantum routine and is tolerant to noisy sampling. A follow-up work further improved the algorithm with randomly-compiled Hamiltonian and more precise coefficient calculation [(Phys. Rev. Lett. 129, 030503)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.030503). However, there has been no experimental demonstration so far and it's not clear how the algorithms will actually perform in a real noisy environment.

In this short Hackathon project, 
-   we successfully implemented this algorithm using both `Qiskit` and `AWS-braket`. We reproduced the result shown in the original paper, and further took a more practical view on the algorithm implementation. 
-   We also put the algorithm on a noisy quantum simulator and used error mitigation for the results.
-   We tried to run our algorithm on `ibm_guadalupe`, but the noise scale is to large and no useful results can be extracted even with error mitigation.

You can first take a look at our [slides](QHack-SunnyDelft.pdf) for an overview of our result. If you are interested in our code implementation, we recommend you start with `HA_noiseless_qiskit.ipynb` [[here](HA_noiseless_qiskit.ipynb)] where we have some explanations about how to implement the algorithm in the quantum routine. We also have a notebook `F_list_calculation.ipynb` [[here](F_list_calculation.ipynb)] to introduce our classical routine about F coefficient calculation. 

For `AWS-braket` version of code, please check `HA_noiseless_braket.ipynb` [[here](HA_noiseless_braket.ipynb)]. For noisy simulation, please check `HA_noisy_qiskit.ipynb` [[here](HA_noisy_qiskit.ipynb)]. For code of real-backend submission, please check `HA_real_qiskit.ipynb` [[here](HA_real_qiskit.ipynb)].


    