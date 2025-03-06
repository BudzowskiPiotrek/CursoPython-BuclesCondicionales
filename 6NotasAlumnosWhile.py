# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.

contador = 0
notasValidas = 0
while contador < 10:
    nota = int(input(f"Dime la nota numero {contador}: "))
    contador += 1
    if nota >= 7:
        notasValidas += 1

print(f"Las notas validas son : {notasValidas}")
