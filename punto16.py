import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("monthrg.dat")
def DFT(x):
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j*np.pi * k * n / N)
    return np.dot(e, x)