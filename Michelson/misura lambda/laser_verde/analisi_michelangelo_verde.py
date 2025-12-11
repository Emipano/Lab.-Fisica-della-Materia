## Programma
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks as fp
import inspect

root_path = inspect.getfile(lambda: None); root_path = root_path[:root_path.rfind("\\")] + "\\"

lambda_list = []
num_picchi_list = []
heights = [0.42, 0.4, 0.37, 0.34, 0.36, 0.35, 0.35]

indexes = [a for a in range(1, 7)] + ["20um"]

for index in indexes:
    data = root_path + r"dati_michelson_verde_{}.txt".format(index)
    x, y = np.loadtxt(data, unpack = True, skiprows = 1)

    if index == "20um":
        x = x[:520]
        y = y[:520]
        index = 7
    elif index == 5:
        x = x[83:]
        y = y[83:]

    findpeaks = fp(y, height = heights[index-1], distance = 5)

    # plt.figure()
    # plt.xlabel("Tempo [u.a.]")
    # plt.ylabel("Ampiezza [u.a.]")
    # plt.errorbar(x, y, fmt = "-.")
    # plt.show()

    num_picchi = len(findpeaks[0])
    # if index in [4, 6, 7]: # sistema il taglio dei dati non ragionevole
    #     num_picchi += 1
    # print("Numero di picchi: {}".format(num_picchi))

    if index != 7: # lunghezze diverse di acquisizione
        lambd = 2 * 1.000294 * 70e-6 / (num_picchi)
    else:
        lambd = 2 * 1.000294 * 20e-6 / (num_picchi)

    lambda_list.append(lambd)
    num_picchi_list.append(num_picchi)

    # print("{} nm".format(lambd*1e9))

lambda_tot = np.mean(lambda_list)
sigma_lambda_tot = np.std(lambda_list)

print("Numero di picchi")
print(num_picchi_list, "\n")
print("Lunghezza d'onda stimata: ({} +/- {}) nm".format(round(lambda_tot*1e9, 2), round(sigma_lambda_tot*1e9, 2)))
print("Lunghezza d'onda nominale: 532 nm")

## Cambia punti in virgole
import os
dir = r"C:\Users\Gruppo 7\Desktop\G7_2025\dati_michelefiglio_verde\\"

for file in os.listdir(dir):
    if ".lvm" in file:
        with open(dir + file, "r") as f:
            text = f.read()
            text = text.replace(",", ".")
            with open(dir + file[:-4] + ".txt", "w") as p:
                p.write(text)
        os.remove(dir + file)
