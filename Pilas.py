class Pila():
    #Crear una pila vacía
    def __init__(self):
        self.cima, self.datos = -1, [0] * 7

def Apilar(pila, datos):
    #Apila el dato en la cima
    pila.cima += 1
    pila.datos[pila.cima] = datos

def Desapilar(pila):
    datos = pila.datos[pila.cima]
    pila.cima -= 1
    return datos

def Pila_Vacia(pila):
    return pila.cima == -1

def Pila_Llena(pila):
    return pila.cima == len(pila.datos) -1

def tamanio(pila):
    return len(pila.datos)

def cima(pila):
    return pila.datos[pila.cima]

'''
pila = Pila()

Apilar(pila, 2)
Apilar(pila, 7)
Apilar(pila, 4)

print(Desapilar(pila))

print(pila.cima, pila.datos)
'''
