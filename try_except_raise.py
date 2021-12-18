

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