# Desarrollar un programa que permita cargar n números enteros
# y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional
# (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

limite = int(input("Hasta que numero?"))
contador = 1
numPar = 0
numImpar = 0

while contador < limite:
    if contador % 2 == 0:
        numPar += 1
    else:
        numImpar += 1
    contador += 1

print(f"Numeros pares {numPar} y numeros impares {numImpar}")
