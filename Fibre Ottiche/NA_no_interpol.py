import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

data = np.loadtxt('Apertura_numerica_1.txt', skiprows=2)
gradi = data[:, 0]
dg = data[:, 1]#/np.sqrt(12)
P = data[:, 2]
dP = data[:, 3]

gradi = gradi - 43
I = P/1 # [W/cm^2]

I_max = np.max(I)
I_5 = 0.05 * I_max
print(I_5)

mask = (I > 3.5e-7) & (I < 6e-7)
gradi_int = gradi[mask]
print(gradi_int)
gradi_5 = np.mean(abs(gradi_int))
dg_int = dg[mask]
print(dg_int)
dg_5 = np.sqrt(np.sum(dg_int**2))

print(f'Gradi corrispondenti a I_5%: {gradi_5} +/- {dg_5}')

n_a= 1.00027653*np.sin(np.radians(gradi_5))
dn_a = 1.00027653 * np.abs(np.cos(np.radians(gradi_5))) * np.radians((dg_5))
print(f'Apertura numerica: {n_a} +/- {dn_a}')
x = np.linspace(-18.94, 18.94, 100)
I_5 = np.full_like(x, I_5)
fig = plt.figure()
plt.errorbar(gradi, I, dP, dg, fmt='.', label='Dati')
plt.plot(x, I_5, color="red")
plt.xlabel('Gradi')
plt.ylabel('Intensità')
plt.title('Intensità in funzione dei gradi')
plt.legend()
plt.grid()
plt.show()