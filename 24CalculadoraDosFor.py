# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos
# muestre la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el
# 36.

while True:
    limite = int(input("Dime un valor entre 1 hasta 10: "))
    if 10 >= limite > 0:
        break

for var in range(limite, (13 * limite), limite):
    print(f"{var} x {var} = {var * var}")
