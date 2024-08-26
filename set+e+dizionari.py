# set
# dizionari

# set / insiemi -  struttura dati mutabile, i valori non sono indicizzati e sono univoci

attrezzi = { "martello", "cacciavite", "pinza"}

attezzi2 = set() # creazione di un set vuoto

valori = (1,7,9,5) # tupla

valori_set = set(valori) # casting da tupla a set

# operazioni elementari con i set

num_attrezzi = len(attrezzi)

if "pinza" in attrezzi :
    print("La pinza è presente negli attrezzi")
else :
    print("La pinza non è presente negli attrezzi")


for attrezzo in attrezzi : # l'ordine non è garantito
    print(attrezzo)

# metodi per inserire o rimuovere elementi

attrezzi.add("scalpello")

attrezzi.discard("chiave_inglese")

attrezzi.remove("scalpello")

valori_set.clear()

# subset

attrezzi_mario = {"martello","pinza"}

if attrezzi_mario.issubset(attrezzi) :
    print("tutti gli attrezzi di mario sono presenti anche negli attrezzi generici")

# unione, intersezione e differenza

italia = {"rosso","bianco","verde"}

inghilterra = {"rosso", "blu", "bianco"}

unione = italia.union(inghilterra)

print(unione)

intersezione = italia.intersection(inghilterra)

print(intersezione)

differenza_ita = italia.difference(inghilterra)

print(differenza_ita)




# dizionari

auto = {
    "marca"   : "Fiat",
    "modello" : "Panda",
    "elettrica" : False,
    "anno"    : 2021, 
    "cilindrate" : [900,1000,12000]   
}

# operazioni con i dizionari

# accedere ad un elemento del dizionario tramite la chiave

marca = auto["marca"]
marca = auto.get("marca")

# recuperare tutte le chiavi o i valori di un dizionario in una lista

chiavi = auto.keys()
dati = auto.values()

# convertire un dizionario in una tupla annidata

tuple = auto.items()

# verificare la presenza di una chiave

if "modello" in auto:
    print("chiave presente")

# cambiare, aggiungere o aggiornare valori

auto["anno"] = 2000
auto.update({"anno": 2000}) 

# rimuovere valori

auto.pop("anno")
del auto["anno"]

auto.popitem() # rimuovo l'ultima coppia chiave valore inserita

# del auto  elimino il dizionario
auto.clear() # svuoto il dizionario

# percorrere un dizionario con un ciclo

for k in auto:
    print(k) # stampo le chiavi
    print(auto[k]) # stampo i valori corrispondenti alle chiavi

for val in auto.values():
    print(val)

for k,val in auto.items():
    print(k.val)


# copiare dizionari

auto2 = auto.copy()
auto3 = dict(auto)





