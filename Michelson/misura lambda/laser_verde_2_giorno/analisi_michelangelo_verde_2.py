## Programma
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks as fp

lambda_list = []
num_picchi_list = []
heights = [0.30, 0.30, 0.34, 0.175, 0.175, 0.20, 0.20, 0.175, 0.175, 0.175]
spost = []

for index in range(1, 11):
    data = r"C:\Users\Gruppo 7\Desktop\G7_2025\dati_michelefiglio_verde_2giorno_1070rangepiezo_5minutiscansionemichelson\dati_verde2_{}.txt".format(index)

    x, y = np.loadtxt(data, unpack = True, skiprows = 0)

    findpeaks = fp(y, height = heights[index-1], distance = 5)

    # plt.figure()
    # plt.xlabel("Tempo [u.a.]")
    # plt.ylabel("Ampiezza [u.a.]")
    # plt.errorbar(x, y, fmt = "-.")
    # plt.show()

    num_picchi = len(findpeaks[0])
    # print("Numero di picchi: {}".format(num_picchi))

    if index in [1, 2, 3, 4]:
        lambd = 2 * 1.000294 * 60e-6 / (num_picchi)
    elif index in [5, 8, 9, 10]:
        lambd = 2 * 1.000294 * 70e-6 / (num_picchi)
    elif index in [6, 7]:
        lambd = 2 * 1.000294 * 20e-6 / (num_picchi)
    lambda_list.append(lambd)
    num_picchi_list.append(num_picchi)

    spost.append(round((532e-9 * num_picchi / (2 * 1.000294))*1e6, 2))

    # print("{} nm".format(lambd*1e9))

lambda_tot = np.mean(lambda_list)
sigma_lambda_tot = np.std(lambda_list, ddof = 1)

print("Numero di picchi")
print(num_picchi_list)
print("\n")
print("Lunghezza d'onda stimata: ({} +/- {}) nm".format(round(lambda_tot*1e9, 2), round(sigma_lambda_tot*1e9, 2)))
print("Spostamenti")
print(spost)

## Cambia punti in virgole
import os
dir = r"C:\Users\Gruppo 7\Desktop\G7_2025\dati_michelefiglio_verde_2giorno_1070rangepiezo_5minutiscansionemichelson\\"

for file in os.listdir(dir):
    if ".lvm" in file:
        with open(dir + file, "r") as f:
            text = f.read()
            text = text.replace(",", ".")
            with open(dir + file[:-4] + ".txt", "w") as p:
                p.write(text)
        os.remove(dir + file)
