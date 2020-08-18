class nodoArbol(object):

    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertar_nodo(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def postorden(raiz):
    if(raiz is not None):
        inorden(raiz.der)
        print(raiz.info)
        inorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def busqueda(raiz, buscado):
    if(raiz is not None):
        print(raiz.info)
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

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

arbol = None

arbol = insertar_nodo(arbol, 5)
arbol = insertar_nodo(arbol, 3)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 0)
arbol = insertar_nodo(arbol, 1)
arbol = insertar_nodo(arbol, 6)

arbol, dato = eliminar_nodo(arbol, 5)
preorden(arbol)

# pos = busqueda(arbol, 20)
# if(pos is not None):
#     print(pos.info)
# else:
#     print(pos)