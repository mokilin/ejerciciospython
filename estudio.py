"""def cuadrado(x):
    return x ** 2

print(cuadrado(3))"""

#lista=[1,2,3,4,5,6,7,8,9,10]

"""
------------------------------------------------------
EN LIST Y DICT COMPREH EL IF ES OPCIONAL - 

LA ESTRUCTURA ES:
list =[ i  for i in range(1,100000) if i%4 == 0 and i % 6 ==0 and i % 9 == 0]
print(list)

print(list)
dict = {i: round(i** 0.5, 2) for i in range (1001 )} 
print(dict)
--------------------------------------------------------

La función map() en Python APLICA UNA FUNCION a cada uno de los elementos de una lista.

La función filter() FILTRA una lista de elementos para los que una función devuelve TRUE

La función reduce  se utiliza principalmente para llevar a cabo un cálculo acumulativo
sobre una lista de valores y devolver el resultado.

"""

def divisores (num):
    try:
        if abs(num) == (-1)*num:
            raise ValueError('no se puede ingresar un número negativo')

    except ValueError as ve:
        print(ve)
        return False

    divisores=[]
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores



def run():
    try:
        num = int(input('Ingresá un número entero: '))
        #divisores(num)
        print(divisores(num))
    except ValueError:
        print('Debes ingresar un número ')

if __name__ == '__main__':
    run()
