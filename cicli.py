# introduzione ai cicli
# il ciclo FOR
# il ciclo WHILE
# cicli annidati

# il ciclo FOR

# Esempio 01

for i in range(1, 10) :
    print(i)

for i in range(1, 10, 2) :
    print(i)

for i in range(10) :
    print(i," ciao")

# Esempio 02

Name = "Mario Rossi"
for letter in Name :
    print(letter)

# il ciclo WHILE

# Esempio 01

'''
saldo = 1000.0
while (saldo>0) :
    prelievo = float(input("Quanto vuoi prelevare: "))
    if (prelievo>saldo) :
        print("valore massimo prelevabile: ", saldo)
    else :   
        saldo=saldo-prelievo
'''        

# Esempio 02

'''
somma = 0
while True :
    val = int(input("Valore da sommare: "))
    if (val==0) :
        break
    else :   
        somma+=val

print("Somma finale: ",somma)
'''

# cicli annidati

# Inizializzazione delle costanti.
NMAX = 4
XMAX = 10

# Stampa intestazione.
for n in range(1, NMAX + 1) :
    print("%10d" % n, end="")

print()
for n in range(1, NMAX + 1) :
    print("%10s" % "x ", end="")

print("\n", " ", "-" * 40)

# Stampa corpo della tabella.
for x in range(1, XMAX + 1) :
    for n in range(1, NMAX + 1) :
        print("%10.0f" % x ** n, end="")
    print()

# https://docs.python.org/3/library/stdtypes.html#old-string-formatting







