import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

directory = r"C:\Users\loreg\Desktop\Laboratorio di fisica della materia e nanotecnologie\microlitografia\dati_elaborati_nuovo_master_1.txt"
data = np.loadtxt(directory, unpack = True)

y = np.array(data[0])
x = data[1]
# x = np.array(x - x[-1])

def radice(t, ampiezza, c, potenza, ritardo):
    return ampiezza * (abs(t - ritardo)**potenza) + c

figure = plt.figure("Master nuovo 1", figsize = (7.5, 5.625))

ax1 = figure.add_axes((0.15, 0.3, 0.8, 0.6))
plt.errorbar(x, y, marker = ".", linestyle = "", label = "Dati")

init = (10, -50, 0.5, 50)
pars, covm = curve_fit(radice, x, y, p0 = init)

xx = np.linspace(min(x), max(x), 500)
# plt.plot(xx, radice(xx, *init), color = "tab:orange")
plt.plot(xx, radice(xx, *pars), label = "Fit")
# plt.plot(xx, radice(xx, *init), label = "Stima dei parametri\niniziali")

# plt.xlabel("Tempo [s]")
plt.ylabel("Posizione [u.a.]")
plt.minorticks_on()
plt.title("Grafico della posizione del fludio\nin funzione del tempo con fit")
plt.legend()

props = dict(boxstyle = "round", facecolor = "wheat", alpha = 0.5)
testo = r"Funzione di fit: $A|t - t_{rit}|^{potenza} + C$" + "\n" + r"potenza = {0:.2g}".format(pars[2])
ax1.text(0.03, 0.95, testo, transform = ax1.transAxes, fontsize = 10, verticalalignment = "top", bbox = props)
ax1.legend(loc = "best")

figure.add_axes((0.15, 0.1, 0.8, 0.15))

res = y - radice(x, *pars)

plt.errorbar(x, res, marker = ".", linestyle = "", label = "Residui")

plt.xlabel("Tempo [s]")
plt.ylabel("Residui [u.a.]")
plt.minorticks_on()

plt.legend()
plt.show()

##
# root_directory = r"C:\Users\Gruppo 9\Desktop\\"
#
# new_array = []
#
# for line in open(root_directory + "dati.txt").readlines():
#     line = line.replace(" - ", "\t")
#     line = line.replace(",", ".")
#     new_array.append(line)
#
# with open(root_directory + "dati_elaborati_nuovo_master_3.txt", "w") as file:
#     for value in new_array:
#         file.write(value)
