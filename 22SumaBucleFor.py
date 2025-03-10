# Desarrollar un programa que solicite la carga de 10 números e imprima la suma
# de los últimos 5 valores ingresados.

suma = 0
for var in range(0, 10):
    numero = int(input("Dime un numero: "))
    if var >= 5:
        suma += numero

print(f"la suma de ultimos 5 numeros es: {suma}")