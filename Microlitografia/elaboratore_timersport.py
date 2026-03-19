## Elaboratore dei risultati di TimerSport per farli leggere da Python
# A numpy.loadtxt() danno fastidio i trattini di TimerSport. Questo arnese li fa
# sostituire da delle tab (stringa "\t") e chiama il nuovo file "dati_nuovi.txt".
# Il file iniziale si deve chiamare "dati.txt". Chiamate le cose come le volete
# utilizzare.
# Per problemi o altro: loregugo03@gmail.com

root_directory = r"C:\Users\Gruppo 9\Desktop\\"

new_array = []

for line in open(root_directory + "dati.txt").readlines():
    line = line.replace(" - ", "\t")
    line = line.replace(",", ".")
    new_array.append(line)

with open(root_directory + "dati_nuovi.txt", "w") as file:
    for value in new_array:
        file.write(value)