from Listas import Lista, insertar, eliminar, busqueda, barrido, tamanio, lista_vacia, nodoLista
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
'''
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
