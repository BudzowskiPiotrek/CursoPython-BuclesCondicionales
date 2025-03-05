# Calcula e imprime los primeros 10 números de la sucesión de Fibonacci utilizando bucles y variables.
a = 0
b = 1

for var in range(1, 11):
    c = a + b
    print(c, "", end="")
    a = b
    b = c
