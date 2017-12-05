# Eliisa Raal

# Funktsiooni defineerimine
def välgu_kaugus(ajavahemik):
    kaugus = ajavahemik * 330 / 1000 # Välgulöögi kauguse arvutamine
    
    return(round(kaugus)) # Välgulöögi kauguse ümardamine täisarvuni ja tagastamine

# Välgu kauguse väljastamine
ajavahemik = int(input("Mitu sekundit kulus välgu nägemisest müristamise kuulmiseni? ")) # Kasutajalt ajavahemiku küsimine

print("Välgulöögi kaugus kilomeetrites: " , välgu_kaugus(ajavahemik)) # Välgulöögi kauguse väljastamine