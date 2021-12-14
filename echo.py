"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que 
el usuario introduzca hasta que el usuario escriba “salir” que terminará."""


contador =1

while contador !=0:
    echo = input('Haré eco de tus palabras escritas, hasta que escribas "salir": ')
    if echo != str('salir'):
       print(echo)
       contador +=1
    else:
       print('game over ')
       break