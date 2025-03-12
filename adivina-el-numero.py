# Genera un número aleatorio entre 1 y 20. Pide al usuario que lo adivine y dale pistas de si el número es mayor o menor.
import random

print("BIENVENIDO AL JUEGO")

name = input("qual o seu nome?: ")

numero_secreto = random.randint(0, 20)
adivinado = False

while not adivinado:
    entrada = input(f"{name} escolha um numero de 0 a 20: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("felicidades! voce acertou!")
        adividado = True

    elif numero > numero_secreto:
        print(f"{name} o numero secreto é menor que o escolhido")
    else:
        print(f"{name} o numero secreto é maior que o escolhido")
print("FIM DE JOGO")
