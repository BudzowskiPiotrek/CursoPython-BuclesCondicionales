#Una planta que fabrica perfiles de hierro posee un lote de n piezas.
#Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

cantidad = int(input("Dime la cantidad de las piezas: "))
x = 0
piezasValidad = 0

while x < cantidad:
    longitud = int(input(f"Dime la longitud en cm de la pieza número {x+1}: "))
    if 120 < longitud < 130:
        piezasValidad += 1
    x += 1

print(f"En el lote hay {piezasValidad} piezas válidas")
