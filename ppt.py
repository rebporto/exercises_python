# Modifica tu código del juego para que el usuario juegue contra la computadora en lugar de otro jugador.

import random

name = input("qual seu nome?: ")
adivinado = False
print(f"Bem vinda ao jogo {name}")


while not adivinado:
    eleccion = random.choice(["pedra", "papel", "tesousa"])
    entrada = input("escolhe pedra, papel ou tesousa?: ")

    if entrada == eleccion:
        print("Empate!")

    elif (
        (entrada == "pedra" and eleccion == "tesoura")
        or (entrada == "tesoura" and eleccion == "papel")
        or (entrada == "papel" and eleccion == "pedra")
    ):
        print("Voce ganhou!")
        adivinado = True
        break
    else:
        print("voce perdeu :( ")
