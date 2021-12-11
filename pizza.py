

ingredientescomunes = ['mozzarella', 'tomate']
ingredientesveggies = ['pimiento', 'tofu']
ingredientesnoveggies = ['peperoni', 'jamón', 'salmón']

pedido = input('\n Buenas noches, por favor ingrese "V" para pizza veggie y "C" para pizza común: ')
print('\n')


print('Su pizza contiene los siguientes ingredientes: \n')

if pedido == 'v':
    for i in ingredientescomunes:
        print(i)
    for i in ingredientesveggies:
        print(i)
   
if pedido == 'c':
    for i in ingredientescomunes:
        print(i)
    for i in ingredientesnoveggies:
        print(i)

print('\n' )
print('Gracias por elegirnos :)  \n')
print('Esperamos volver a verle pronto')