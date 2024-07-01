respuesta='s'

while respuesta=='s' or respuesta=='S':
    respuesta=input(("Desea continuar?(s/n): "))
else: print("gracias")

while respuesta=='x':
    pass #no se lo que voy a hacer en el bloque

for letra in "juampa":
    if letra=='a':
        break
    print(letra)

for letra in "juampa":
    if letra=='a':
        continue
    print(letra)