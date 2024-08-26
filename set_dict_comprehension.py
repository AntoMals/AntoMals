# Esempio di set comprension

stringa = "corso python premium"
vocali_uniche = {i for i in stringa if i in 'aeiou'}
print(vocali_uniche)

# Esempio di dict comprension

radici_quadrate = {i: i*i for i in range(5)}
print(radici_quadrate)

a = [3,6,8]
test = {i: 5 for i in a}
print(test)

# se utilizzi liste set e dizionari per calcoli transitori e' molto più utilie utilizzare generatori. Esempio:

s = sum([i*i for i in range(1000)])
print(s)

import sys
print(sys.getsizeof([i*i for i in range(1000)]))

# con generatore

g = sum((i*i for i in range(1000)))
print(g)

print(sys.getsizeof((i*i for i in range(1000))))


# considerazioni sulle prestazioni. Esempio: 

from timeit import default_timer as timer #importo la libreria timeit per gestire un timer

# avvio un timer con una list comprehension
start = timer()
a = [i*i for i in range(1_000_000)]
end = timer()
print(end-start)


# avvio un secondo timer con un classico for
start = timer()
a = []
for i in range(1_000_000):
    a.append(i*i)
end = timer()
print(end-start)