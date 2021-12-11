"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

edad = int(input('\n Cuál es tu edad? : '))
print('\n')

for i in range(edad):
    print('cumpliste ' + str(i+1))
