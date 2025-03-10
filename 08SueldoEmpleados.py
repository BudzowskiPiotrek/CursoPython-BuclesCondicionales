# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
# realizar un programa que lea los sueldos que cobra cada empleado e informe
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además
# el programa deberá informar el importe que gasta la empresa en sueldos al personal.

numeroEmpleados = int(input("Cuantos empleados tiene: "))
contador = 0
grupoA = 0
grupoB = 0

while contador < numeroEmpleados:
    sueldo = int(input("Dime cual es tu sueldo: "))
    if 600 > sueldo > 300:
        grupoB += 1
    elif 300 > sueldo > 100:
        grupoA += 1
    else:
        print("ingresaste mal tu sueldo")
    contador += 1

print(f"Grupo de 100 a 300 son: {grupoA}")
print(f"Grupo de mas de 300 son: {grupoB}")
