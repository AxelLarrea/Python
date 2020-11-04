from Grafos import Grafo, grafo_vacio, insertar_vertice, buscar_vertice, insertar_arista, barrido_vertices, tamanio, adyacentes, existe_paso
from Heap import Heap, heap_vacio, arribo as arribo_h, atencion as atencion_h, buscar as buscar_h, cambiar_prioridad
from Pila_Dinamico import Pila, apilar, pila_vacia, desapilar
from math import inf



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

#barrido_vertices(g)

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


