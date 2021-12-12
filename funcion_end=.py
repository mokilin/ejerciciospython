"""Ejercicio 3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas.


"""

numero = int(input('ingrese un número entero y positivo: '))

for i in range(numero):
    if (i%2) != 0:
        i = str(i)
        print(i, end = ", " )



