# Eliisa Raal ja Iris-Maria Rohelpuu

# Ülesanne 11

from turtle import*

# Funktsiooni defineerimine
def ruut_2(pikkus, värv):
    i = 0
    while (i < 4): # Teeb ruudu kasutates while tsüklit
        color(värv) # Kasutab ruudu joonestamisel kasutaja sisestatud värvi
        forward(pikkus) # Kasutab ruudu joonestamisel kasutaja sisestatud pikkust
        left(90)
        i = i + 1  
    up()
    left(180)
    forward(200)
    down()
        
    
# Kasutajalt ruudu külje pikkuse, värvi küsimine
pikkus = int(input("Palun sisestage ruudu külje pikkus: "))
värv = input("Palun sisestage ruudu värv: ")
arv = int(input("Palun sisestage ruutude arv: "))


# Ruudu joonistamine
ruut_2(pikkus, värv)



exitonclick()
