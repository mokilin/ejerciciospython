

def divisores (num):
   
    divisores=[]
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores



def run():
    try:
        num = int(input('Ingresá un número entero: '))
        assert num > 0, 'El número debe ser positivo'
        print(divisores(num))
    except ValueError:
        print('Debes ingresar un número ')

if __name__ == '__main__':
    run()




