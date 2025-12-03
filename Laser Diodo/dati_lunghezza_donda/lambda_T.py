import numpy as np 
import matplotlib.pyplot as plt

l_max = []
l_max1 = []
#fig1 = plt.figure("1")
for i in range(16, 43):
    l, I = np.loadtxt(f"/home/emiliano/Documenti/Lab. Materia/Laser Diodo/dati_lunghezza_donda/Sp_T{i}.txt", unpack= True, skiprows=17, encoding="latin-1", max_rows=651)
    I = I/np.max(I)
    x = np.argmax(I)
    l01 = l[x]
    mask = (l >= 778) & (l <= 788)
    l = l[mask]
    I = I[mask]
    l0 = np.sum(l*I)/np.sum(I)
    l_max.append(l0)
    l_max1.append(l01)
    #plt.errorbar(l, I, fmt=".-")

T = np.arange(16, 43)
print(l_max)
fig2 = plt.figure("2")
plt.errorbar(T, l_max, fmt="o", label="Medie")
plt.errorbar(T, l_max1, fmt="o", label="Max. Picchi")
plt.ylabel(r"$\lambda$ [nm]")
plt.xlabel("T [°C]")
plt.grid(which="both", ls="dashed", color="grey")
plt.legend()
plt.show()
