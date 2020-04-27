'''
#Ejercicio 1 "Fibonacci"

n = int(input('Ingrese cuantos números de la sucesión quiere ver: '))

def Fibonacci(num):
    a = 0
    b = 1
    i = 0
    for i in range(0, num):
        if(num > i):
            a, b = b, a+b
            print(a, b)

Fibonacci(n)


def FibonacciRec(num):
    if(num < 2):
        return num
    else:
        return FibonacciRec(num-1) + FibonacciRec(num-2)
        
num = int(input('Ingrese la posición del número: '))
print(FibonacciRec(num))



#Ejercicio 2

n = int(input('Ingrese hasta cuanto quiere sumar: '))

def sumatoria(num):
    i = 0
    suma = 0
    if(num <= 0):
        print('Tiene que ser un número positivo')
    else:
        for i in range(0, num+1):
            suma += i
            print('La sumatoria es: ', suma)

sumatoria(n)

num = int(input('Ingrese un número positivo, para realizar la sumatoria: '))

def SumatoriaRec(num):
    if(num == 0):
        return num
    else:
        return num + SumatoriaRec(num - 1)

print(SumatoriaRec(num))


#Ejercicio 3

n1 = int(input('Ingrese su primer número: '))
n2 = int(input('Ingrese su segundo número: '))

def producto(num1, num2):
    print('El producto es: ', num1 * num2)

producto(n1, n2)

def ProductoRec(num1, num2):
    if (num1 == 0 or num2 == 0):
        return 0
    else:
        return num1 + ProductoRec(num1, num2 - 1)

print('El producto es: ', ProductoRec(n1, n2))

#Ejercicio 4

n1 = int(input('Ingrese su primer número, el cual será la base: '))
n2 = int(input('Ingrese su segundo número, el cual será el exponente: '))

def potencia(num1, num2):
    print('La potencia es: ', num1 ** num2)

potencia(n1, n2)

def PotenciaRec(num1, num2):
    if(num1 == 1  or num2 == 0):
        return 1
    else:
        return num1 * PotenciaRec(num1, num2 - 1)

print('La potencia es: ', PotenciaRec(n1, n2))


#Ejercicio 5

cadena = input('Ingrese la palabra o número a invertir: ')
ind = len(cadena) 

def InvertirRec(cadena, ind):
    if(ind == 0 ):
        return ""
    else:    
        return cadena[ind - 1] + InvertirRec(cadena, ind -1)

print(InvertirRec(cadena, ind))


#Ejercicio 6

num = int(input('Ingrese hasta que número irá la serie: '))

def SerieRec(num):
    if(num == 1):
        return 1
    else:
        return (1 / num) + (SerieRec(num - 1))

print(SerieRec(num))


#Ejercicio 7

num = int(input('Ingrese el número a transformar en binario: '))

def BinarioRec(num):
    if(num == 0):
        return ''
    else:
        return BinarioRec(num // 2) + (str(num % 2))

print(BinarioRec(num))

'''
'''
#Ejercicio 8    POR TERMINARR

num1 = int(input('Ingrese el número correspondiente al argumento: '))
num2 = int(input('Ingrese el número de la base logaritmica: '))
n = 1

def LogaritmoRec(num1, num2, n):
    if(num1 == num2):
        return 1
    elif(num1 == 1):
        return 0
    elif(n == num1):
        return ''
    else:
        return num1 * LogaritmoRec(num1, num2, n + 1) 

print('El logaritmo es: ', LogaritmoRec(num1, num2, n))

'''

