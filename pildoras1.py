"""
Ejercicio 1:
• Crea un programa que pida dos números por teclado.
 El programa tendrá una función llamada “DevuelveMax” 
 encargada de devolver el número más alto de los dos introducidos.



num1=int(input('Ingrese el primer número: '))
num2=int(input('Ingrese el segundo número: '))

def devuelvemax(n1,n2):
    iguales = 'Ambos números son iguales'
    if n1>n2:
        return n1
    elif n2>n1:
        return n2
    else:
        return iguales


print('Resultado: ',devuelvemax(num1,num2))   

...................................................


Ejercicio 2:

• Crea un programa que pida por teclado “Nombre”, 
“Dirección” y “Tfno”. Esos tres datos deberán ser almacenados 
en una lista y mostrar en consola el mensaje: “Los datos personales son: 
nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).


lista=[]

nombre=input('Nombre: ')
dire = input('Dirección: ')
tel = input('Teléfono: ')

lista.append(nombre)
lista.append(dire)
lista.append(tel)


print('Los datos personales son: \n')
for i in lista:
    print(i)


............................................................ 




Ejercicio 3:
• Crea un programa que pida tres números por teclado.
 El programa imprime en consola la media aritmética /promedio
  de los números introducidos.



n1= int(input('Primer número: '))
n2= int(input('Segundo número: '))
n3= int(input('Tercer número: '))

def prom(num1,num2,num3):
    average = round((num1+num2+num3)/3,2)
    return average


print('Promedio: ',prom(n1,n2,n3))

......................................................


Ejercicio 1:
• Crea un programa que muestre los números impares del 1 al 100. 
Los números deberán aparecer una al lado del otro sin salto de línea.



for i in range(100):
    if i%2!= 0:
        print(i, end=' ')


................................................

Ejercicio 2:
• Crea un programa que pida por teclado introducir una contraseña.
La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco.
Si la contraseña es correcta, el programa imprime “Contraseña OK”.
En caso contrario imprime “Contraseña errónea”    


password = input('Ingrese su contraseña, deberá tener un mínimo de 8 caracteres, sin espacios:  ')

def verificacion (pas):
    check= True
    sumaletras=0
    for i in (pas):
        if i != ' ':
            sumaletras+=1
    #print(sumaletras) esto está contando OK
    for i in (pas):
        if i == ' ' or sumaletras < 8:
            check = False
    return check # IMPORTANTE: LA UBICACION DEL RETURN CAMBIA EL RESULTADO!



if verificacion(password):
    print('Contraseña OK')
else:
    print('Contraseña Incorrecta')


......................................................................

Ejercicio 3:
• Crea un programa que evalúe si una dirección de correo electrónico
 es válida o no en función de si tiene “@” o “.” Hay que tener en cuenta 
 que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”
           
 

email = input('Ingresá tu email: ')


def comprobacion (em):
    check = False
    puntos = 0
    arroba = 0
    for i in em:
        if i == '.':
            puntos+=1
        elif i == '@':
            arroba+=1
    
    if puntos >= 1 and arroba == 1:
        check=True
    
    return check

if comprobacion(email):
    print('La dirección de correo introducida es correcta')
else:
    print('La dirección de correo introducida es incorrecta')

............................................


Ejercicio 1:
• Crea un programa que pida números infinitamente. 
Los números introducidos deben ser cada vez mayores 
El programa finalizará cuando se introduce un número 
menor que el anterior.   


num1=int(input('Ingresá un número: '))

num2=int(input('Ingresá un número mayor que el anterior: '))

while num2 > num1:
    num1 = num2
    num2=int(input('Ingresá un número mayor que el anterior: '))

print('El número que ingresaste es menor que el anterior')

.........................................

Ejercicio 2:
• Crea un programa que pida números positivos indefinidamente. 
El programa termina cuando se introduce un número negativo. 
Finalmente el programa muestras la suma de todos los números introducidos 


n=int(input('Introduce un número: '))
suma = 0

while n > 0:
    suma += n
    n=int(input('Intruce un número: '))

print('Ese último número es negativo. El programa finaliza. La suma de todos los números aceptado es ',suma)


................. practica aleatoria .................


Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir
la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  
(Un poco mas emocionante) 
 

   


def nombres_con_a (lista_de_nombres):
    nombres_seleccionados=[]
    for i in lista_de_nombres:
        if i[0] == 'A':
            nombres_seleccionados.append(i)
    return nombres_seleccionados


lista=[]
for i in range(5):  
    nombre=input('Ingresá un nombre: ')
    nombre=nombre.capitalize()
    lista.append(nombre)

print(nombres_con_a(lista))

.......................................

Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra 
y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y 
así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.


def contar_vocales(palabra):
    a=0
    e=0
    i=0
    o=0
    u=0
    for letra in palabra:
        if letra == 'a':
            a+=1
        elif letra == 'e':
            e+=1
        elif letra == 'i':
            i+=1
        elif letra == 'o':
            o+=1
        elif letra == 'u':
            u+=1

    print('cantidad de "a" : ',a)
    print('cantidad de "e" : ',e)
    print('cantidad de "i" : ',i)
    print('cantidad de "o" : ',o)
    print('cantidad de "u" : ',u)

palabra=input('Palabra: ')
contar_vocales(palabra)


.......................................

Ordenamiento de dos listas NO FUNCIONA CORRECTAMENTE 



def ordena_listas(lista_a,lista_b):
    lista_ordenada =[]
    long_a=len(lista_a)
    long_b=len(lista_b)
    i=j=0
    
    while i < long_a and j < long_b:
        if lista_a[i] < lista_b[j]:
            lista_ordenada.append(i)
            i+=1
        else:
            lista_ordenada.append(j)
            j+=1
    
    while i < long_a:
        lista_ordenada.append(lista_a[i])
        i+=1
    while j < long_b:
        lista_ordenada.append(lista_b[j])
        j+=1

    return lista_ordenada





lista_a =[4,7,2,5]

lista_b=[9,1,6,3]   

print(ordena_listas(lista_a,lista_b))  

........................................................

Ejercicio 1:
• Crea un programa que pida introducir una dirección de email 
por teclado. El programa debe imprimir en consola si la dirección 
de email es correcta o no en función de si esta tiene el símbolo ‘@’. 
Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
 ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo 
 de la dirección de email o al final, la dirección también será errónea,





def comprobacion (em):
    global email
    check = False
    puntos = 0
    arroba = 0
    
    
    for i in em:
        if i == '.':
            puntos+=1
        elif i == '@':
            arroba+=1
    
    if puntos >= 1 and arroba == 1:
        check=True
    
    return check



email = input('Ingresá tu email: ')

while email[0] == '@' or email[len(email)-1]  == '@': # USAR FUNCION FIND
    print('La @ no puede estar en primera o última posición del email introducido')
    email = input('Ingresá tu email: ')

            

if comprobacion(email):
    print('La dirección de correo introducida es correcta')

else:
    print('La dirección de correo introducida es incorrecta') """











