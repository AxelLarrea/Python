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