import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.dat")
plt.figure(figsize=(18,4))

nu = np.shape(data)[1]
nt = np.shape(data)[0]

u = np.linspace(0,1,nu)
t = np.linspace(0,6,nt)

plt.subplot(1,3,1)
plt.imshow(data, extent =[-1,1,1,0],aspect =2.0)
plt.xlabel("Posición")
plt.ylabel("$\psi$")
plt.colorbar()

#Editado y sacado de la solucion del profesor para el problema de difusión https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/29/plot.py
plt.subplot(1,3,2)
delta_t = 0.01
for i in range(nt):
        plt.plot(u, data[i,:],label="t={:.02f}".format(i*delta_t))
plt.legend(loc=1)
plt.xlabel("Posicion")
plt.ylabel("$\psi$")

plt.subplot(1,3,3)
plt.plot(t,data[:,99], color = "black")
plt.xlabel("Tiempo")
plt.ylabel("$\psi$")

plt.savefig("resultado.png")