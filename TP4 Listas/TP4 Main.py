from Listas_de_listas import busqueda, barrido, tamanio, lista_vacia
from Listas_de_listas import Lista, barrido_con_sublista, nodoLista, insertar, eliminar
from random import randint
'''
#Ejercicio 1

lista = Lista()

while (tamanio(lista) < randint(0, 20)):
    dato = randint(0, 99)
    insertar(lista, dato)

barrido(lista)
print()
print('La cantidad de elementos de la lista es:', tamanio(lista))

#Ejercicio 2

lista = Lista()

while (tamanio(lista) < 20):
    dato = randint(97, 122)
    insertar(lista, chr(dato))

print('Datos de la lista:')
barrido(lista)
print()

dato = eliminar(lista, 'a')
while(dato is not None):
    dato = eliminar(lista, 'a')

dato = eliminar(lista, 'e')
while(dato is not None):
    dato = eliminar(lista, 'e')

dato = eliminar(lista, 'i')
while(dato is not None):
    dato = eliminar(lista, 'i')

dato = eliminar(lista, 'o')
while(dato is not None):
    dato = eliminar(lista, 'o')

dato = eliminar(lista, 'u')
while(dato is not None):
    dato = eliminar(lista, 'u')

print('Datos de la lista sin vocales:')
barrido(lista)

#Ejercicio 3

lista = Lista()
lista_par = Lista()
lista_impar = Lista()

for i in range(10):
    insertar(lista, randint(0, 50))

print('Los datos de la lista son: ')
barrido(lista)

while not (lista_vacia(lista)):
    dato = eliminar(lista, lista.inicio.info)
    if(dato % 2 == 0):
        insertar(lista_par, dato)
    else:
        insertar(lista_impar, dato)
print()

aux = lista.inicio

while(aux is not None):
    if(aux.info % 2 == 0):
        insertar(lista_par, aux.info)
    else:
        insertar(lista_impar, aux.info)
    aux= aux.sig

print('Lista par: ')
barrido(lista_par)
print()
print('Lista impar: ')
barrido(lista_impar)

#Ejercicio 4

lista = Lista()

while (tamanio(lista) < 10):
    dato = randint(0, 99)
    insertar(lista, dato)

barrido(lista)
print('El tamaño de la lista es:', tamanio(lista))

pos = int(input(print('Posicion en la que insertar el nodo: ')))

nodito = nodoLista()
nodito.info = 2020
aux = lista.inicio
if (pos >= 0 and pos <= tamanio(lista)):
    if (pos < tamanio(lista)):
        for i in range(1, pos-1):
            aux = aux.sig
        nodito.sig = aux.sig
        aux.sig = nodito
    else:
        while (aux.sig is not None):
            aux = aux.sig
        aux.sig = nodito

barrido(lista)
print('El tamaño de la lista es:', tamanio(lista))

#Ejercicio 5

lista = Lista()

while (tamanio(lista) < 10):
    dato = randint(0,99)
    insertar(lista, dato)

barrido(lista)

aux = lista.inicio
cont = 0
while (aux is not None):
    x = aux.info
    for i in range(1, x):
        if (x % i  == 0):
            cont += 1
    if (cont < 3):
        eliminar(lista, x)
    aux = aux.sig
    cont = 0
print('Lista sin números primos: ')
barrido(lista)

#Ejercicio 6

lista = Lista()
dc = 0
marvel = 0

nombre = ['Linterna Verde', 'Wolverine', 'Dr. Strange', 'Capitana Marvel', 'Mujer Maravilla','Flash', 'Star-Lord', 'Iron-Man']
anio = ['1940', '1974', '1963', '1968', '1941', '1959', '1976','1963']
casa = ['DC', 'Marvel', 'DC', 'Marvel', 'DC', 'DC', 'Marvel','Marvel']
biografia = ['Caracterizado por su anillo de poder, posee la capacidad de crear manifestaciones de luz sólidad con solo pensarlo',
            'Su nombre es: James Logan, y sus característica son sus sentidos afinados, capacidad física mejorada y sus reconocibles garras',
            'Su nombre es: Stephen Strange, es el hechicero supremo, encargado de proteger la tierra de amenazas mágicas y místicas',
            'Su nombre es: Carol Danvers, es una superheroína la cual tiene genes Kree. Gracias a estos genes puede viajar a la velocidad de la luz y poseer un poder inmenso',
            'Princesa guerrera del Amazonas, conocida como Diana Prince, posee un Lazo de La Verdad, brazaletes mágicos irrompibles, además de poderes superhumanos y superiores habilidades de combate',
            'Posee supervelocidad en todos aspectos, tales como moverse y pensar, puede atravesar materia sólida y también posee reflejos superhumanos',
            'Su nombre es: Peter Quill, es conocido por su grupo Guardianes de las Galaxias',
            'Su nombre es: Tony Stark, es un excéntrico multillonario, filántropo y playboy. Posee una increíble armadura super resistente, equipada con armas y esta también le permite volar']

for i in range(0, len(anio)):
    insertar(lista, [nombre[i], anio[i], casa[i], biografia[i]])
barrido(lista)
print()

aux = lista.inicio
while (aux is not None):
    dato = aux.info
    #A : Borrar a Linterna Verde
    if (dato[0] == 'Linterna Verde'):
        print(dato[0],'ha sido eliminado')
        eliminar(lista, dato)
    #B : Mostrar año de aparicion de Wolverine
    if (dato[0] == 'Wolverine'):
        print('La fecha de aparición de', dato[0],'es:', dato[1])
    #C : Cambiar casa de Dr. Strange a Marvel
    if (dato[0] == 'Dr. Strange'):
        print('La casa de Dr. Strange es:', dato[2])
        dato[2] = 'Marvel'
        print('La casa a sido cambiada, ahora es:', dato[2])
    #D : Mostrar superhéroes que en su biografía tengan la palabra 'traje' o 'armadura'
    if (dato[3].find('traje') >= 0 or dato[3].find('armadura') >= 0):
        print('Este/a héroe/heroína posee traje o armadura:', dato[0])
    #E : Mostrar casa y nombre de héroes/heroínas cuya aparición sea anterior a 1963
    if (dato[1] < str(1963)):
        print('El/la héroe/heroína', dato[0], 'perteneciente a', dato[2],'apareció antes de 1963')
    #F : Mostrar casa a la que pertenecen Capitana Marvel y Mujer Maravilla
    if(dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla'):
        print(dato[0],'pertenece a', dato[2])
    #G : Mostrar info de Flash y Star-Lord
    if(dato[0] == 'Flash' or dato[0] == 'Star-Lord'):
        print('Biografía de:', dato[0], dato[3])
    #H : Listar superhéroes que comienzan con letra B,M y S
    if(dato[0][0] == 'B' or dato[0][0] == 'M' or dato[0][0] == 'S'):
        print('Este héroe comienza con B, M, o S:', dato[0])
    #I : Determinar cuantos superhéroes hay de cada casa de cómics
    if(dato[2] == 'DC'):
        dc += 1
    else:
        marvel += 1
    aux = aux.sig
print('Marvel tiene un total de', marvel,'héroes/heroínas')
print('DC tiene un total de', dc,'héroes/heroínas')

#Ejercicio 7

lista = Lista()
lista1 = Lista()
lista2 = Lista()
cont = 0

while (tamanio(lista) < 3):
    dato = randint(0, 5)
    insertar(lista, dato)
    insertar(lista2, dato)

while (tamanio(lista1) < 3):
    dato = randint(0, 5)
    insertar(lista1, dato)

print('Barrido lista 1: ')
barrido(lista)
print()

print('Barrido lista 2: ')
barrido(lista1)
print()

aux = lista.inicio
aux1 = lista1.inicio

#A: Concatenar dos listas, una tras la otra
while aux1 is not None:
    dato = aux1.info
    insertar(lista, dato)
    aux1 = aux1.sig
print('Listas concatenadas: ')
barrido(lista)
print()

#B: concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden
#C: contar cuántos elementos repetidos hay entre dos listas
aux1 = lista1.inicio
for i in range(0, tamanio(lista1)):
    dato = aux.info
    dato1 = aux1.info
    if(dato1 == dato):
        cont += 1
        eliminar(lista2, dato)
    else:
        insertar(lista2, dato1)
    aux = aux.sig
    aux1 = aux1.sig

print('Listas concatenadas sin elementos repetidos: ')
barrido(lista2)
print()
print('Hay un total de', cont,'elementos repetidos')
print()

#D: eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido
aux2 = lista2.inicio
while aux2 is not None:
    dato = aux2.info
    print('Contenido del nodo a eliminar:', dato)
    eliminar(lista2, dato)
    aux2 = aux2.sig

#Ejercicio 9

class Alumnos(object):
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' - ' + str(self.legajo)

class Parciales(object):
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha
    
    def __str__ (self):
        return self.materia + '' + str(self.nota)

lista = Lista()

for i in range(3):
    nombre = input('Ingrese nombre del alumno: ')
    apellido = input('Ingrese apellido del alumno: ')
    legajo = input('Ingrese legajo del alumno: ')
    alumno = Alumnos(nombre, apellido, legajo)
    insertar(lista, alumno,'apellido')
    print()

legajo = input('Ingrese legajo a buscar: ')
while legajo != '':
    pos = busqueda(lista, legajo, 'legajo')
    if pos is not None:
        materia = input('Ingrese materia del parcial: ')
        nota = int(input('Ingrese nota del parcial: '))
        fecha = input('Ingrese fecha del parcial: ')
        parcial = Parciales(materia, nota, fecha)
        insertar(pos.sublista, parcial, 'materia')
    else:
        print('No existe ese legajo')
    legajo = input('Ingrese legajo a buscar: ')

#A Mostrar alumnos ordenado por apellido
barrido(lista)

aux = lista.inicio
while aux is not None:
    parcial = aux.sublista.inicio
    promo = True
    promedio = 0
    while parcial is not None:
        if parcial.info.nota < 7:
            promo = False
        promedio += parcial.info.nota
        parcial = parcial.sig
    #B Indicar alumnos que no desaprobaron ningun parcial
    if promo == True:
        print('Alumno/a que no desaprobó ningún parcial:', aux.info)
    #E Mostrar promedio de cada alumno
    if tamanio(aux.sublista) > 0:
        prom = promedio/tamanio(aux.sublista)
        print('Promedio del alumno',aux.info,':', prom)
    #C Determinar alumnos con promedio mayor a 8.89
    if prom > 8.89:
        print('Este alumno posee un promedio mayor a 8.89:', aux.info)
    #D Mostrar toda la info de los alumnos con apellido comenzado en L
    if aux.info.apellido[0].upper() == 'L':
        print('Alumno cuyo apellido comienza con L:', aux.info)
    aux = aux.sig
    print()

#Ejercicio 10

top = ['Harry Styles - Watermelon Sugar','One Direction - You & I','Niall Horan - On The Loose','One Direction - History','One Direction - Little Things'
    ,'FKJ - Tadow','Calvin Harris - Under Control','Zomboy - Nuclear','Zayn - Dusk Till Dawn','Zayn - Like I Would','Liam Payne - Strip That Down'
    ,'One Direction - Cmon Cmon','One Direction - 18','Ed Sheeran - Perfect','Ed Sheeran - Thinking Out Loud','Harry Styles - Falling','Harry Styles - Sign Of The Time'
    ,'Niall Horan - Nice To Meet Ya','Logic - 1-800-2738255','Halsey - Sorry','Halsey - Without Me','NF - I You Want Love','David Guetta - Memories'
    ,'Skillet - Never Surrender','Skillet - One Day Too Late', 'Suicide Silence - You Only Live Once', 'Metallica - One','Iron Maiden - The Trooper'
    ,'Asking Alexandria - The Final Episode','Artic Monkeys - 505','Harry Styles - Lights Up','Robin Schulz - Ok','Robin Schulz - Show Me Love'
    ,'Jack & Jack - Groove','The Neighbourhood - Prey','The Neighbourhood - Sweater Weather','Vicentico - Creo Que Me Enamoré','Years & Years - Desire'
    ,'Years & Years - King','Linkin Park - Burn It Down']
class Canciones(object):
    def __init__(self, artista, nombre, duracion, reproducciones):
        self.artista = artista
        self.nombre = nombre
        self.duracion = duracion
        self.reproducciones = reproducciones
    
    def __str__(self):
        return self.artista + ' - ' + self.nombre + ', Duracion:' + self.duracion + ', Reproducciones:' + str(self.reproducciones)

lista = Lista()

for i in range(2):
    artista = input('Ingrese nombre del artista: ')
    nombre = input('Ingrese nombre de la cancion: ')
    duracion = input('Ingrese duracion de la cancion: ')
    reproducciones = randint(100000, 10000000)
    cancion = Canciones(artista, nombre, duracion, reproducciones)
    insertar(lista, cancion,'artista')
    print()

extensa = ''
aux = lista.inicio
while aux is not None:
    #A Cancion más extensa
    if aux.info.duracion > extensa:
        extensa = aux.info.duracion
        bio = aux.info
    #C Obtener canciones de banda Artic Monkeys
    if aux.info.artista == 'Artic Monkeys':
        print('Canciones de Artic Monkeys:', aux.info.nombre)
    #D Mostrar nombres de artistas con una sola palabra como nombre
    if len(aux.info.artista.split()) == 1:
        print('Este artista contiene una palabra como nombre:', aux.info.artista)
    aux = aux.sig
print()

print('Info de la cancion más extensa:', bio)
print()
#B Obtener top 5, top 10 y top 40
opcion = int(input('Ingrese una de las siguientes opciones: 1 = TOP 5, 2 = TOP10, 3 = TOP40, 0 = SALIR'))
while not opcion == 0:
    if opcion == 1:
        print('TOP 5')
        for i in range(0, 5):
            print(i+1,'-',top[i])
    if opcion == 2:
        print('TOP 10')
        for i in range(0, 10):
            print(i+1,'-',top[i])
    if opcion == 3:
        print('TOP 40')
        for i in range(0, 40):
            print(i+1,'-',top[i])
    opcion = int(input('Ingrese una de las siguientes opciones: 1 = TOP 5, 2 = TOP10, 3 = TOP40, 0 = SALIR'))
    '''