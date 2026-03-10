import numpy as np
from matplotlib import pyplot as plt
#
num_picchi_0 = np.array([11, 27, 46, 68, 90, 81, 67, 51, 30, 8])
V_fin_0 = np.array([20 ,40, 60, 80, 100, 80, 60, 40, 20, 0])

num_picchi_1 = np.array([10, 21, 39, 60, 81, 71,  58, 42, 22,  0])
V_fin_1 = np.array([20.52, 40.37, 60.16, 80.23, 100.52, 80.18, 59.9, 40.12, 20.14, 1.15])

num_picchi_2 = np.array([10, 25,  43, 60, 80, 70, 57, 40, 20, -1])
V_fin_2 = np.array([20, 40.41, 60.17, 80.3, 100.12, 79.96, 60.47, 40.07, 20.05, 1.15])

spost0 = 633e-9 * num_picchi_0 / (2 * 1.000294)*1e6
spost1 = 633e-9 * num_picchi_1 / (2 * 1.000294)*1e6
spost2 = 633e-9 * num_picchi_2 / (2 * 1.000294)*1e6

plt.errorbar(V_fin_0, spost0, fmt='.-')
plt.errorbar(V_fin_1, spost1, fmt='.-')
plt.errorbar(V_fin_2, spost2, fmt='.-')
plt.xlabel('Voltaggio finale [V]')
plt.ylabel('Spostamento [\mu m]')

plt.show()

