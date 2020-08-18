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


#Ejercicio 8

num = int(input('Ingrese el número correspondiente al argumento: '))
base = int(input('Ingrese el número de la base logaritmica: '))

def LogaritmoRec(base, num):
    if(base == num):
        return 1
    else:
        return 1 + LogaritmoRec(base, num/base)

print('El logaritmo es: ', LogaritmoRec(base, num))


#Ejercicio 9

num = int(input('Ingrese el número a ser contado: '))

def ContadorRec(num):
    if (num < 10):
        return 1
    else:
        return 1 + ContadorRec(num//10)

print('La cantidad de dígitos es: ', str(ContadorRec(num)))

#Ejercicio 10

numero = int(input('Ingrese el número a invertir: '))

def invertir(numero):
    if(numero<10):  
        return numero
    else:
        return (numero % 10) * (10 ** (len(str(numero))-1)) + invertir(numero//10)

print('El número invertido es: ', invertir(numero))

#Ejercicio 11

m = int(input('Ingrese el primer número: '))
n = int(input('Ingrese el segundo número: '))

def mcdRec(m, n):
    if(m % n == 0):
        return n
    else:
        return mcdRec(n, m % n)

print('El M.C.D es: ', mcdRec(m, n))

#Ejercicio 12

m = int(input('Ingrese el primer número: '))
n = int(input('Ingrese el segundo número: '))

def mcmRec(m, n):
    if(n % m == 0):
        return n
    else:
        return mcmRec(n, m * n)

print('El M.C.M es: ', mcmRec(m, n))

#Ejercicio 13

n = int(input('Ingrese el número deseado: '))

def sumdigRec(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumdigRec(n//10)
 
print('La suma de los dígitos es:', sumdigRec(n))

#Ejercicio 14

num = int(input('Ingrese el número entero a radicar: '))
mult = 1

def raizRec(num, mult):
    if (mult * mult) <= num :
        return mult
    else:
        return raizRec(num, mult - 1)

def raizC(num):
    if num == 0:
        return 0
    else:
        return raizRec(num, num)

print('El resultado es:', raizC(num))

#Ejercicio 15

termino = int(input('Ingrese el termino mayor a 0 a calcular: '))

def suc_geo(termino):
    if termino == 1:
        return 2
    else:
        return suc_geo(termino -1) * -3

for i in range(1, termino + 1):
    print('Valor en el término', i, ':', suc_geo(i))

#Ejercicio 16

def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

vec = [1,2,3,4]

print(barrido(vec))

#Ejercicio 17

mat = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
        print(mat[i][j])

def barrido_matriz(mat, i, j):
    if(i<len(mat) and j<len(mat[i])):
        print(mat[i][j])
        if(j == len(mat[i])-1):
            i += 1
            j = -1
        barrido_matriz(mat, i, j+1)

for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
        print(barrido_matriz(mat, i, j))

#Ejercicio 18

num = int(input('Ingrese el termino deseado mayor a 0 : '))

def sucesionRec(num):
    if num == 1:
        return 2
    else:
        return num + (1 / sucesionRec(num - 1))

print('El valor de la sucesion es:', sucesionRec(num))

#Ejercicio 24

termino = int(input('Ingrese el término de la sucesión que desee ver: '))

def sucesiongeo(termino):
    if(termino==1):
        return 5.25
    else:
        return sucesiongeo(termino-1) * 4

print('El resultado es: ', sucesiongeo(termino))

#Ejercicio 25

num = int(input('Ingrese el termino a calcular: '))

def suc_rec(num):
    if num == 1:
        return 3
    else:
        return (2*num) + suc_rec(num - 1)

print('El resultado es:', suc_rec(num))
'''