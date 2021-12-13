"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

En esta versión le doy al usuario hasta cuatro intentos para introducir la contraseña
correcta """

password = str('tiffmoki')

acceso = input(' \n Bienvenido, introduzca su contraseña para acceder: ')


for i in range(3):
    
    if acceso != password:
       
        acceso = input('incorrecta, intente otra vez: ')
        if acceso == password:
            print('Ud. ha accedido correctamente! ')
            acceso = 1 
            break
        else:
            continue
    else:
       print('Ud. ha accedido correctamente! ')
       acceso = 1  
       break
       
    
if acceso != 1:
    print('clave bloqueada, inténtelo nuevamente más tarde')
else:
    print('Continúe con el proceso')

      







    
    


   
        
    
        
        
        

    
        
    
    