"""
Ejercicio 1
Escribir un programa que almacene las asignaturas 
de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista y la muestre por pantalla.

subjects = ['Maths', 'Physics', 'Literature', 'Chemestry', 'History']

for i in subjects:
    print(i)

---------------------------
Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una
 lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
 donde <asignatura> es cada una de las asignaturas de la lista.

subjects = ['Maths', 'Physics', 'Literature', 'Chemestry', 'History']

for i in subjects:
    print('I study '+ i)  
    
 ------------------------------


Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura> has 
sacado <nota> donde <asignatura> es cada una des las asignaturas de 
la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.   
    
    
    
     """

#marks = {'Maths': 10, 'Physics':8, 'Literature':9, 'Chemestry':7, 'History':4}
# # Añade un nuevo elemento al diccionario
# dic['tres'] = 3  ----> tres : 3

subjects = ['Maths', 'Physics', 'Literature', 'Chemestry', 'History']
list =[]
dict ={}
for i in subjects:
    mark =input('Please type the mark you got in ' + i +' : ')
    #list.append('You got a ' + mark + ' in ' + i   )
    dict[i] = mark

for key,value in dict.items():
    print('You got a '+ key + ' in '+ value)