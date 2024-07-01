lista=[0,23,"MJ","bokita"]     #las listas pueden tener distintos tipos de datos
lista2=[1,43,"xd"]
print(lista+lista2)    #concateno las listas

resultado=lista2[:2]            #guardo desde el 1er elemento hasta el 2 no inclusive
print(resultado)

print(lista)
lista[2]="KB"              #cambio el valor de la posicion 2
print(lista)               #la lista cambio, no me tira error como los string

lista.append("juampa")              #agregué un elemento, es como concatenar pero con la lista base, sin declarar nueva variable
print(lista)
lista.pop()      #elimina un elemento. Asi elimina por defecto el ultimo
print(lista)
lista.pop(2)    #elimina el elemento en la poscion 2. lo puedo guardar en una variable
print(lista)
lista_numerica=[1,-2,19,5,48,-10]
lista_numerica.sort()   #ordena de menor a mayor. Opera en la lista original
print(lista_numerica)
lista_numerica.reverse()  #invierte el orden
print(lista_numerica)

#los metodos sort y reverse no devuelve nada