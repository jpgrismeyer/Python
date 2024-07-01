def chequear_3_cifras(lista):
    lista_filtrada=[]
    for n in lista:
        if n in range(100,1000):
            lista_filtrada.append(n)
        else:
            pass
    return lista_filtrada
Set=[4,7,42.54,1002]
set2=[105, 222, 3]
print(chequear_3_cifras(set2))
print(chequear_3_cifras(Set))

def suma_menores(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n in range(0,1000):
            suma+=n
    return suma
lista_numeros=[1,2,3,4,5,20000]
print(suma_menores(lista_numeros))