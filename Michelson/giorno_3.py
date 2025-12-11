import numpy as np

ref_index_list = []
num_picchi = [41, 42, 42, 42, 42, 43, 43, 43, 43, 44, 42]

for picchi in num_picchi:
    ref_index_list.append(633e-9 * picchi / (2 * 5e-2) + 1)
# inc camera: 1/20 mm

# exp_index = 1.000271373 # a 633 nm
exp_index = 1.000270611 # incertezza su 11, p atmosferica, 20.8 °C, 633 nm

ref_index_tot = np.mean(ref_index_list)
sigma_ref_index_tot = np.std(ref_index_list)

print("Indice di rifrazione stimato: {} +/- {:f}".format(ref_index_tot, sigma_ref_index_tot))
print("Indice di rifrazione aspettato: {}".format(exp_index))
print("Distanza in barre d'errore: {}".format(abs(exp_index - ref_index_tot)/sigma_ref_index_tot))

# dovremmo vedere tra 43 e 44 picchi
# indice del vuoto che fa la camera col nostro conteggio di picchi:
index_vuoto_camera = exp_index - (633e-9 * np.mean(picchi) / (2 * 5e-2))
print("Indice del vuoto che fa la camera mediando i nostri conteggi dei picchi:\n{}".format(index_vuoto_camera))