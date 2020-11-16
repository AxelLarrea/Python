from Grafos import Grafo, insertar_vertice, buscar_vertice, insertar_arista, barrido_vertices, adyacentes, existe_paso
from Grafos import dijkstra, prim
from Arbol_Binario_AVL import eliminar_nodo, inorden, insertar_nodo, padre, busqueda, remplazar, por_nivel
from Pila_Dinamico import desapilar, pila_vacia
from Heap import Heap, heap_lleno, heap_vacio, arribo, atencion
from random import randint

#Ejercicios

#1 Arbol binario

arbol = None
personajes = ['Yoda', 'Obi-Wan Kenobi', 'C-3PO', 'Dar Vader']

#Punto 1
for i in range(0, len(personajes)):
    if arbol is None:
        arbol = insertar_nodo(arbol, personajes[i], randint(0, 500))
    else:
        x = busqueda(arbol, personajes[i])
        if x is None:
            arbol = insertar_nodo(arbol, personajes[i], randint(0, 500))


#Punto 2
print('Listado de manera ascendente: ')
inorden(arbol)
print()

#Punto 3
x = busqueda(arbol, 'Yoda')
if x is not None:
    print(x.info, x.nrr)
print()

#Punto 4
print('Listado por nivel:')
por_nivel(arbol)
x = busqueda(arbol, 'Obi-Wan Kenobi')
if x is not None:
    print('Nivel en el que se encuentra Obi-Wan:', x.altura - 1)
print()

#Punto 5
x = eliminar_nodo(arbol, 'C-3PO')
if x is not None:
    print('C-3PO ha sido eliminado correctamente')
else:
    print('C-3PO no ha sido eliminado')
print()

#Punto 6
x = busqueda(arbol, 'Dar Vader')
if x is not None:
    x.info = 'Darth Vader'
print('Darth Vader ha sido modificado')
print()

#2 Heap

#Punto 1, 2 y 3
cola = Heap(10)
names = [['MARK XL', 'Reparar'], ['MARK L', 'Reparar'], ['MARK XX', 'Producir'], ['MARK MCC', 'Reparar'], ['MARK CLV', 'Producir'], ['MARK CMC', 'Reparar'], ['MARK CXX', 'Producir'], ['MARK MMXL', 'Producir']]

for i in range(0, 7):
    arribo(cola, names[i], randint(1, 3))

#Punto 4
for i in range(0, 3):
    print(atencion(cola))

arribo(cola, ['MARK XLV', 'Reparar'], 3)
arribo(cola, ['(MARK XXL,', 'Producir'], 2)
arribo(cola, ['MARK III', 'Reparar'], 1)
print()

#Punto 5
for i in range(0, cola.tamanio):
    print(atencion(cola))
print()

#Ejercicio 3

g = Grafo(False)
personas = ['Juan', 'Pedro', 'Axel', 'Magali', 'Maria', 'Tom Holland', 'Robert Downey', 'Daisy Ridley', 'Pedro Pascal', 'Adam Driver']

#Punto 1 y 2
for i in range(0, len(personas)):
    insertar_vertice(g, personas[i])

ori = buscar_vertice(g, 'Juan')
des = buscar_vertice(g, 'Pedro')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Axel')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Daisy Ridley')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Pedro Pascal')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Adam Driver')
insertar_arista(g, randint(10, 120), ori, des)

ori = buscar_vertice(g, 'Tom Holland')
des = buscar_vertice(g, 'Robert Downey')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Axel')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Magali')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Daisy Ridley')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Pedro Pascal')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Adam Driver')
insertar_arista(g, randint(10, 120), ori, des)

ori = buscar_vertice(g, 'Maria')
des = buscar_vertice(g, 'Pedro')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Robert Downey')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Juan')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Daisy Ridley')
insertar_arista(g, randint(10, 120), ori, des)
des = buscar_vertice(g, 'Pedro Pascal')
insertar_arista(g, randint(10, 120), ori, des)

# barrido_vertices(g)

#Punto 3
bosque = prim(g)

print('Arbol de expansion minimo: ')
for i in range(0, len(bosque), 2):
    print(bosque[i], bosque[i+1])
print()

#Punto 4
ori = buscar_vertice(g, 'Guido Rossum')
des = buscar_vertice(g, 'Mark Hamill')
if ori is None or des is None:
    print('No es posible conectar a Guido y Mark')
else:
    x = existe_paso(g, ori, des)
    if x:
        print('Es posible conectar a Guido y Mark')
    else:
        print('No es posible conectar a Guido y Mark')
print()

ori = buscar_vertice(g, 'Tom Holland')

def adyacentes2(vertice):
    """Muestra los adyacents del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        if aux.destino == 'Robert Downey':
            print('Hay conexión directa entre Tom y Robert')
            break
        else:
            aux = aux.sig

adyacentes2(ori)
print()

#Punto 5
ori = buscar_vertice(g, 'Daisy Ridley')
adyacentes(ori)
print()

#Punto 6
caminito = dijkstra(g, 'Pedro Pascal', 'Adam Driver')
fin = 'Adam Driver'
peso_total = None
print('Camino más corto desde Pedro Pascal: ')
while(not pila_vacia(caminito)):
    dato = desapilar(caminito)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('El camino tiene un peso total de:', peso_total)
print()