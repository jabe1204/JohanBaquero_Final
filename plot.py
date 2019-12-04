import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.dat")
plt.figure(figsize=(18,4))

Nx = np.shape(data)[1]
Nt = np.shape(data)[0]

x = np.linspace(0,1,Nx)
t = np.linspace(0,6,Nt)

plt.subplot(1,3,1)
plt.imshow(data, extent =[-1,1,1,0],aspect =2.0)
plt.xlabel("Posición")
plt.ylabel("U")
plt.colorbar()

#Editado y sacado de la solucion del profesor para el problema de difusión https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/29/plot.py
plt.subplot(1,3,2)
delta_t = 0.01
for i in range(Nt):
    if(i%5==0):
        plt.plot(x, data[i,:],label="t={:.02f}".format(i*delta_t))
plt.legend(loc=1)
plt.xlabel("Posicion")
plt.ylabel("U")

plt.subplot(1,3,3)
plt.plot(t,data[:,99], color = "black")
plt.xlabel("Tiempo")
plt.ylabel("U")

plt.savefig("resultado.png")