# Eliisa Raal

# Funktsiooni kala_kaal defineerimine
def kala_kaal(pikkus, indeks):
    kaal = pikkus**3 * indeks / 100 # Kala kaalu arvutamine

    return round(kaal) # Kala kaalu tagastamine täisarvuna

# Kalade pikkuste faili küsimine
fail = input("Sisestage failinimi: ")

# Kalade alammõõdu küsimine
alammoot = int(input("Sisestage püügi alammõõt: "))

# Fultoni tüsedusindeksi küsimine
tusedus = float(input("Sisestage Fultoni tüsedusindeks: "))

# Andmete lugemine järjendisse
kalade_pikkused = [] # Tühja järjendi loomine kalade pikkuste jaoks

f = open(fail, encoding="UTF-8") # Faili avamine, kodeering UTF-8

for rida in f:
    kalade_pikkused.append(int(rida)) # Kalade pikkuste lisamine järjendisse (täisarvud)

print(kalade_pikkused)

# Kalade kaalude väljastamine kasutades funktsiooni kala_kaal
for kala_pikkus in kalade_pikkused:
    
    if kala_pikkus < alammoot:
        print("Kala lasti vette tagasi.")
    else:
        kalade_kaal = kala_kaal(kala_pikkus, tusedus)
        print("Kala kaal on", kalade_kaal)

