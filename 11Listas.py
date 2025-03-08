# Realizar un programa que permita cargar dos listas de 15 valores
# cada una. Informar con un mensaje cual de las dos listas tiene un
# valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor",
# "Listas iguales")Tener en cuenta que puede haber dos o más estructuras
# repetitivas en un algoritmo.
contador = 0
valorUno = 0
valorDos = 0

while contador < 15:
    valor = int(input(f"dime el valor numero {contador}: "))
    valorUno += valor
    contador += 1

contador = 0

while contador < 15:
    valor = int(input(f"dime el valor numero {contador}: "))
    valorDos += valor
    contador += 1

if valorUno > valorDos:
    print("Lista 1 mayor")
elif valorDos > valorUno:
    print("Lista 2 mayor")
else:
    print("Listas iguales")
