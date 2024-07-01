mi_set=set({1,'b', 45})
print(type(mi_set))
print(mi_set)
set2={1,2,3,4}
print(type(set2))
lista=[1,2,3,4]
print(type(lista))

set3={1,2,3,3,3,5,5,1,2,4,11}
print(set3)          #elimina los valores repetidos
set4={1,2,3,(1,2),(1,2,3),4,5,6,7} #puede contener tuplas y de esa manera repetir datos. no puede listas ni dic
print(set4)

#no tiene orden dentro, no se puede imprimir un lugar de posicion
s1=set2.union(set3)
print(s1)
s1.add(7)          #agrego un 7
print(s1)
s1.remove(7)          #saco el 7
print(s1)
s1.discard(2)          #
print(s1)

sorteo=s1.pop()          #
print(sorteo)
sorteo=s1.pop()          #
print(sorteo)