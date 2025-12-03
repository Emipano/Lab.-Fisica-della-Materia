import numpy as np
import matplotlib.pyplot as plt 

phi_o, I_o, dI_o = np.loadtxt("/home/emiliano/Documenti/Lab. Materia/Laser Diodo/Apertura angolare/orizzontale_1.txt", unpack=True)
phi_o-=270
phi_v, I_v, dI_v = np.loadtxt("/home/emiliano/Documenti/Lab. Materia/Laser Diodo/Apertura angolare/verticale_1.txt", unpack=True)
phi_v-=270



fig = plt.figure()
plt.errorbar(phi_o, I_o, yerr=dI_o, label="Orizzontale", fmt=".-")
plt.errorbar(phi_v, I_v, yerr=dI_v, label="Verticale", fmt=".-")
plt.grid(which="both", ls="dashed", color="gray")
plt.title("Apertura Angolare")
plt.xlabel(r"$\varphi$ [°]")
plt.ylabel("I [$\mu$A]")
plt.legend()
plt.show()


