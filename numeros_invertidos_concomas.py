"""
Ejercicio 5
Escribir un programa que almacene en una lista los números 
del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

lista = [1,2,3,4,5,6,7,8,9,10]

lista= lista[::-1]
print(lista)

"""
SOLUCION ALF #1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")


SOLUCION ALF #2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")


"""
   