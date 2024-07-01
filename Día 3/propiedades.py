nombre="Juampa"
print(id(nombre))
nombre="juampa"
print(id(nombre)) #al reasignarle valor al string, este cambia de direccion, y el string original no se modifica

print(nombre + nombre)
print(nombre * 10) #se multiplica :O

poema_de_vegeta="""My life fell like dew
Disappears like dew
All of this world
Is dream after dream
"""
print(poema_de_vegeta)

print("dew" in poema_de_vegeta)  #Imprime si esta la palabra en el string (V o F)

print(len(poema_de_vegeta))    #imprime la longitud del string