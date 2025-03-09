# Escribir un programa que lea 10 números enteros y luego muestre cuántos
# valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en
# cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
multipleTres = 0
multipleCinco = 0
for var in range(0, 11):
    numero = int(input("Dime un numero: "))
    if numero % 3 == 0:
        multipleTres += 1
    if numero % 5 == 0:
        multipleCinco += 1

print(f"Multiples de tres: {multipleTres}")
print(f"Multiples de cinco: {multipleCinco}")
