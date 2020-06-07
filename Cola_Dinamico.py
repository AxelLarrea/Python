
class nodoCola(object):
    """crea una variable nodo cola"""
    def __init__(self):
        self.info, self.sig = None, None

class Cola(object):
    """TDA cola """

    def __init__(self):
        self.frente, self.final, self.tamanio = None, None, 0


def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if(cola.final is None):
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    aux = cola.frente.info
    cola.frente = cola.frente.sig
    if(cola.frente is None):
        cola.final = None
    cola.tamanio -= 1
    return aux


def cola_vacia(cola):
    return cola.tamanio == 0


def tamanio(cola):
    return cola.tamanio

def en_frente(cola):
    return cola.frente.info

def mover_final(cola):
    x = atencion(cola)
    arribo(cola, x)
    return x


'''
c = Cola()
caux = Cola()
while tamanio(c)<10:
    dato = int(input("ingrese un número"))
    if(cola_vacia(c)):
        arribo(c, dato)
    elif(dato<en_frente(c)):
        arribo(c, dato)
        for i in range (1, tamanio(c)):
            mover_final(c)
    else:
        cont = 0
        while(en_frente(c)< dato and cont<tamanio(c)):
            mover_final(c)
            cont += 1
        arribo(c, dato)
        for i in range(cont, tamanio(c)-1):
            mover_final(c)
    
print('barrido')
for i in range(0, tamanio(c)):
    print(mover_final(c))
'''
'''
while tamanio(c)<10:
    dato = int(input("ingrese un número"))
    arribo(c, dato)
num = int(input('ingrese la posicion del elemento que desea eliminar '))
if(num<tamanio(c)):
    for i in range(0, tamanio(c)):
        if(i == num-1):
            dato = atencion(c)
            print(dato)
        else:
            mover_final(c)
print('barrido')
for i in range(0, tamanio(c)):
    print(mover_final(c))
'''

'''
while not cola_vacia(c):
    x = atencion(c)
    arribo(caux, x)
    print(x)
while not cola_vacia(caux):
    x = atencion(caux)
    arribo(c, x)
for i in range(0, tamanio(c)):
    print(mover_final(c))
print("fin del barrido")
print(tamanio(c))
'''