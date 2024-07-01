dic={'c1':23,'c2':[1,2,3],'dic2':{'d1':24,'d2':14}}

print(dic['c1'])
print(dic['c2'][2])
print(dic['dic2']['d2'])

dic1={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic1['c2'][1].upper())         #tomo la e y la paso a mayuscula y la imprimo


dic3={1:'a', 'x': 'x', 4:'b'}

print(dic3)
dic3[4]='B'                      #cambie la clave 4, no el lugar de memoria o elemento 4
print(dic3)                      #puedo cambiar un diccionario sin problemas

print(dic.keys())         #imprime las claves dentro del dic
print(dic.values())       #imprime los valores del dic
print(dic.items())        #imprime todo lo que hay en el dic