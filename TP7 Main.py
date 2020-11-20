from Grafos import Grafo, grafo_vacio, insertar_vertice, buscar_vertice, insertar_arista, barrido_vertices, tamanio, adyacentes, existe_paso
from Grafos import barrido_amplitud, barrido_profundidad, marcar_no_visitado, dijkstra, prim, eliminar_arista
from Heap import Heap, heap_vacio, arribo as arribo_h, atencion as atencion_h, buscar as buscar_h, cambiar_prioridad
from Pila_Dinamico import Pila, apilar, pila_vacia, desapilar
from math import inf
from random import randint


'''
#Ejercicio 1

g = Grafo(False)

insertar_vertice(g, 'Argentina', [" S34°0'0'' O64°0'0'' ",'17'])
insertar_vertice(g, 'Alemania', [" N10°3'0'' E45°0'0'' ", '12'])
insertar_vertice(g, 'Brasil', [" S10°3'0'' O55°0'0'' ", '22'])
insertar_vertice(g, 'China', [" S54°3'0'' E33°0'0'' ", '43'])
insertar_vertice(g, 'Estados Unidos', [" S10°3'32'' E55°11'0'' ", '52'])
insertar_vertice(g, 'Francia', [" N10°3'0'' E12°0'0'' ", '11'])
insertar_vertice(g, 'Grecia', [" N21°3'0'' E07°30'0'' ", '11'])
insertar_vertice(g, 'Japón', [" N04°32'0'' E13°40'0'' ", '30'])
insertar_vertice(g, 'Jamaica', [" S01°3'30'' O35°0'0'' ", '20'])
insertar_vertice(g, 'Tailandia', [" S00°39'45'' E57°0'0'' ", '31'])


ori = buscar_vertice(g, 'Argentina')
des = buscar_vertice(g, 'Brasil')
insertar_arista(g, ['12:30 hs', '14:30 hs', 'Aerolíneas Argentinas', '$10000', 2, 1700], ori, des)
des = buscar_vertice(g, 'Estados Unidos')
insertar_arista(g, ['7:30 hs', '14:30 hs', 'American Airlines', '$10000', 7, 7400], ori, des)
des = buscar_vertice(g, 'Japón')
insertar_arista(g, ['5:00 hs', '10:00 hs', 'アクセル', '$10000', 5, 3800], ori, des)

ori = buscar_vertice(g, 'Alemania')
des = buscar_vertice(g, 'Estados Unidos')
insertar_arista(g, ['15:00 hs', '20:00 hs', 'Deutsch Airlines', '$10000', 5, 5900], ori, des)
des = buscar_vertice(g, 'Grecia')
insertar_arista(g, ['4:45 hs', '8:45 hs', 'Deutsch Airlines', '$10000', 4, 3500], ori, des)
des = buscar_vertice(g, 'Francia')
insertar_arista(g, ['6:00 hs', '7:00 hs', 'Deutsch Airlines', '$10000', 1, 900], ori, des)

ori = buscar_vertice(g, 'Brasil')
des = buscar_vertice(g, 'Jamaica')
insertar_arista(g, ['11:00 hs', '16:00 hs', 'Brasilia Airlines', '$10000', 5, 5000], ori, des)
des = buscar_vertice(g, 'Estados Unidos')
insertar_arista(g, ['10:00 hs', '16:00 hs', 'American Airlines', '$10000', 6, 6000], ori, des)

ori = buscar_vertice(g, 'Grecia')
des = buscar_vertice(g, 'Tailandia')
insertar_arista(g, ['19:00 hs', '21:00 hs', 'Greek Airlines', '$10000', 2, 2000], ori, des)
des = buscar_vertice(g, 'Francia')
insertar_arista(g, ['21:00 hs', '00:00 hs', 'French Airlines', '$10000', 3, 3200], ori, des)
des = buscar_vertice(g, 'China')
insertar_arista(g, ['23:00 hs', '04:00 hs', 'Chinese Airlines', '$10000', 5, 4700], ori, des)

barrido_vertices(g)


#E calcular el camino más corto desde el aeropuerto de Argentina a Tailandia considerando los siguientes criterios:


#1- menor distancia.

def dijkstra_distancia(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info[5]):
                no_visitados.vector[pos][1][1] = dato[1][0].info[5]
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info[5])
            aux = aux.sig
    return camino


camino_mas_corto = dijkstra_distancia(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(camino_mas_corto)):
    dato = desapilar(camino_mas_corto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        # print(dato[1][0].info)
        fin = dato[1][1]
print('Menor distancia posible a recorrer:', peso_total, 'Km')
print()


#2- menor duración de tiempo

def dijkstra_duracion(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info[4]):
                no_visitados.vector[pos][1][1] = dato[1][0].info[4]
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info[4])
            aux = aux.sig
    return camino


camino_mas_corto = dijkstra_duracion(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(camino_mas_corto)):
    dato = desapilar(camino_mas_corto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        # print(dato[1][0].info)
        fin = dato[1][1]
print('Menor tiempo posible de viaje:', peso_total, 'hs')
print()

#3- determinar todos los aeropuertos a los que se puede arribar desde Grecia de manera directa o indirecta.

print('Países desde los cuales se puede ir directamente desde Grecia: ')
print()

ori = buscar_vertice(g, 'Grecia')
adyacentes(ori)
print()

print('Países desde los cuales se puede ir indirectamente desde Grecia: ')
print()

lista = ['Argentina', 'Alemania', 'Brasil', 'China', 'Estados Unidos', 'Francia', 'Japón', 'Jamaica', 'Tailandia']

for elemento in lista:
    des = buscar_vertice(g, elemento)
    if existe_paso(g, ori, des):
        pilita = dijkstra_duracion(g, ori, des)
        while not pila_vacia(pilita):
            x = desapilar(pilita)
            print(x[1][0].info, x[1][0].adyacentes.inicio.info)



#Ejercicio 2

#H Utilizar grafo no dirigido.

g = Grafo(False)

#A Cada nodo tiene el nombre y el tipo.

insertar_vertice(g, 'Ubuntu', 'PC')
insertar_vertice(g, 'Debian', 'Notebook')
insertar_vertice(g, 'Switch 1', 'Switch')
insertar_vertice(g, 'Impresora', 'Impresora')
insertar_vertice(g, 'Mint', 'PC')
insertar_vertice(g, 'Router 1', 'Router')
insertar_vertice(g, 'Router 2', 'Router')
insertar_vertice(g, 'Router 3', 'Router')
insertar_vertice(g, 'Red Hat', 'Notebook')
insertar_vertice(g, 'Guarani', 'Servidor')
insertar_vertice(g, 'Switch 2', 'Switch')
insertar_vertice(g, 'Manjaro', 'PC')
insertar_vertice(g, 'Parrot', 'PC')
insertar_vertice(g, 'Fedora', 'PC')
insertar_vertice(g, 'Arch', 'Notebook')
insertar_vertice(g, 'MongoDB', 'Servidor')

# print('Listado de vértices')
# barrido_vertices(g)
# print()

#Carga de aristas desde Switch 1
ori = buscar_vertice(g, 'Switch 1')
des = buscar_vertice(g, 'Debian')
insertar_arista(g, 17, ori, des)
des = buscar_vertice(g, 'Ubuntu')
insertar_arista(g, 18, ori, des)
des = buscar_vertice(g, 'Impresora')
insertar_arista(g, 22, ori, des)
des = buscar_vertice(g, 'Mint')
insertar_arista(g, 80, ori, des)
des = buscar_vertice(g, 'Router 1')
insertar_arista(g, 29, ori, des)

#Carga de aristas desde Router 1
ori = buscar_vertice(g, 'Router 1')
des = buscar_vertice(g, 'Router 2')
insertar_arista(g, 37, ori, des)
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 43, ori, des)

#Carga de aristas desde Router 2
ori = buscar_vertice(g, 'Router 2')
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 50, ori, des)
des = buscar_vertice(g, 'Red Hat')
insertar_arista(g, 25, ori, des)
des = buscar_vertice(g, 'Guarani')
insertar_arista(g, 9, ori, des)

#Carga de aristas desde Switch 2
ori = buscar_vertice(g, 'Switch 2')
des = buscar_vertice(g, 'Router 3')
insertar_arista(g, 61, ori, des)
des = buscar_vertice(g, 'Manjaro')
insertar_arista(g, 40, ori, des)
des = buscar_vertice(g, 'Parrot')
insertar_arista(g, 12, ori, des)
des = buscar_vertice(g, 'MongoDB')
insertar_arista(g, 5, ori, des)
des = buscar_vertice(g, 'Arch')
insertar_arista(g, 56, ori, des)
des = buscar_vertice(g, 'Fedora')
insertar_arista(g, 3, ori, des)

# print('Listado de vértices y aristas')
# barrido_vertices(g)
# print()

#B Realizar barrido en profundidad y amplitud desde las tres netbooks

print('Barrido en profundidad desde Debian: ')

ori = buscar_vertice(g, 'Debian')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en profundidad desde Red Hat: ')

ori = buscar_vertice(g, 'Red Hat')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en profundidad desde Arch: ')

ori = buscar_vertice(g, 'Arch')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

#C Encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora.

caminito = dijkstra(g, 'Manjaro', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Manjaro: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)

caminito = dijkstra(g, 'Red Hat', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Red Hat: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)

caminito = dijkstra(g, 'Fedora', 'Impresora')
fin = 'Impresora'
peso_total = None
print('Camino más corto desde Fedora: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()
marcar_no_visitado(g)

#D Encontrar el árbol de expansión mínimo

print('Árbol de expansión mínimo: ')
bosque = prim(g)

for i in range(0, len(bosque), 2):
    print(bosque[i], bosque[i+1])
print()

#E Determinar desde que PC es el camino más corto hasta el sv Guaraní

min = []

# Dijkstra Parrot
caminito = dijkstra(g, 'Parrot', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
min = ['Parrot', peso_total] 
marcar_no_visitado(g)

# Dijkstra Manjaro
caminito = dijkstra(g, 'Manjaro', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Manjaro', peso_total]
marcar_no_visitado(g)

# Dijkstra Fedora
caminito = dijkstra(g, 'Fedora', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Fedora', peso_total]
marcar_no_visitado(g)

# Dijkstra Mint
caminito = dijkstra(g, 'Mint', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Mint', peso_total]
marcar_no_visitado(g)

# Dijkstra Ubuntu
caminito = dijkstra(g, 'Ubuntu', 'Guarani')
fin = 'Guarani'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < min[1]):
    min = ['Ubuntu', peso_total]
marcar_no_visitado(g)

print('La PC con el camino más corto hasta el server Guaraní es:', min[0], 'con un peso de', min[1])
print()

#F Indicar que computadora del Switch 1 es el camino más corto hasta el sv MongoDB

mini = []

# Dijkstra Ubuntu
caminito = dijkstra(g, 'Ubuntu', 'MongoDB')
fin = 'MongoDB'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
mini = ['Ubuntu', peso_total]
marcar_no_visitado(g)

# Dijkstra Mint
caminito = dijkstra(g, 'Mint', 'MongoDB')
fin = 'MongoDB'
peso_total = None
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        fin = dato[1][1]
if (peso_total < mini[1]):
    mini = ['Mint', peso_total]
marcar_no_visitado(g)

print('La PC con el camino más corto hasta el server MongoDB es:', mini[0], 'con un peso de', mini[1])
print()

#G Cambiar la conexión de la impresora el Router 2 y resolver el punto B nuevamente


ori = buscar_vertice(g, 'Impresora')
des = buscar_vertice(g, 'Switch 1')
eliminar_arista(g, ori, 'Switch 1')
# barrido_vertices(g)
print()
des = buscar_vertice(g, 'Router 2')
insertar_arista(g, 50, ori, des)
# barrido_vertices(g)

print('Barrido en profundidad desde Debian: ')

ori = buscar_vertice(g, 'Debian')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Debian: ')
ori = buscar_vertice(g, 'Debian')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en profundidad desde Red Hat: ')

ori = buscar_vertice(g, 'Red Hat')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Red Hat: ')
ori = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en profundidad desde Arch: ')

ori = buscar_vertice(g, 'Arch')
barrido_profundidad(g, ori)
print()
marcar_no_visitado(g)

print('Barrido en amplitud desde Arch: ')
ori = buscar_vertice(g, 'Arch')
barrido_amplitud(g, ori)
print()
marcar_no_visitado(g)

'''
#Ejercicio 3

#F Utilizar grafo no dirigido
g = Grafo(False)

#A Nombre, país de ubicación y tipo de maravilla

#Maravillas Modernas
insertar_vertice(g, 'Ciudad de Petra', ['Jordania','Arquitectonica'])
insertar_vertice(g, 'Taj Mahal', ['India', 'Arquitectonica'])
insertar_vertice(g, 'Machu Picchu', ['Peru', 'Arquitectonica'])
insertar_vertice(g, 'Chichen Itza', ['Mexico', 'Arquitectonica'])
insertar_vertice(g, 'Coliseo', ['Roma', 'Arquitectonica'])
insertar_vertice(g, 'Gran Muralla', ['China', 'Arquitectonica'])
insertar_vertice(g, 'Cristo Redentor', ['Brasil', 'Arquitectonica'])

#Maravillas Naturales
insertar_vertice(g, 'Bahía de Ha Long', ['Vietnam', 'Naturales'])
insertar_vertice(g, 'Isla de Komodo', ['Indonesia', 'Naturales'])
insertar_vertice(g, 'Río subterráneo de Puerto Princesa', ['Filipinas', 'Naturales'])
insertar_vertice(g, 'Montaña de la Mesa', ['Sudáfrica', 'Naturales'])
insertar_vertice(g, 'Cataratas del Iguazú', [['Argentina', 'Brasil'], 'Naturales'])
insertar_vertice(g, 'Río Amazonas', [['Perú', 'Colombia', 'Brasil'], 'Naturales'])
insertar_vertice(g, '2 Islas Jeju', ['Corea del Sur', 'Naturales'])

barrido_vertices(g)

#B Cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa

#Carga de Maravillas Arquitectónicas
ori = buscar_vertice(g, 'Ciudad de Petra')
des = buscar_vertice(g, 'Taj Mahal')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Machu Picchu')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Taj Mahal')
des = buscar_vertice(g, 'Machu Picchu')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Machu Picchu')
des = buscar_vertice(g, 'Chichen Itza')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Chichen Itza')
des = buscar_vertice(g, 'Coliseo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Coliseo')
des = buscar_vertice(g, 'Gran Muralla')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Gran Muralla')
des = buscar_vertice(g, 'Cristo Redentor')
insertar_arista(g, randint(1000, 8000), ori, des)


#Carga de Maravillas Naturales
ori = buscar_vertice(g, 'Bahía de Ha Long')
des = buscar_vertice(g, 'Isla de Komodo')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Isla de Komodo')
des = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Río subterráneo de Puerto Princesa')
des = buscar_vertice(g, 'Montaña de la Mesa')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Montaña de la Mesa')
des = buscar_vertice(g, 'Cataratas del Iguazú')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Cataratas del Iguazú')
des = buscar_vertice(g, 'Río Amazonas')
insertar_arista(g, randint(1000, 8000), ori, des)
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)

ori = buscar_vertice(g, 'Río Amazonas')
des = buscar_vertice(g, '2 Islas Jeju')
insertar_arista(g, randint(1000, 8000), ori, des)


#C Hallar el árbol de expansión mínimo de cada tipo de las maravillas
bosque = prim(g)

print('Arbol de expansion minimo: ')
for i in range(0, len(bosque), 2):
    print(bosque[i], bosque[i+1])
print()


#D determinar si existen países que dispongan de maravillas arquitectónicas y naturales