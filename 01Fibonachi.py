# Calcula e imprime los primeros 10 números de la sucesión de Fibonacci utilizando bucles y variables.
a = 0
b = 1

for var in range(1, 10):
    c = a + b
    print(c, "", end="")
    a = b
    b = c

# o

a, b = 0, 1
fibonacci = [a]

for _ in range(10):
    a, b = b, a + b
    fibonacci.append(a)

# _ La barra baja _ en for _ in range(n) es una convención en Python que indica que la variable no se usará dentro del bucle.
print(fibonacci)

# o

print([" ".join(map(str, fibonacci))])

# map(función, iterable) aplica la función str() a cada elemento de fibonacci, convirtiéndolos en texto.
# " ".join(iterable) une los elementos de la lista en una sola cadena, separándolos con un espacio " ".
