# Codificar un programa que lea n números enteros y calcule la cantidad de
# valores mayores o iguales a 1000 (n se carga por teclado)
# Este tipo de problemas también se puede resolver empleando la estructura
# repetitiva for. Lo primero que se hace es cargar una variable que indique la
# cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la
# estructura repetitiva for.
limite = int(input("Dime cuantos numeros vas a sumar: "))
suma = 0
for var in range(0, limite):
    numero = int(input("Dime un numero: "))
    if numero >= 1000:
        suma += 1

print(
    f"En {limite}, cantidad de veces que numero fueron mayores o iguales a 1000 fueron: {suma}"
)
