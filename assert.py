
""" MI CODIGO
def divisores (num):
    #try:
       # if abs(num) == (-1)*num:
            #raise ValueError('no se puede ingresar un número negativo')

    #except ValueError as ve:
       # print(ve)
        #return False
    divisores=[]
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores



def run():
    try:
        num = int(input('Ingresá un número entero: '))
        #divisores(num)
        assert num > 0, 'El número debe ser positivo'
        print(divisores(num))
    except ValueError:
        print('Debes ingresar un número ')

if __name__ == '__main__':
    run()
"""



""" CODIGO DE COMPAñERA
def divisor(num):
    divisors =[i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def run():
    num = input(f'Ingresa un número: ') 
    assert num.isnumeric() > 0, "ingresa un número positivo"      
    print(divisor(int(num)))
    print("termino mi programa")

    
if __name__ =='__main__':
    run()   """


def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0] #USÓ LIST COMPREH
    return(divisors)

def run():

    num = input("Ingresa un numero:") # al parecer no es necesario poner int(input) ya que en la siguiente linea assert me lo asegura
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero positivo." #acá convierte num a int
    print(divisors(int(num))) #acá convierte a num a int
    print('El programa ha terminado')

if __name__ == '__main__':
    run()
