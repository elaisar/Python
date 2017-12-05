# Eliisa Raal

# Tühja järjendi loomine
arvud = []

# While tsükkel
while True:
    hinded = input("Palun sisestage oma hinded (kui rohkem sisestada ei soovi, kirjutage stop): ") # Kasutajasisestus
    if hinded == "stop":
        break
    arvud.append(int(hinded)) # Kasutaja sisestatud hinnete lisamine järjendisse

keskmine = round(sum(arvud) / len(arvud), 2) # Keskmise hinde arvutamine ja ümardamine
print("Teie keskmine hinne on: ", keskmine) # Kasutajale keskmise hinde väljastamine

