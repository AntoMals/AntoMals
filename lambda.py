# lambda argomenti: espressione

cubo = lambda x: x*x*x
print(cubo(5))

# esempio con argomenti multipli

area_triangolo = lambda b,a: (b*a)/2
print(area_triangolo(5,10))

# esempio di funzione lambda come parametro di un'altra funzione

puntiCartesiani = [(2,1), (4,2), (10,3), (3,9)]
puntiCartesiani_ordinari = sorted(puntiCartesiani, key=lambda x: x[0] + x[1])
print(puntiCartesiani_ordinari)

# esempio di funzione lambda con funzione map

# map (funzione, sequenza), esempio:

a = [1,2,3,4,5]
b = map(lambda x: x*x, a)
print(list(b))

# esempio di funzione lambda con funzione filter

# filter (funzione, sequenza), esempio:
c = filter(lambda x: x%2==0, a)
print(list(c))

# esempio di funzione lambda con funzione reduce

# reduce (funzione, sequenza), esempio:
from functools import reduce
prodotto_a = reduce(lambda x,y: x*y, a)
print(prodotto_a)

