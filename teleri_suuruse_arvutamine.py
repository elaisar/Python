# Eliisa Raal

# Ülesanne 5. Teleri suurus

# Funktsiooni defineerimine
def teleri_diagonaal(kaugus):
    diagonaal = kaugus * 100 * 0.39 / 2.5 # Diagonaali pikkuse arvutamine

    return round(diagonaal) # Diagonaali pikkuse ümardamine täisarvuni

# Kasutajalt teleri kauguse küsimine
kaugus = int(input("Palun sisestage teleri kaugus diivanist (meetrites): "))
# Teleri diagonaali pikkuse väljastamine
print("Teleri diagonaal tollides on: ", teleri_diagonaal(kaugus))
