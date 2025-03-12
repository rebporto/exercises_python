import random

secret_number = random.randint(0, 20)
adivinado = False
print("Bien venido al juego!")

entrada = input("guess a number from 1 to 20: ")
numero = int(entrada)
while not adivinado:
    if numero == secret_number:
        print("felicitaciones! acertou")
        break
    elif numero < secret_number:
        print("la respuesta es mayor que esa")
        numero = int(input("Intenta nuevamente: "))

    else:
        print("las respuesta es menor que esa")
        numero = int(input("Intenta nuevamente: "))


print("fin de juego")
