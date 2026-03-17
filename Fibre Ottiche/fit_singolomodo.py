import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt(r"C:\Users\loreg\Desktop\Laboratorio di fisica della materia e nanotecnologie\fibre_ottiche\fibra_singolo_modo.txt", unpack = True, skiprows = 2)
gradi = data[0]
dg = data[1]
P = data[2] * 1e9
dP = data[3] * 1e9
dg = dg/np.sqrt(12)

I = P/1
dI = dP

# Fit gaussiano

def func(gradi, a, mu, sigma):
    return a * np.exp(-(gradi - mu)**2 / (2 * sigma**2))

da, dmu, dsigma = 0, 0, 0

init = [3.7, 41.5, 1]
a = init[0]
mu = init[1]
sigma = init[2]

for i in range(5):
    d_tot = np.sqrt((a * np.exp(-(gradi - mu)**2 / (2 * sigma**2)) * (gradi - mu) / sigma**2 * dg)**2 + dI**2)
    pars, covm = curve_fit(func, gradi, I, sigma = d_tot,  p0 = init, absolute_sigma = True)
    a, mu, sigma = pars
    da, dmu, dsigma = np.sqrt(np.diag(covm))

print(f"Parametri del fit: a = {a:.3g}, mu = {mu:.3g}, sigma = {sigma:.3g}")
print(f"Incertezze del fit: da = {da:.3g}, dmu = {dmu:.3g}, dsigma = {dsigma:.3g}")

residui = P - func(gradi, *pars)

x  = np.linspace(np.min(gradi), np.max(gradi), 500)
figure = plt.figure("Grafico con fit", figsize = (7.5, 5.625))

figure.add_axes((0.15, 0.3, 0.8, 0.6))

plt.errorbar(gradi, I, d_tot, fmt = ".", label = "Dati")
plt.plot(x, func(x, *pars), label = "Fit gaussiano", color = "red")
# plt.xlabel("Gradi [°]")
plt.ylabel("Intensità [nW/cm^2]")

plt.minorticks_on()
plt.title("Intensità rilevata in funzione dei gradi")
plt.legend()

figure.add_axes((0.15, 0.1, 0.8, 0.15))
plt.errorbar(gradi, residui, d_tot, fmt = ".")
plt.xlabel("Gradi [°]")
plt.ylabel("Residui [nW/cm^2]")
plt.minorticks_on()

Chi2 = ((residui/d_tot)**2).sum()
gdl = len(gradi) - len(pars)

print("Chi2: {}".format(round(Chi2)))
print("Chi2 atteso = {} +/- {}".format(round(gdl), round((2 * gdl)**0.5)))

plt.show()