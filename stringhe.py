# Definizione di stringa
# Inizializzazione delle stringhe
# Conteggio, concatenazione e ripetizione di stringhe
# Conversione da numeri a stringhe
# Stringhe caratteri e slicing
# Alcuni metodi della classe String
# Caratteri di escape

# Inizializzazione delle stringhe

stringa1 = "Ciao mondo"
stringa2 = 'Mario Rossi'

# Conteggio, concatenazione e ripetizione di stringhe

lunghezza = len(stringa1)
print(lunghezza)

stringa = stringa1 + stringa2
print(stringa)

stringa = stringa1 + " " + stringa2
print(stringa)

messaggio = "Echo..."
print(messaggio * 5)

# Conversione da numeri a stringhe

print("la lunghezza della stringa1 e: " + str(lunghezza))

# Stringhe caratteri e slicing

nome = "Luisa"
iniziale = nome[0]
finale = nome[4]

finale2 = nome[len(nome)-1]

print(iniziale)
print(finale)
print(finale2)

print(stringa1[2:5]) # esclusi
print(stringa1[:5]) # escluso 
print(stringa1[2:]) # escluso

# Alcuni metodi della classe String

stringa2 = 'Mario Rossi'

Maiuscolo = stringa2.upper()
print(Maiuscolo)

print(stringa2.lower())

nomeNuovo = stringa2.replace("Mario", "Luigi")
print(nomeNuovo)

# https://www.w3schools.com/python/python_ref_string.asp

# caratteri di escape

print("Si alzò un coro \"campioni\" ") 

print("Path C:\\home\\user\\mike")

print("*\n**\n***")

# https://docs.python.org/3/reference/lexical_analysis.html#strings



