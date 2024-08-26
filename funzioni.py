# introduzione alle funzioni
# definizione di funzione
# passaggio dei parametri
# valori di ritorno
# scope delle variabili
# funzioni ricorsive


# Esempio di funzione

def areaTriangolo(base,altezza) :
    area = (base*altezza)/2
    return area

triangolo1 = areaTriangolo(5,20)
triangolo2 = areaTriangolo(3,7)

print("L'area di trinagolo 1 è: ", triangolo1)
print("L'area di trinagolo 2 è: ", triangolo2)

# definizione di funzione

# intestazione
# def nomeFunzione(eventualiParametri) :

# corpo della funzione
# istruzioni
# return eventualiValoreDiRitorno


# nuovi esempi di funzioni

def pippo() :
    print("Ciao, sono pippo!")

pippo()


def calcoloCubo(lato) :
    cubo = lato*lato*lato
    print("Il volume del cubo è: ", cubo)


calcoloCubo(5)

def areaRombo() :
    base = int(input("Inserisci la base del rombo: "))
    altezza = int(input("Inserisci l'altezza del rombo: "))
    area = base*altezza
    return area

areaRombo1 = areaRombo()

# passaggio dei parametri

def scambiaVal(val1,val2) :
    app = val1
    val1 = val2
    val2 = app

valA = int(input("Inserisci un primo numero intero: ")) 
valB = int(input("Inserisci un secondo numero intero: ")) 

print(valA," ",valB)

scambiaVal(valA,valB)

print(valA," ",valB)

# i parametri vengono sempre passati riferimento
# la discriminante però riguarda la natura dell'argomento che può essere mutabile o immutabile
# oggetti come numeri e stringhe sono immutabili, per questo motivo non viene preservato il valore 


# soluzione

def scambiaVal1(val1,val2) :
    val1 ,val2 = val2, val1
    return val1, val2

valA = int(input("Inserisci un primo numero intero: ")) 
valB = int(input("Inserisci un secondo numero intero: ")) 

print(valA," ",valB)

valA,valB = scambiaVal1(valA,valB)

print(valA," ",valB)

# scope delle variabili

def main() :
    lato = 10
    volume = volumeCubo(lato)
    print(volume)

def volumeCubo(l=5) :
    return l ** 3

main() 

bilancio = 1000

def prelievo(valore) :
    global bilancio
    if bilancio >= valore :
        bilancio-=valore

# funzioni ricorsive


def main () :
    stampaQuadrato(4)

def stampaQuadrato(lato) :
    if lato < 1 : return
    stampaQuadrato(lato-1)
    print("[]"*lato)

main()



 







