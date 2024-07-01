#se pide al usuario ingresar un texto
print("Bienvenido al analizador de texto")
texto=input("Ingrese el texto a analizar:")
#print(texto)
#se pide que el usuario escoja 3 letras para hacer cinco analisis
print("Primeramente, se le pedirá que ingrese 3 letras para análisis")
letras=["a","b","c"]
##print(letras)
#1 cuantas veces aparece cada una de las letras elegidas?
letras[0]=input("Escoja las letras que quiere analizar:\n1-")
letras[1]=input("2-")
letras[2]=input("3-")

texto1=texto.lower()

letras[0]=letras[0].lower()
letras[1]=letras[1].lower()
letras[2]=letras[2].lower()
#print(letras)
#print(texto1)

n1=str(texto1.count(letras[0]))
n2=str(texto1.count(letras[1]))
n3=str(texto1.count(letras[2]))


print("1- La letra "+letras[0]+" aparece "+n1+" veces")
print("La letra "+letras[1]+" aparece "+n2+" veces")
print("La letra "+letras[2]+" aparece "+n3+" veces")


#2 conteo de palabras
palabras=texto.split()
num_palabras=str(len(palabras))
print("2- El texto tiene un total de "+num_palabras+" palabras")

#3 primera y ultima letra del texto
long=len(texto)
print("3- La primera letra del texto es: "+texto[0])
print("La última letra del texto es: "+texto[long-1])

#4
print("4- El texto con las mismas palabras ordenadas en inversa queda:")
palabras.reverse()
#print(palabras)
palabras2=" ".join(palabras)
print(palabras2)

#5 dice si aparece la palabra "Python"
print("5- A continuación se analizará si la palabra 'Python' aparece en el texto")
var="Python" in texto
dic={True:'La palabra se encuentra en el texto',False:'"Python" no se encuentra'}
print(dic[var])
