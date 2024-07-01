from random import *
estado='s'
#while estado=='s':
nombre=input("Bienvenido al juego de adivinanza. Dime tu nombre: ")
print(f"Bueno {nombre}, el juego es así: Yo pienso un número al azar, y tu tienes que adivinarlo")
print("Las reglas son las siguientes:\n1. El numero va entre 1 y 100")
print("2. Tienes 8 intentos para adivinar")
print("3. Cada vez que te equivoques, te diré si el número es mayor o menor, de modo que te vayas acercando")
print("Comencemos! buena suerte")
while estado == 's':
    numero=randint(1,100)
    for n in range(1,9):
        eleccion=int(input(f"Intento numero {n}: "))
        if eleccion <0 or eleccion>100:
            print("El numero debe estar entre 0 y 100")
        elif eleccion<numero:
            print("El numero es mayor")
        elif eleccion>numero:
            print("El numero es menor")
        elif eleccion==numero:
            print(f"Adivinaste! Te ha tomado {n} intentos")
            break
    if eleccion!=numero:
        print(f"No Acertaste. El numero era {numero}")
    estado=input("Quieres volver a jugar?(s/n): ")
print("Gracias por jugar <3")


