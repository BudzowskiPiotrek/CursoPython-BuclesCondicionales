# Desarrollar un programa que permita la carga de 10 valores por teclado y nos
# muestre posteriormente la suma de los valores ingresados y su promedio. Este
# problema ya lo desarrollamos, lo resolveremos empleando la estructura for
# para repetir la carga de los diez valores por teclado.
suma = 0
for var in range(0, 11):
    numero = int(input("Dime un numero: "))
    suma += numero

promedio = suma / 10
print(f"el promedio es de: {promedio}")
print(f"la suma es de: {suma}")
print("Programa ha terminado")
