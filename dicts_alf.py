"""
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda in monedas:   #ATENCION A ESTO
    print(monedas[moneda])  #ATENCION A ESTO
else:
    print("La divisa no está.")
"""

"""
Escribir un programa que guarde en una variable el diccionario {'rojo':'stop',
 'amarillo':'precaucion', 'verde':'avanzar'}, 
pregunte al usuario por una color
y muestre su significado o un mensaje de aviso si el color no está en el diccionario


"""

colores = {'rojo':'stop', 'amarillo':'precaucion','verde':'avanzar'}

color = input('ingrese un color ')
    
assert color in colores, 'color no apto'

if color in colores:
    print(colores[color])

    
else:
    print('color no apto')