renta = float(input('ingrese su renta anual: '))


if renta < 10000:
    print('le corresponde abonar el 5 %')
elif renta >= 10000 and renta <= 20000:
    print('le corresponde abonar el 15 %')
elif renta >20000 and renta <= 35000:
    print('le corresponde abonar el 20 %')
elif renta >35000 and renta <= 60000:
    print('le corresponde abonar el 30 %')

else:
    print('le corresponde abonar el 60 %')
    