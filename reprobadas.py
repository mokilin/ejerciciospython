"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura y 
 elimine de la lista las asignaturas aprobadas. 
 Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

subjects = ['Matemáticas', 'Física', 'Química', 'Historia' , 'Lengua']
allmarks=[]
retake = []

for i in subjects:
    mark = int(input('Nota promedio obtenida en ' + i + ' '))
    allmarks.append(mark)
    
    
    
    #if mark < 6:
        #retake.append(i)

print('\n')


retake = list(filter(lambda i: i < 6, allmarks))

for i in retake:
    print('Debes recursar '+ str(i))

    #pares = list(filter(lambda i: i%2 == 0, my_list))

# retake = list(filter(lambda i: i < 6, subjects))


