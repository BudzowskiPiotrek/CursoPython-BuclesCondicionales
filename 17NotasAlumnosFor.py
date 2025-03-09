# Escribir un programa que solicite por teclado 10 notas de alumnos y nos
# informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
suma = 0
for var in range(0, 11):
    numero = int(input("Dime una nota: "))
    if 10 >= numero >= 7:
        suma += 1

print(f"de las 10 notas cantidad de {suma} es superior o igual de 7")
