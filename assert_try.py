

def divisores (num):
   
    divisores=[]
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores



def run():
    #try:
        num = input('Ingresá un número entero: ') #el int me determina la posibilidad del value error
        assert num.isnumeric() and int(num) > 0, 'Sólo puedes ingresar un número positivo para operar'
        print(divisores (int(num)))
    #except ValueError:
        #print('Debes ingresar un número ')

if __name__ == '__main__':
    run()




