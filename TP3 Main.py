from Cola_Dinamico import Cola, arribo, atencion, cola_vacia, tamanio, en_frente, mover_final
from random import randint, choice
#from Pila_Dinamico import Pila, apilar, desapilar, pila_vacia, tamanio
from math import asin, cos, sin, sqrt, radians

'''


#Ejercicio 1

cola = Cola()
cola2 = Cola()

while not cola_llena(cola):
    x = input('Ingrese las letras deseadas: ')
    arribo(cola, x)
print('Lista de letras: ')
for i in range(0, tamanio(c)):
    print(mover_final(c))

while not cola_vacia(cola):
    x = atencion(cola)
    if ((x != 'a') and (x != 'e') and (x != 'i') and (x != 'o') and (x != 'u')):
        arribo(cola2, x)

while not cola_vacia(cola2):
    x = atencion(cola2)   
    print('Lista de letras sin vocales: ', x)



# Ejercicio 2

cola = Cola()
pila = Pila()

while (tamanio(cola) < 5):
    x = int(input('Ingrese los números deseados: '))
    arribo(cola, x)

print('Los datos ingresados son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)

print('Los datos al revés son: ')

while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)



#Ejercicio 3

cola = Cola()
cola2 = Cola()
pila = Pila()
status = False

print('Ingrese su palabra letra por letra: ')
while (tamanio(cola) < 4):
    x = input('Ingrese la letra correspondiente: ')
    arribo(cola, x)
    arribo(cola2, x)

print('Los datos ingresados son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)

while not (pila_vacia(pila) and cola_vacia(cola2)):
    x = desapilar(pila)
    y = atencion(cola2)
    if (x == y):
        status = True

if (status == True):
    print('Es palindromo')
else:
    print('No es palindromo')



#Ejercicio 4

cola = Cola()
cola2 = Cola()
cont = 0

while (tamanio(cola) < 10):
    x = randint(0,10)
    arribo(cola, x)

print('Los datos son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    for i in range(1, x+1):
        if ((x % i) == 0):
            cont += 1
    if (cont < 3):
        arribo(cola2, x)
    cont = 0

print('Los datos sin números compuestos: ')
for i in range(0, tamanio(cola2)):
    print(mover_final(cola2))



#Ejercicio 5

pila = Pila()
cola = Cola()

while (tamanio(pila) < 10):
    x = int(input('Ingrese numeros: '))
    apilar(pila, x)

while not pila_vacia(pila):
    x = desapilar(pila)
    arribo(cola, x)

print('Los datos invertidos son: ')
while not cola_vacia(cola):
    x = atencion(cola)
    print(x)



#Ejercicio 6

cola = Cola()
cont = 0

while (tamanio(cola) < 5):
    x = randint(0, 10)
    arribo(cola, x)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))

c = randint(0, 10)

for i in range (0, tamanio(cola)):
    x = atencion(cola)
    if (x == c):
        cont += 1

print('La cantidad de ocurrencias de', c, 'es:', cont )



#Ejercicio 7

cola = Cola()

while (tamanio(cola) < 10):
    x = int(input('Ingrese un número: '))
    arribo(cola, x)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))

c = atencion(cola)
atencion(cola)
arribo(cola, c)

print ('Dato a poner al frente:', c)

while not (en_frente(cola) == c):
    mover_final(cola)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))



#Ejercicio 8

cola = Cola()
cola2 = Cola()

for i in range(0, 10): 
    dato = randint(1, 50) 
    while not cola_vacia(cola) and en_frente(cola) <= dato: 
        arribo(cola2, atencion(cola))
    arribo(cola2, dato)
    while not cola_vacia(cola): 
        arribo(cola2, atencion(cola)) 
    while not cola_vacia(cola2): 
        arribo(cola, atencion(cola2)) 
    print()

print('Elementos de Cola: ')
for i in range (0, tamanio(cola)):
    print(mover_final(cola))



#Ejercicio 9

cola = Cola()
maximo = 0
minimo = 0
cant = 0

while (tamanio(cola) < 10):
    x = int(input('Ingrese un número entero:'))
    arribo(cola, x)
    if (x > maximo):
        maximo = x
    elif (x < minimo):
        minimo = x
        cant += 1

rango = (maximo - minimo) 

print('Los elementos de la cola son: ')
for i in range (0, tamanio(cola)):
    print(mover_final(cola))
print()

print('El rango es:', rango)
print('La cantidad de números negativos es:', cant)



#Ejercicio 10

class starwars(object):
    def __init__(self):
        self.nombre = ''
        self.planeta = ''
    
    def __str__(self):
        return self.nombre + " - " + self.planeta


cola = Cola()
cola2 = Cola()

while (tamanio(cola) < 3):
    sw = starwars()
    sw.nombre = input('Ingrese nombre del personaje: ')
    sw.planeta = input('Ingrese el planeta del personaje: ')
    arribo(cola, sw)
    print()

#A
print('A continuacion se mostrarán los personajes los cuales su planeta de origen sea: Alderaan, Endor o Tatooine: ')
for i in range(0, tamanio(cola)):
    dato = atencion(cola)
    if ((dato.planeta == 'Alderaan') or (dato.planeta == 'Endor') or (dato.planeta == 'Tatooine')):
        print(dato)
    arribo(cola2, dato)
print()

#B
for i in range(0, tamanio(cola2)):
    dato = atencion(cola2)
    if ((dato.nombre == 'Han Solo') or (dato.nombre == 'Luke Skywalker')):
        print('El planeta natal de', dato.nombre, 'es:', dato.planeta)
    arribo(cola, dato)
print()

#C
while not cola_vacia(cola):
    dato = atencion(cola)
    if (dato.nombre == 'Yoda'):
        sw = starwars()
        print('Ingrese los datos del nuevo personaje:')
        print()
        sw.nombre = input('Ingrese nombre del personaje: ')
        sw.planeta = input('Ingrese el planeta del personaje: ')
        arribo(cola2, sw)
    arribo(cola2, dato)
print()

#D
while not cola_vacia(cola2):
    dato = atencion(cola2)
    if(dato.nombre == 'Jar Jar Binks'):
        atencion(cola2)
    arribo(cola, dato)

print('Los elementos de la cola son: ')

for i in range(0, tamanio(cola)):
    print(mover_final(cola))



#Ejercicio 11

cola = Cola()
cola2 = Cola()
cola3 = Cola()

#Cargamos la primer cola ordenada
for i in range(0, 3): 
    dato = randint(1, 50) 
    while not cola_vacia(cola) and en_frente(cola) <= dato: 
        arribo(cola3, atencion(cola))
    arribo(cola3, dato)
    while not cola_vacia(cola): 
        arribo(cola3, atencion(cola)) 
    while not cola_vacia(cola3): 
        arribo(cola, atencion(cola3)) 
print()

print('Elementos de Cola: ')
for i in range (0, tamanio(cola)):
        print(mover_final(cola))

#Cargamos la segunda cola ordenada
for i in range(0, 3): 
    dato = randint(1, 50) 
    while not cola_vacia(cola2) and en_frente(cola2) <= dato: 
        arribo(cola3, atencion(cola2))
    arribo(cola3, dato)
    while not cola_vacia(cola2): 
        arribo(cola3, atencion(cola2)) 
    while not cola_vacia(cola3): 
        arribo(cola2, atencion(cola3)) 
print()

print('Elementos de Cola2: ')
for i in range (0, tamanio(cola2)):
        print(mover_final(cola2))
print()

#Juntamos ambas colas

#while (not(cola_vacia(cola)) and not(cola_vacia(cola2))):
#    if ((en_frente(cola)) <= (en_frente(cola2))):
#        dato = atencion(cola)
#        arribo(cola3, dato)
#    elif ((en_frente(cola)) > (en_frente(cola2))):
#        dato = atencion(cola2)
#        arribo(cola3, dato)
#if (cola is not None):
#   while not cola_vacia(cola):
#        dato = atencion(cola)
#        arribo(cola3, dato)
#elif (cola2 is not None):
#    while not cola_vacia(cola2):
#        dato = atencion(cola2)
#        arribo(cola3, dato)

for i in range (0, tamanio(cola)):
    if(en_frente(cola) < en_frente(cola2)):
        mover_final(cola)
    else:
        while(en_frente(cola) > en_frente(cola2)):
            dato = atencion(cola2)
            arribo(cola, dato)
        mover_final(cola)

while not(cola_vacia(cola2)):
    dato = atencion(cola2)
    arribo(cola, dato)

print('Elementos de la nueva cola: ')
for i in range (0, tamanio(cola)):
        print(mover_final(cola))



#Ejercicio 12

cola = Cola()
cola_dig = Cola()
cola_car = Cola()
letras = 0
existe = False

while (tamanio(cola) < 20):
    dato = randint(33, 126)
    arribo(cola, chr(dato))

print('Elementos de cola general: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))
print()

#A
while not (cola_vacia(cola)):
    dato = ord(atencion(cola))
    if ((dato >= 48) and (dato <= 57)):
        arribo(cola_dig, chr(dato))
    else:
        arribo(cola_car, chr(dato))

print('Elementos de cola digitos: ')
for i in range(0, tamanio(cola_dig)):
    print(mover_final(cola_dig))
print()

print('Elementos de cola caracteres: ')
for i in range(0, tamanio(cola_car)):
    print(mover_final(cola_car))
print()

#B y #C
for i in range(0, tamanio(cola_car)):
    dato = ord(atencion(cola_car))
    if((dato >= 65 and dato <= 90) or (dato >= 97 and dato <= 122)):
        letras += 1
    elif(dato == 63 or dato == 35):
        existe = True
    arribo(cola_car, chr(dato))
print()
print('El total de letras es:', letras)

if(existe == False):
    print('Los caracteres no existen')
else:
    print('El/los caracteres si existen')



'''
#Ejercicio 14

cola = Cola()
bases = [['Pry', 30, 50, 47], ['Star', 57, 32, 20], ['Lion', 81, 113, 65]]
r = 6371000
q2 = 0
d2 = 0
cercana = 0
flota = 0
name = ''

def haversine(r, q1, q2, d1, d2):
    return 2*r*asin(sqrt(sin((q2-q1)/2)**2 + cos(q1)*cos(q2) * sin((d2-d1)/2)**2))

for i in range(0, 3):
    arribo(cola, bases[i])

print('Ahora deberá ingresar su posición actual')
q1 = int(input(print('Ingrese la latitud: ')))
d1 = int(input(print('Ingrese la longitud: ')))

while not cola_vacia(cola):
    x = atencion(cola)
    #A,B Determinar base más cercana
    data = haversine(r, q1, x[2], d1, x[3])
    if data < cercana:
        cercana = data
        name = x[0]
    #C Tres bases más cercanas
    
    #D Determinar la distancia hacia la base con mayor flota
    if x[1] > flota:
        flota = x[1]
        distancia = data





print('La base más cercana llamada', name, 'está a: ', cercana,'metros de distancia')
print('Distancia a la base con mayor flota aerea:', distancia)



'''
#Ejercicio 19

vehiculos = ['auto', 'camioneta', 'camion', 'colectivo']
costo = [47, 59, 71, 64]

puesto1 = Cola()
puesto2 = Cola()
puesto3 = Cola()
cantidad1  = [0, 0, 0, 0]
total1 = 0
total2 = 0
total3 = 0
cabina = 0

for i in range (30):
    arribo(puesto1, (choice(vehiculos)))
    arribo(puesto2, (choice(vehiculos)))
    arribo(puesto3, (choice(vehiculos)))

while(not cola_vacia(puesto1)):
    vehiculo = atencion(puesto1)
    pos = vehiculos.index(vehiculo)
    total1 += costo[pos]
    cantidad1[pos] += 1
    
    vehiculo = atencion(puesto2)
    pos = vehiculos.index(vehiculo)
    total2 += costo[pos]
    cantidad1[pos] += 1

    vehiculo = atencion(puesto3)
    pos = vehiculos.index(vehiculo)
    total3 += costo[pos]
    cantidad1[pos] += 1

total = 0
if total1 > total:
    total = total1
    cabina = 1
if total2 > total:
    total = total2
    cabina = 2
if total3 > total:
    total = total3
    cabina = 3
print('Vehiculos: Auto|Camioneta|Camion|Bus')
print('Cantidad de vehículos atendidos:', cantidad1)
print('El total es de:', total, 'y corresponde a la cabina:', cabina)
'''