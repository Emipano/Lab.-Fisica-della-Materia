import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("dati_rayleigh.txt", unpack = True)
lambd = data[0]
loss = data[1]
dl = data[2]

def rayleigh(x, A):
    y = A / (x**4)
    return y

init = 0.85e12
popt, pcov = curve_fit(rayleigh, lambd, loss, init, sigma=dl, absolute_sigma=False)
A_hat = popt 
dA = np.sqrt(pcov)
print(A_hat)

x = np.linspace(min(lambd), max(lambd), 10000)

fig = plt.figure()
plt.errorbar(lambd, loss, yerr= dl, fmt="o")
plt.plot(x, rayleigh(x, A_hat))
#plt.plot(x, rayleigh(x, init))
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel('Perdite [dB/km]')
plt.title('Perdite')
plt.show()