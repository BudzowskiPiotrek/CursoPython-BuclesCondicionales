# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

contador = 0

while contador < 500:
    if contador % 8==0:
        print(contador)
    contador+=1
