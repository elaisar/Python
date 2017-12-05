# Eliisa Raal ja Iris-Maria Rohelpuu

# Ülesanne 10

from turtle import*

# Funktsiooni defineerimine
def ruut_2(pikkus, värv):
    i = 0
    while (i < 4): # Teeb ruudu kasutates while tsüklit
        color(värv) # Kasutab ruudu joonestamisel kasutaja sisestatud värvi
        forward(pikkus) # Kasutab ruudu joonestamisel kasutaja sisestatud pikkust
        left(90)
        i = i + 1  

# Kasutajalt ruudu külje pikkuse ja värvi küsimine
pikkus = int(input("Palun sisestage ruudu külje pikkus: "))
värv = input("Palun sisestage ruudu värv: ")

# Ruudu joonistamine
ruut_2(pikkus, värv)

exitonclick()
