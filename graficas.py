import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

datos=pd.read_csv("atenuacion.data", header=None)

x=np.array(datos[0])
xp=np.linspace(8.8,22.8,x.size)
y=np.array(datos[1])
errorx=np.array(datos[2])
errory=np.array(datos[3])

m=0.376265895953757
n=0.74692485549133

fig, ax=plt.subplots()

ax.axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
ax.set_xlabel("Frecuencia (MHz)", fontsize=15)
ax.set_ylabel("Atenuación (dB/m)", fontsize=15)

plt.errorbar(x,y,xerr=errorx, color='red',fmt='none', label='Datos experimentales')
plt.plot(xp,m*xp+n, label='Recta de regresión')

plt.legend()

plt.savefig("/home/alvaro/UNIVERSIDAD/recuarto/poe/pr1/desfase.pdf", dpi=96)

