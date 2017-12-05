#IrisMariaRohelpuu  #EliisaRaal
#Kirjuta funktsioon nimega järjendi_summa, mis leiab argumendina saadud järjendi elementide summa ning tagastab selle. 

arvud1 = [2, 6, 8, 3]
#def funktsioon
def järjendi_summa(arvud):
    summa = 0
    for el in arvud:         #el on rida failist
        arv = int(el)        #rea teisendamine täisarvuks, salvestame muutujasse arv
        summa += arv
     

    return summa   #tagastame järjendi

    #faili nime salvestamine muutujasse

andmed = järjendi_summa(arvud1) #funktsiooni väärtuse salvestamine muutujasse

print(andmed)   #tulemuse väljastamine