# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
# iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

limite = int(input("Dime cuantos vas a ingresar: "))
equilatero = 0
isosceles = 0
escaleno = 0

for var in range(0, limite):
    ladoA = int(input("Dime cuanto tiene lado a: "))
    ladoB = int(input("Dime cuanto tiene lado b: "))
    ladoC = int(input("Dime cuanto tiene lado c: "))
    if ladoA == ladoB == ladoC:
        print("Es un Equilatero")
        equilatero += 1
    elif ladoA == ladoB | ladoB == ladoC | ladoC == ladoA:
        print("Es un Isosceles")
        isosceles += 1
    else:
        print("Es un Escaleno")
        escaleno += 1

print(
    f"de los ingresados, {equilatero} - fueron equilateros,{isosceles} - fueron isosceles,{escaleno} - fueron escaleno"
)
