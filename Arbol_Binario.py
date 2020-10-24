from Cola_Dinamico import Cola, cola_vacia, arribo, atencion

class nodoArbol(object):

    def __init__(self, info, nrr = None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr


class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class nodoArbolGreek(object):
    
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion

class nodoArbolMarvel(object):

    def __init__(self, nombre, heroe):
        self.izq = None
        self.der = None
        self.nombre = nombre
        self.heroe = heroe


def insertar_nodo(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


from Archivos import leer

def inorden_lightsaber(raiz, archivo):
    if(raiz is not None):
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if(jedi[4].find('green') > -1):
            print(raiz.info, jedi[4])
        inorden_lightsaber(raiz.der, archivo)

def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


def busqueda(raiz, buscado):
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_nario(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.info == buscado):
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)

def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def insertar_nario(padre, hijo):
    if(padre.izq is None):
        #print('insertar hijo de', padre.info)
        padre.izq = hijo
    else:
        aux = padre.izq
        while(aux.der is not None):
            aux = aux.der
        #print('insertar hno de', aux.info)
        aux.der = hijo

def por_nivel_nario(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        hno = nodo.der
        while(hno is not None):
            print(hno.info)
            if(hno.izq is not None):
                arribo(cola, hno.izq)
            hno = hno.der
            
# arbol = None

# arbol = insertar_nodo(arbol, 5)
# arbol = insertar_nodo(arbol, 3)
# arbol = insertar_nodo(arbol, 4)
# arbol = insertar_nodo(arbol, 7)
# arbol = insertar_nodo(arbol, 9)
# arbol = insertar_nodo(arbol, 0)
# arbol = insertar_nodo(arbol, 1)
# arbol = insertar_nodo(arbol, 6)

# arbol = insertar_nodo(arbol, 7)
# arbol = insertar_nodo(arbol, 7)

# 3 5
# cantp, canti = 0, 0

def contar(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = contar(raiz.izq, cp, ci)
        cp, ci = contar(raiz.der, cp, ci)
    return cp, ci

# cantp, canti = contar(arbol, cantp, canti)
# print(cantp, canti)


def contar_repetidos(raiz, buscado, cant):
    if(raiz is not None):
        if(raiz.info == buscado):
            cant += 1
            cant = contar_repetidos(raiz.der, buscado, cant)
        else:
            cant = contar_repetidos(raiz.izq, buscado, cant)
    return cant

# cant = 0
# bus = 7
# pos = busqueda(arbol, bus)
# if(pos is not None):
#     print('asdas', contar_repetidos(pos, bus, cant))
# else:
#     print(0)



#arbol, dato = eliminar_nodo(arbol, 5)
# por_nivel(arbol)

# pos = busqueda(arbol, 20)
# if(pos is not None):
#     print(pos.info)
# else:
#     print(pos)

# from random import randint

# for i in range(0, 1000):
#     arbol = insertar_nodo(arbol, randint(0, 50000))

# print('barrido inorden')
# inorden(arbol)
# a = input()
# print('barrido preorden')
# preorden(arbol)
# a = input()
# print('barrido postorden')
# postorden(arbol)
# a = input()
# print('barrido por nivel')
# por_nivel(arbol)
# # a = input()

# buscado = int(input('ingrese valor buscado '))
# pos = busqueda(arbol, buscado)

# if(pos is not None):
#     print('esta')
# else:
#     print('no esta')