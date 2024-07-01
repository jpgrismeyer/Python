from random import *
Num_entero=randint(1,100)
print(Num_entero)
Num_decimal=round(uniform(1,5),1)  #toma un fraccional entre 1 y 5 y lo redondea
print(Num_decimal)

porcentual=random()      #tira un valor entre 0 y 1, sirve para porcentajes
print(porcentual)

clubes=["Boca","Real Madrid", "Flamengo", "Bayern Munchen", "Manchester Utd", "Milan"]
eleccion=choice(clubes)
print(eleccion)

campeon=[1977,1978,2000,2001,2003,2007]
shuffle(campeon)
print(campeon)