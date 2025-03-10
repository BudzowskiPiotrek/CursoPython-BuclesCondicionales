# Solicita un límite al usuario y calcula la suma de todos los números primos hasta ese valor,
# utilizando un bucle while y verificaciones de divisibilidad.

limite = int(input("Hasta donde¿?"))
suma = 0
num = 2  # para saltarse el 1

while num <= limite:
    es_primo = True
    i = 2
    while i < num:
        if num % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        suma += num
    num += 1

print(f"La suma de los numero primos hasta el limite es: {suma}")
