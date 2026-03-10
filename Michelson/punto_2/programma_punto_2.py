## Programma
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks as fp

# lambda_list = []
# num_picchi_list = s[]
# heights = []
# spost = []

data = r"/Users/valeriofrancopecchia/Desktop/Fisica/LabMateriaGit/Michelson/punto_2/punto2_acq1.txt"

x, y = np.loadtxt(data, unpack = True, skiprows = 1)

# findpeaks = fp(y, height = heights[index-1], distance = 5)

plt.figure()
plt.xlabel("Tempo [u.a.]")
plt.ylabel("Ampiezza [u.a.]")
plt.errorbar(x, y, fmt = "-.")
plt.show()

# num_picchi = len(findpeaks[0])
# if index in [4, 6, 7]: # sistema il taglio dei dati non ragionevole
#     num_picchi += 1
# # print("Numero di picchi: {}".format(num_picchi))
#
# lambd = 2 * 1.000294 * 70e-6 / (num_picchi)
# lambda_list.append(lambd)
# num_picchi_list.append(num_picchi)
#
# spost.append(round((633e-9 * num_picchi / (2 * 1.000294))*1e6, 2))
#
# # print("{} nm".format(lambd*1e9))
#
# lambda_tot = np.mean(lambda_list)
# sigma_lambda_tot = np.std(lambda_list)
#
# print("Numero di picchi")
# print(num_picchi_list)
# print("\n")
# print("Lunghezza d'onda stimata: ({} +/- {}) nm".format(round(lambda_tot*1e9, 2), round(sigma_lambda_tot*1e9, 2)))
# print("Spostamenti")
# print(spost)
# print("Media sposatmenti")
# print(round(np.mean(spost), 3))

## Cambia punti in virgole
for index in range(1):
    data = r"C:\Users\Gruppo 7\Desktop\G7_2025\punto_2\punto2_acq2.lvm"
    with open(data, "r") as f:
        text = f.read()
        text = text.replace(",", ".")
        with open(data, "w") as p:
            p.write(text)