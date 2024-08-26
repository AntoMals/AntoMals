# definizione di lista
# primi esempi
# operazioni con le liste
# liste con le funzioni
# tuple
# tabelle



# struttura dati sequenziale ordinata dinamica contraddistinta da un indice 
# mutabile

valori = [33, "pippo", 90, 17.5, "pluto"]

# dimensione 5 indici da 0 a 4

# accedere agli elementi di una lista

print(valori[1])

valori[1]=80

print(valori[1])

# creazione di una lista vuota

lista = []


# scansione di una lista

for i in range(5) :
    print(i,": ",valori[i])


for i in range(len(valori)) :
    print(i,": ",valori[i])


for elemento in valori :
    print(elemento)


# riferimento a lista

miei_valori = valori

miei_valori[4] = "ciao"
print(*valori, sep=' ')
print(*miei_valori, sep=' ')

# copiare una lista

miei_valori = valori.copy()

miei_valori[4] = "hello"
print(*valori, sep=' ')
print(*miei_valori, sep=' ')


# operazioni con le liste

# append

valori.append(99)
valori.append("nome")
print(*valori, sep=' ')

# insert

valori.insert(1, "mario")
print(*valori, sep=' ')

# ricerca elementi

nomi = ["mario", "silvia", "luigi", "laura", "luigi"]

if "mario" in nomi :
    print("il nome è presente")

n = nomi.index("luigi")
n2 = nomi.index("luigi", n + 1)


if "mario" in nomi :
    n = nomi.index("mario")
else :
    n = -1

# rimuovere valori dalla lista

nomi.pop() #rimuove l'ultimo elemento
nomi.pop(2) #posso specificare un esatto indice

# nomi.remove("luigi") #rimozione per valore ma se non presente genera un'eccezione

# soluzione
valore = "luigi"
if valore in nomi :
    nomi.remove(valore)

# concatenazione e replica di liste

nomi2 = ["sara", "silvia"]

nomi_tot = nomi + nomi2 #ho l'unione delle due liste

print(nomi_tot)

nomi_ripetuti = nomi2 * 5 #nomi due viene ripetuto 5 volte

print(nomi_ripetuti)

val_ripetuti = [0] * 10 # creo 10 elementi inizializzati tutti a 0

print(val_ripetuti)



# test di uguaglianza, somma, massimo, minimo e ordinamento

if nomi == nomi2 :
    print("le liste sono uguali")

sequenza = [1,2,3,4,5,6,7]

somma = sum(sequenza)
val_massimo = max(sequenza)
val_minimo = min(sequenza)

sequenza.sort(reverse = True)

# Slices

# esempio temperature campionate nei 12 mesi di un anno
temperature = [18, 21, 24, 28, 33, 39, 40, 39, 36, 30, 22, 18]

# destra: compreso partendo da 0 sinistra escluso 
terzo_trimstre = temperature[6:9]

print(*terzo_trimstre, sep=' ')

primo_semestre = temperature[:6]

print(*primo_semestre, sep=' ')

secondo_semestre = temperature[6:]

print(*secondo_semestre, sep=' ')


# passare liste alle funzioni

def sum(tmp) :
    total = 0
    for element in tmp :
        total = total + element
    return total

somma_temp = sum(temperature)

# essendo la lista mutabile il contenuto modificato dentro la funzione avrà effetto anche fuori
def multi(tmp, factor) :
    for i in range(len(tmp)) :
        tmp[i] = tmp[i] * factor   

multi(temperature,3)

# TUPLE

# sono simili alle liste ma con la differenza che essendo immutabili una volta inizializzate non possono più essere modificate

esempio_tupla = (5,10,"pippo",17.78,"pluto")

# possiamo agire in lettura ma non possiamo modificare il contenuto

# possiamo convertire una tupla in una lista 

esempio_lista = list(esempio_tupla)


# tabelle

# un modo per implementare le tabelle in paython è quello di creare liste bidimensionali

# esempi

tabella = [
    [15,"ciao",17.5],
    ["mondo",-6,99],
    [3.76,4,"pippo"]
]

print(*tabella, sep=' ')

