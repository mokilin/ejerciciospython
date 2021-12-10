
# Preguntar al usuario por la renta
renta = float(input('ingrese su renta anual: '))

# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
    print('le corresponde abonar el 5 %')
elif renta >= 10000 and renta <= 20000:
    tipo = 15
    print('le corresponde abonar el 15 %')
elif renta >20000 and renta <= 35000:
    tipo = 20
    print('le corresponde abonar el 20 %')
elif renta >35000 and renta <= 60000:
    tipo = 30
    print('le corresponde abonar el 30 %')

else:
    tipo = 60
    print('le corresponde abonar el 60 %')

print('Que es igual a: ' + (str(renta * tipo / 100)))
    