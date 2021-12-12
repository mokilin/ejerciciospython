"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido 
en la inversión cada año que dura la inversión."""


cantidad = float(input('Cuánto dinero quiere invertir?: '))
interes_anual = float(input('Cuál es el interés anual?: '))
anios = int(input('Por cuántos años desea mantener el dinero en la inversión?: '))

for i in range(anios):
    interes_obtenido = (cantidad * interes_anual/100)
    capital_obtenido = (cantidad + interes_obtenido)
    cantidad = capital_obtenido
    print('Año' + ' i ' + 'obtiene ' + str(capital_obtenido) + ' pesos' )