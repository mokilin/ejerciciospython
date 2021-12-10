name = input('Nombre del empleado: ')
name = name.capitalize()
punct = float(input('Puntuación del mes: '))

if punct == 0.0:
    print('nivel rendimiento: Inaceptable ')
    print(name + ' no recibe recompensa adicional este mes')
elif punct == 0.4:
    print('nivel rendimiento: Aceptable ')
    print(name + ' recibe ' + str(float(2400 * 0.4)) + ' como recompensa adicional este mes')
elif punct >= 0.6:
    print('nivel rendimiento: Meritorio ')
    print(name + ' recibe ' + str(float(2400 * 0.6)) + ' como recompensa adicional este mes')
else:
    print('ese valor de puntuación no existe, indique el valor correcto')

