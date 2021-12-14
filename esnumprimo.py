"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""


num = int(input('Ingrese un número entero: ')) #27
resto=[]
recipiente =[]
longi =0

for i in range (2,num): #i va del 2 al 27
    restito = num%i
    resto.append(restito) 

print([resto])

contador = 0
for i in resto: 
    if i == 0:
        print('numero no primo')
        recipiente.append(0)
        break
    else:
        recipiente.append(1)
        continue

for j in recipiente: 
    if j == 1:
        longi +=1


if longi == len(recipiente):
    print('número primo')
  


"""
  SOLUCION 1 ALF - RE FACIL!!!! 

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")"""
       
    
        

"""  SOLUCION 2 DE ALF NO TAN FACIL

n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
#print(i)
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
    """
   
   
    
