# Confeccionar un programa que lea n pares de datos, cada par de datos
# corresponde a la medida de la base y la altura de un triángulo. El programa
# deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.
# Ver video

limite = int(input("Dime cuantos numeros vas a sumar: "))
suma = 0
for var in range(0, limite):
    base = int(input("Dime un numero: "))
    altura = int(input("Dime un numero: "))
    superficie = base * altura
    print(f"Su base es: {base}")
    print(f"Su altura es: {altura}")
    print(f"Su superficie es: {superficie}")
    if superficie > 12:
        suma += 1

print(f"Superficia mas grande de las 12 de todas ingresadas: {suma}")
