# Genera un número aleatorio entre 1 y 20. Pide al usuario que lo adivine y dale pistas de si el número es mayor o menor.
import random

print("BIENVENIDO AL JUEGO")

numero_secreto = random.randint(0, 20)
adivinado = False
print(f"o numero secreto es: {numero_secreto}")
while not adivinado:
    entrada = input("adivine un numero del 0 al 20: ")
    number = int(entrada)
    if number == numero_secreto:
        print("felicitaciones!!")
        adivinado = True
    elif number > numero_secreto:
        print("todavia no. el numero secreto es menor")
    else:
        print("el numero secreto es mayor que ese")
print("fin de juego")
