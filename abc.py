"""
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

FORMA TRADICIONAL:

abc = ['a','b','c','d','e','f','g','h','i','j','k']
newabc=[]

for i in abc:
    if abc.index(i)%3!=0:
        newabc.append(i)

print(newabc) 

"""
#LIST COMPREHENSIONS:

abc = ['a','b','c','d','e','f','g','h','i','j','k']

newabc = [i for i in abc if abc.index(i)%3 != 0]

print(newabc)


        








