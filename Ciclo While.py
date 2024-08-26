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


somma = 0
while True :
    val = int(input("Valore da sommare: "))
    if (val==0) :
        break
    else :   
        somma+=val

print("Somma finale: ",somma)
