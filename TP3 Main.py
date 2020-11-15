from Cola_Dinamico import Cola, arribo, atencion, cola_vacia, tamanio, en_frente, mover_final
from Pila_Dinamico import Pila, pila_vacia, desapilar, apilar, cima, tamanio as tamanio_p
from Heap import Heap, arribo as arribo_h, atencion as atencion_h, buscar, cambiar_prioridad
from random import randint, choice
from time import sleep
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



#Ejercicio 14

cola = Cola()
bases = [['Pry', 30, 50, 47], ['Star', 57, 32, 20], ['Lion', 81, 113, 65]]
r = 6371000
cercana = 0
flota = 0
name = ''
pila = Pila()

def haversine(r, q1, q2, d1, d2):
    return 2*r*asin(sqrt(sin((q2-q1)/2)**2 + cos(q1)*cos(q2) * sin((d2-d1)/2)**2))

for i in range(0, 3):
    arribo(cola, bases[i])

print('Ahora deberá ingresar su posición actual')
q1 = int(input('Ingrese la latitud: '))
d1 = int(input('Ingrese la longitud: '))

while not cola_vacia(cola):
    x = atencion(cola)

    #A,B Determinar base más cercana
    data = haversine(r, radians(q1), radians(x[2]), radians(d1), radians(x[3]))
    if cercana == 0:
        cercana = data
        name = x[0]
    elif data < cercana:
        cercana = data
        name = x[0]

    #C Tres bases más cercanas
    apilar(pila, [x[0], round(data, 0), x[1]])

    #D Determinar la distancia hacia la base con mayor flota
    if x[1] > flota:
        flota = x[1]
        distancia = data

#C Treas bases más cercanas y base con mayor flota aérea de las tres

mayor_flota = 0
basesita = ''

Paux = Pila()
while not pila_vacia(pila):
    c = 0
    dato = desapilar(pila)
    while not pila_vacia(Paux) and cima(Paux)[1] >= dato[1]:
        apilar(pila, desapilar(Paux))
        c += 1
    apilar(Paux, dato)
    for i in range(0, c):
        apilar(Paux, desapilar(pila))

for i in range(0, 3):
    x = desapilar(Paux)
    if x[2] > mayor_flota:
        mayor_flota = x[2]
        basesita = x[0]
    apilar(pila, x)

print('La base más cercana llamada', name, 'está a:', round(cercana, 0),'Km de distancia')
print('Distancia a la base con mayor flota aerea:', round(distancia, 0),'Km de distancia')
print('Las tres bases más cercanas son: ')
print('|Nombre|Distancia|Flota|')
while not pila_vacia(pila):
    print(desapilar(pila))
print('La base con mayor flota aérea de las tres más cercanas es:', basesita, 'con', mayor_flota, 'unidades')



#Ejercicio 15

cola = Heap(10)

#A Cargar tres documentos de Empleados.
names = ['Random', 'Avengers', 'Sumi']

for i in range(0, 3):
    arribo_h(cola, names[i], 1)

#B Imprimir el nombre del primer documento.
x = atencion_h(cola)
print('Nombre del primer documento:', x[1])
arribo_h(cola, x[1], x[0])
print()

#C Cargar dos documentos de Staff TI.
arribo_h(cola, 'Zero Two', 2)
arribo_h(cola, 'Oregairu', 2)

#D Cargar un documento de Gerente
arribo_h(cola, 'Que se termine el año pls', 3)

#E Imprimir los dos primeros documentos.
print('Primeros dos documentos: ')
for i in range(0, 2):
    x = atencion_h(cola)
    print(x)
    arribo_h(cola, x[1], x[0])
print()

#F Cargue dos documentos de empleados y uno de gerente.
arribo_h(cola, 'Hiro', 1)
arribo_h(cola, 'Primm', 1)
arribo_h(cola, 'Coldplay', 3)

#G Imprimir todos los documentos
print('|Prioridad|Nombre|')
while not cola_vacia(cola):
    print(atencion_h(cola))



#Ejercicio 16
cola = Cola()

arribo(cola, [1, 10])
arribo(cola, [2, 3])
arribo(cola, [4, 5])
while not cola_vacia(cola):
    dato = atencion(cola)
    
    #A Atender procesos
    print('Atendiendo proceso:', dato[0])
    
    #B Si el proceso no terminó su ejecución debe volver a la cola
    if(dato[1] > 4.5):
        dato[1] = dato[1] - 4.5
        sleep(4.5)
        arribo(cola, dato)
    else:
        sleep(dato[1])
    
    #C Agregar procesos
    resp = input('Quiere cargar proceso S/N?')
    if(resp.upper() == 'S'):
        tiempo = float(input('Ingrese tiempo del proceso: '))
        arribo(cola,[randint(1, 500), tiempo])



#Ejercicio 17

cola = Cola()
cola_1 = Cola()
cola_2 = Cola()
letras = ['A', 'B', 'C', 'D', 'E', 'F']
cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0
cont_e = 0
cont_f = 0

#A Cargar turnos de manera aleatoria
for i in range(1000):
    arribo(cola, [choice(letras), randint(000, 1000)])

#B Separar en dos colas, en la primera los que empiecen con A,C,F y en la otra con B,D,E
while not cola_vacia(cola):
    x = atencion(cola)
    if (x[0] == 'A') or (x[0] == 'C') or (x[0] == 'F'):
        arribo(cola_1, x)
    else:
        arribo(cola_2, x)

#C Determinar cuál cola tiene mayor cantidad de turnos y de esta determinar cuál letra tiene más cantidad
control = True
if tamanio(cola_1) > tamanio(cola_2):
    print('La cola 1 tiene mayor cantidad de turnos con:', tamanio(cola_1),'turnos')
    while not cola_vacia(cola_1):
        x = atencion(cola_1)
        if x[0] == 'A':
            cont_a += 1
        elif x[0] == 'C':
            cont_c += 1
        else:
            cont_f += 1
else:
    print('La cola 2 tiene mayor cantidad de turnos con:', tamanio(cola_2),'turnos')
    control = False
    while not cola_vacia(cola_2):
        x = atencion(cola_2)
        if x[0] == 'B':
            cont_b += 1
        elif x[0] == 'D':
            cont_d += 1
        else:
            cont_e += 1

if control:
    if cont_a > cont_c and cont_a > cont_f:
        print('La letra A tiene asignado la mayor cantidad de turnos con:', cont_a)
    elif cont_c > cont_a and cont_c > cont_f:
        print('La letra C tiene asignado la mayor cantidad de turnos con:', cont_c)
    else:
        print('La letra F tiene asignado la mayor cantidad de turnos con:', cont_f)
else:
    if cont_b > cont_d and cont_b > cont_e:
        print('La letra B tiene asignado la mayor cantidad de turnos con:', cont_b)
    elif cont_d > cont_b and cont_d > cont_e:
        print('La letra D tiene asignado la mayor cantidad de turnos con:', cont_d)
    else:
        print('La letra E tiene asignado la mayor cantidad de turnos con:', cont_e)

#D Mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.
if control:
    while not cola_vacia(cola_2):
        x = atencion(cola_2)
        if x[1] > 506:
            print(x)
else:
    while not cola_vacia(cola_1):
        x = atencion(cola_1)
        if x[1] > 506:
            print(x)



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



#Ejercicio 20

tipos_aviones = ['Carga', 'Negocios', 'Pasajeros']
origen = ['Argentina', 'Estados Unidos', 'Brasil']
destino = ['Irlanda', 'Inglaterra', 'España', 'India', 'Rusia']
empresa = ['American Airlines', 'Aerolíneas Argentinas', 'LATAM Airlines', 'British Airways', 'Sky Airline']
horas = ['07:00', '08:30', '01:45', '17:20']
tiempo_despegue = [9, 3, 5]
tiempo_aterrizaje = [12, 5, 10]
cola_despegue = Cola()
cola_aterrizaje = Cola()
hora_actual = '16:40'

for i in range(10):
    arribo(cola_despegue, [choice(empresa), choice(origen), choice(destino), choice(tipos_aviones), choice(horas), choice(horas)])
    arribo(cola_aterrizaje, [choice(empresa), choice(origen), choice(destino), choice(tipos_aviones), choice(horas), choice(horas)])

while(not cola_vacia(cola_despegue) or not cola_vacia(cola_aterrizaje)):
    hora_despegue = en_frente(cola_despegue)[4]
    if(not cola_vacia(cola_aterrizaje) and hora_despegue <= hora_actual):
        avion = atencion(cola_aterrizaje)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_aterrizaje[pos]
        print('Avion de la empresa', avion[0],'aterrizando')
        sleep(tiempo)
    else:
        avion = atencion(cola_despegue)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_despegue[pos]
        print('Avion de la empresa', avion[0],'despegando')
        sleep(tiempo)


'''