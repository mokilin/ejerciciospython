"""Ejercicio 1
Escribir una función que muestre por pantalla
 el saludo ¡Hola amiga! cada vez que se la invoque.





def saludo():
    print('hola amiga! ')


def run():
    saludo()

if __name__ == '__main__':
    run()     
"""

"""
Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre>
 y muestre por pantalla el saludo ¡hola <nombre>!.



def saludo(nombre):
    print('hola '+ nombre + ' !')


def run():
    nombre = input('Cuál es tu nombre? ')
    saludo(nombre)

if __name__ == '__main__':
    run()     """


"""
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


def gravado(amount,iva):
    gravado = amount*iva/100
    return(gravado)


def run():
    amount =float(input('Ingrese total del ticket a pagar: '))
    iva = float(input('Ingrese el porcentaje iva a aplicar (si desconoce, presione "0"): '))
    if iva == 0:
        iva = 21
    print('el importe gravado es de: ')
    print(gravado(amount,iva))
    total = gravado(amount,iva)+amount
    
    print('el importe total a abonar asciende a ' + str(total))

if __name__ == '__main__':
    run()"""

"""

Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media.

numbers = [1,2,3,4,5,6,7,8,9]
half = list(map(lambda i: i/2, numbers))

print('La lista inicial es: ')
print(numbers)
print('y sus mitades son: ')
print(half)    """


"""


"""

