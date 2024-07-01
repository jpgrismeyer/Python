lista= ['a', 'b', 'c', 'd', 'e']
for letra in lista:
    print("Letra: "+ letra) #el iterador i se define y se inicia automaticamente en 0 (letra en este caso)

lista2=["Juan", "PEpe", "Liam"]
for nombre in lista2:
    if nombre.startswith('L'):
        print("Nombres que empiezan con L: "+nombre)
    else:
        print("Nombres que no: "+ nombre)

numeros=[1,2,3,4,5]
valor=0
for numero in numeros:
    valor= valor + numero
    print(valor)


for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)