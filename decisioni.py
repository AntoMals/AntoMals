# il costrutto if else
# operatori relazionali
# if innestati
# alternative multiple if elif
# booleani e operatori logici

# il costrutto if else

soglia = 27

if soglia > 25 :
    print("Accendo il condizionatore")
else :
    print("La temperatura è ancora accettabile")

# operatori relazionali

'''
> maggiore
< minore
>= maggiore uguale
<= minore uguale
== uguale
!= diverso

'''

nome1 = "marco"
nome2 = "luigi"

if nome1 != nome2 :
    print("I due nomi sono diversi")

# if innestati

a = 10
b = 10
c = 10

if a == b :
    if a == c :
        print("i tre numeri sono uguali")
    else :
        print("i tre numeri non sono uguali")
else :
    print("i tre numeri non sono uguali")

# alternative multiple if elif

richter  = 7.5

if richter >= 8.0 :
    print("Distrutta la quasi totalità delle strutture")
elif richter >= 7.0 :
    print("Molte strutture sono distrutte")
elif richter >= 6.0 :
    print("Molte strutture danneggiate, alcune distrutte")
elif richter >= 4.5 :
    print("danni alle strutture più deboli di bassa e media entità")
else :
    print("Nessun danno a strutture")


# booleani e operatori logici

test = True # valori ammessi True, False

if (test) :
    print("Il test è andato a buon fine")


# Operatore logico AND
'''
A       B       A and B
True    True    True
True    False   False
False   True    False
False   False   False

'''  

temp = 15

if temp > 0 and temp < 100 :
    print("Acqua allo stato liquido")

# Operatore logico OR
'''
A       B       A or B
True    True    True
True    False   True
False   True    True
False   False   False

'''

if temp <= 0 or temp >= 100 :
    print("L'acqua non è allo stato liquido")


# operatore logico Not
'''
A       not A
True    False
False   True

'''

if not test :
    print("Il test non è andato a buon fine")    




    

