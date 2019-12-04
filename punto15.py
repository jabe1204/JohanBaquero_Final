import numpy as np
import matplotlib.pyplot as plt

datax = np.loadtxt("valores.txt")
n_points = 10**5
    
def proba_sigma(s,x):
    p = (np.exp(-1/2*((x**2)/(s**2))))/(s*np.sqrt(2*np.pi))
    return p/9

def L(x_data,n):
    sigmas = np.linspace(1,10,n)
    l = np.ones(n)
    proba = []
    for k in x_data:
        proba.append(proba_sigma(sigmas,k))
        l =l*proba_sigma(sigmas,k)
    return sigmas,l,proba

sigmas,l, probas = L(datax,n_points)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(sigmas,l)
plt.subplot(1,2,2)
plt.hist(probas,density = True)
plt.savefig("sigma.png")