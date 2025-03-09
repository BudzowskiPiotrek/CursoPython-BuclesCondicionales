# Escribe un programa en Python que pida al usuario cuántos valores va a
# ingresar. Luego, solicita esos valores uno por uno y al final muestra cuántos
# números negativos se ingresaron.

limite = int(input("Dime cuantos numeros vas a sumar: "))
positivo = 0
negativo = 0
for var in range(0, limite):
    numero = int(input("Dime un numero: "))
    if numero < 0:
        negativo += 1
    else:
        positivo += 1

print(f"Numeros positivos: {positivo}")
print(f"Numeros positivos: {negativo}")
