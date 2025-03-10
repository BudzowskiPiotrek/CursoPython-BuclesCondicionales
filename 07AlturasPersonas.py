# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

limite = int(input("Cuantas alturas vas a subir: "))
contador = 0
resultado = 0
while contador < limite:
    altura = int(input(f"dime altura numero {contador}:"))
    resultado += altura
    contador += 1
promedio = resultado / limite

print(f"el promedio de {limite} personas es de {promedio}")
