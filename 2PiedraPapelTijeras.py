# Simula el juego de 'Piedra, Papel o Tijera' entre el usuario y la computadora,
# utilizando condicionales para determinar el ganador.
import random

pc = random.randint(1, 3)
us = int(input("elige 1 para piedra, 2 para papel, 3 para tijera: "))
if pc == us:
    print("empate han elegido lo mismo")
elif pc == 1 & us == 3 | pc == 2 & us == 1 | pc == 13 & us == 2:
    print("Ha ganado la maquina")
else:
    print("has ganado tu")
    

# o

import random

opciones = {1: "piedra", 2: "papel", 3: "tijera"}
pc = random.choice(list(opciones.keys()))

try:
    us = int(input("Elige: 1 para piedra, 2 para papel, 3 para tijera: "))
    if us not in opciones:
        print("Opción inválida, elige un número entre 1 y 3.")
    else:
        print(f"Tú eliges: {opciones[us]}")
        print(f"La máquina elige: {opciones[pc]}")

        if pc == us:
            print("Empate, han elegido lo mismo.")
        elif (pc == 1 and us == 3) or (pc == 2 and us == 1) or (pc == 3 and us == 2):
            print("Ha ganado la máquina.")
        else:
            print("¡Has ganado tú!")
except ValueError:
    print("Por favor, ingresa un número válido.")

