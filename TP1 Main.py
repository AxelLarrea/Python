'''
#Ejercicio 1 "Fibonacci"

# n = int(input('Ingrese cuantos números de la sucesión quiere ver: '))

# def Fibonacci(num):
#     a = 0
#     b = 1
#     i = 0
#     for i in range(0, num):
#         if(num > i):
#             a, b = b, a+b
#             print(a, b)

# Fibonacci(n)


def FibonacciRec(num):
    if(num < 2):
        return num
    else:
        return FibonacciRec(num-1) + FibonacciRec(num-2)
        
num = int(input('Ingrese la posición del número: '))
print(FibonacciRec(num))


#Ejercicio 2

# n = int(input('Ingrese hasta cuanto quiere sumar: '))

# def sumatoria(num):
#     i = 0
#     suma = 0
#     if(num <= 0):
#         print('Tiene que ser un número positivo')
#     else:
#         for i in range(0, num+1):
#             suma += i
#             print('La sumatoria es: ', suma)

# sumatoria(n)

num = int(input('Ingrese un número positivo, para realizar la sumatoria: '))

def SumatoriaRec(num):
    if(num == 0):
        return num
    else:
        return num + SumatoriaRec(num - 1)

print(SumatoriaRec(num))


#Ejercicio 3

# n1 = int(input('Ingrese su primer número: '))
# n2 = int(input('Ingrese su segundo número: '))

# def producto(num1, num2):
#     print('El producto es: ', num1 * num2)

# producto(n1, n2)

def ProductoRec(num1, num2):
    if (num1 == 0 or num2 == 0):
        return 0
    else:
        return num1 + ProductoRec(num1, num2 - 1)

print('El producto es: ', ProductoRec(n1, n2))

#Ejercicio 4

n1 = int(input('Ingrese su primer número, el cual será la base: '))
n2 = int(input('Ingrese su segundo número, el cual será el exponente: '))

# def potencia(num1, num2):
#     print('La potencia es: ', num1 ** num2)

# potencia(n1, n2)

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
    else:
        if(j == len(mat[i])-1):
            print(mat[i][j])
            j = 0
            barrido_matriz(mat, i+1, j)
        else:
            print(mat[i][j])
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




#Ejercicio 19

vec = [90, 87, 13, 1, 15, 3, 17, 21]
pos = 0

def busqueda(vec, pos, buscado):
    if pos == len(vec):
        return 'El elemento no está en la lista'
    elif (vec[pos] == buscado):
        return 'El elemento está en la lista'
    else:
        return busqueda(vec, pos+1, buscado)

buscado = int(input('Ingrese número a buscar'))

print(busqueda(vec, pos, buscado))



#Ejercicio 20

vec = [1, 3, 4, 8, 9, 10, 20, 21]
pos = 0

def bbin_rec(vec, buscado, pos, ult):
    if pos < ult:
        med = (pos+ult)//2
        if vec[med] == buscado:
            return med
        else:
            if vec[med] > buscado:
                return bbin_rec(vec, buscado, pos, med-1)
            else:
                return bbin_rec(vec, buscado, med+1, ult)

x = bbin_rec(vec, 2, pos, len(vec))
if x is not None:
    print('El elemento está en la lista, es:', vec[x])
else:
    print('El elemento no está en la lista')



#Ejercicio 21

troopers = [["20° 13' 22'' ", 'Cañón', 'Derribado'], ["37° 20' 53'' ", 'Blaster', 'No derribado'], ["50° 14' 33'' ", 'Cañón doble', 'Derribado']]
aux = []
pos = 0

def derribado(vec, aux, pos):
    if (pos == len(vec)):
        return aux
    elif(vec[pos][2] == 'Derribado'):
        aux += vec[pos]
        return derribado(vec, aux, pos+1)
    else:
        return derribado(vec, aux, pos+1)

print(derribado(troopers, aux, pos))


#Ejercicio 22

def matriz_laberinto(i, j, mat):
    tam = len(mat)
    if i == tam-1 and j == tam-1:
        return 'Salio del laberinto'
    else:
        if i == tam-1:
            if mat[i][j+1] == 0:
                print('derecha')
                return matriz_laberinto(i, j+1, mat)
            else:
                if mat[i-1][j] == 0:
                    print('arriba')
                    mat[i][j] = 1
                    return matriz_laberinto(i-1, j, mat)
        else:
            if j == tam-1:
                if mat[i+1][j] == 0:
                    print('abajo')
                    return matriz_laberinto(i+1, j, mat)
                else:
                    if mat[i][j-1] == 0:
                        print('izquierda')
                        mat[i][j] = 1
                        return matriz_laberinto(i, j-1, mat)
            else:
                if mat[i+1][j] == 0:
                    print('arriba')
                    return matriz_laberinto(i+1, j, mat)
                else:
                    if mat[i][j+1] == 0:
                        print('derecha')
                        return matriz_laberinto(i, j+1, mat)
                    else:
                        # mat[i][j] = 1
                        if mat[i-1][j] == 0:
                            print('arriba')
                            return matriz_laberinto(i-1, j, mat)

mat = [[0,1,1], 
       [0,1,0], 
       [0,0,0], 
       [1,1,0]]

matriz_laberinto(0, 0, mat)


'''
#Ejercicio 23

def torre_hanoi(discos, aguja1, aguja2, aguja3, cont):
    if (discos <= 0):
        print('Listo. La cantidad de movimientos fueron:', cont)
    else:
        torre_hanoi(discos-1, aguja1, aguja3, aguja2, cont+1)
        #print('Se mueve de aguja1 a aguja3')
        torre_hanoi(discos-1, aguja2, aguja1, aguja3, cont+1)

cont = 0
aguja1 = 10
aguja2, aguja3 = 0, 0
discos = 10
torre_hanoi(discos, aguja1, aguja2, aguja3, cont)
print('A1:', aguja1,'A2:', aguja2, 'A3:', aguja3)

'''
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