import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

directory = r"C:\Users\Gruppo 9\Desktop\dati_nuovi.txt"
data = np.loadtxt(directory, unpack = True)

# y1 = 50 * np.array(data[0])
# x1 = data[1]

y = 50 * np.array(data[0])
x = data[1]

def radice(t, ampiezza, c, potenza):
    return ampiezza * (t**potenza) + c

figure = plt.figure("Grafico")
plt.errorbar(x, y, fmt = ".", label = "Dati")
plt.errorbar(x1, y1, fmt = ".", label = "Dati")

init = (100, -500, 0.5)
pars, covm = curve_fit(radice, x, y, p0 = init, maxfev = int(1e6))

xx = np.linspace(min(x), max(x), 500)
# plt.plot(xx, radice(xx, *init), color = "tab:orange")
plt.plot(xx, radice(xx, *pars), label = "Fit")

plt.xlabel("Tempo [s]")
plt.ylabel("Posizione [u.a.]")
plt.minorticks_on()
plt.title("Grafico con fit")

plt.legend()
plt.show()

##
root_directory = r"C:\Users\Gruppo 9\Desktop\\"

new_array = []

for line in open(root_directory + "dati.txt").readlines():
    line = line.replace(" - ", "\t")
    line = line.replace(",", ".")
    new_array.append(line)

with open(root_directory + "dati_elaborati_nuovo_master_3.txt", "w") as file:
    for value in new_array:
        file.write(value)