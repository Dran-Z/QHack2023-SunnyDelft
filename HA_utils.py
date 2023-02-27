from openfermion import fermi_hubbard, jordan_wigner, get_sparse_operator
import numpy as np

def get_real_CDF(N_sites, t, U, tau, precision, initial_state_symmetry=True):

    hubbard = fermi_hubbard(1, N_sites, t, U, periodic=False,particle_hole_symmetry=True)
    jw_hamiltonian = jordan_wigner(hubbard)
    fh_matrix = get_sparse_operator(jw_hamiltonian)
    fh_matrix = fh_matrix.todense()
    fh_matrix = fh_matrix.real
    #norm = np.linalg.norm(fh_matrix)
    #tau = np.pi/(4*norm)
    Ndim = 2**(2*N_sites)
    energy, eigenstate= np.linalg.eig(tau*fh_matrix)

    hf_state = np.zeros(Ndim)


    if initial_state_symmetry:
        index_1 = int('0110'*(N_sites//2),2)
        index_2 = int('1001'*(N_sites//2),2)
        #index_1 = int('1100'*(N_sites//2),2)
        #index_2 = int('0011'*(N_sites//2),2)
        hf_state[index_1], hf_state[index_2] = 1/np.sqrt(2), 1/np.sqrt(2)
    else:
        hf_index = 0
        for i in range(N_sites):
            if i%2==0:
                hf_index += 2**(2*i)
            elif i%2!=0:
                hf_index += 2**(2*i+1)
        hf_state[hf_index] = 1

    energy=energy.real
    eigenstate[np.abs(eigenstate)<1e-10]=0
    eigenstate = np.array(eigenstate)

    prob_raw = np.zeros(Ndim)
    for i in range(Ndim):
        prob_raw[i] = np.abs(np.dot(hf_state,eigenstate[:,i]))**2
    prob = []
    ener = []
    for i,ele in enumerate(prob_raw):
        if ele!=0:
            prob.append(ele)
            ener.append(energy[i].real)

    x_list = np.linspace(-np.pi/3, np.pi/3, precision)
    CDF = np.zeros(len(x_list))

    for j,ener_ele in enumerate(ener):

        
        for i,x_ele in enumerate(x_list):
            if x_ele>ener_ele:
                
                CDF[i] += prob[j]

    return CDF

def get_fh_matrix(N_sites, t, U):

    hubbard = fermi_hubbard(1, N_sites, t, U, periodic=False,particle_hole_symmetry=True)
    jw_hamiltonian = jordan_wigner(hubbard)
    fh_matrix = get_sparse_operator(jw_hamiltonian)
    fh_matrix = fh_matrix.todense().real


    return fh_matrix

def Assembly_ACDF(Z_list, F_list, precision):
    
    ACDF = .5*np.ones(precision)
    x_list = np.linspace(-np.pi/3,np.pi/3,precision)
    d = len(F_list)-1
    
    for j in range(d+1):
        ACDF = ACDF + F_list[j]*Z_list[j]*np.exp(1j*(2*j+1)*x_list) - F_list[j]*Z_list[j].conj()*np.exp(-1j*(2*j+1)*x_list)
        #ACDF = ACDF + F_list[j]*Z_list[j]*2j*np.sin((2*j+1)*x_list)
                                                                              
    return ACDF