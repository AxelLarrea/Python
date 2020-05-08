class nodoPila():
    """crea una variable nodo pila"""
    def __init__(self):
        self.info, self.sig = None, None


class Pila():
    """Crear una pila vacia"""
    def __init__(self):
        self.tamanio = 0
        self.cima = None


def apilar(pila, dato):
    """apila el dato en la cima"""
    nodo = nodoPila()
    nodo.info = dato 
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    dato = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    return pila.cima is None


def tamanio(pila):
    return pila.tamanio


def cima(pila):
    return pila.cima.info