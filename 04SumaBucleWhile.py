# pide al usuario 10 numeros y sumalos con bucle while
contador = 0
suma = 0

while contador < 10:
    numero = int(input("Dime un numero: "))
    suma += numero
    contador += 1
    
promedio = suma / 10
print(f"el promedio es de: {promedio}")
print(f"la suma es de: {suma}")
print("Programa ha terminado")
