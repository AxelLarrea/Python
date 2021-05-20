from random import choice, randint
from Cola_Dinamico import Cola, cola_vacia, arribo, atencion, tamanio
from Pila_Dinamico import Pila, pila_vacia, apilar, desapilar, tamanio
from Listas import Lista, tamanio, insertar, busqueda, barrido

#1 Recursividad

objetos =['sable de luz','casco','pistola','vendas','herramientas']

mochila = [0]*5

for i in range(5):
    mochila[i] = choice(objetos)

indice = 0

def Usar_la_fuerza(mochila, indice):
    if mochila[indice] == 'sable de luz':
        return print('Sable de luz encontrado, se encuentra en la posicion', indice)
    elif mochila[indice] != 'sable de luz':
        print(mochila[indice],'encontrado')
        return Usar_la_fuerza(mochila, indice+1)

Usar_la_fuerza(mochila, indice)

#2 Cola

class Noti(object):
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje
    
app = ['Facebook','Whatsapp','Twitter','Instagram']
msj = ['Python','Hola','Que tal todo?']
cola = Cola()
cola2 = Cola()
pila = Pila()

while tamanio(cola) < 5:
    hora = randint(0000,2359)
    aplicacion = choice(app)
    mensaje = choice(msj)
    noti = Noti(hora, aplicacion, mensaje)
    arribo(cola, noti)

while not cola_vacia(cola):
    x = atencion(cola)
    #A
    if x.aplicacion == 'Facebook':
        print('Notificacion de Facebook eliminada')
    #B
    if x.aplicacion == 'Twitter' and x.mensaje == 'Python':
        print(x.mensaje)
        arribo(cola2, x)
    #C
    if x.aplicacion == 'Instagram':
        apilar(pila, x)

#3 Pila

class Trajes(object):
    def __init__(self, modelo, estado, pelicula):
        self.modelo = modelo
        self.estado = estado
        self.pelicula = pelicula

pila = Pila()
pila2 = Pila()

mod = ['Spider-Man','Mark XLIV','Prototipo','Avanzado','']
est = ['Dañado','Impecable','Destruido']
peli = ['Iron-Man','Iron-Man 2','Iron-Man 3','Avengers','Avengers : Infinity War', 'Avengers : End Game']

while tamanio(pila) < 5:
    modelo = choice(mod)
    estado = choice(est)
    pelicula = choice(peli)
    traje = Trajes(modelo, estado, pelicula)
    apilar(pila, traje)

while not pila_vacia(pila):
    x = desapilar(pila)
    #A
    if x.modelo == 'Mark XLIV':
        print('Fue utilizado en la película:', x.pelicula)
    #B
    if x.estado == 'Dañado':
        print('Este modelo está dañado:', x.modelo)
        apilar(pila2, x)
    #C
    if x.estado == 'Impecable':
        print('Este modelo será eliminado:', x.modelo)
    #D
    if x.pelicula == 'Avengers : End Game':
        print('Traje utilizado en Avengers : End Game', x.modelo)


#4

heroes = ['Thor','Spider-Man','Iron-Man','Hulk','Scalet Witch','Loki']

lista = Lista()
lista1 = Lista()
lista2 = Lista()
state = False

insertar(lista, 'Thor','')
insertar(lista, 'Spider-Man','')
insertar(lista, 'Iron-Man','')
insertar(lista, 'Hulk','')
insertar(lista, 'Scalet Witch','')
insertar(lista, 'Loki','')

insertar(lista2, 'Black Widow','')
insertar(lista2, 'Hulk','')
insertar(lista2, 'Rocket Racoonn','')
insertar(lista2, 'Loki','')

aux = lista.inicio
aux1 = lista.inicio
aux2 = lista2.inicio
pos = busqueda(lista, 'Thor','')

for i in range (0, tamanio(lista)):
    dato = aux.info
    #A
    if pos.info == dato:
        print('Thor está en la posición', i)
    #B
    if dato == 'Scalet Witch':
        dato = 'Scarlet Witch'
        print('Nombre corregido, ahora es:', dato)
    aux = aux.sig
#C
for i in range(0, tamanio(lista2)):
    dato2 = aux2.info
    for j in range(0, tamanio(lista)):
        dato = aux1.info
        if dato2 == dato:
            state = True
        aux1 = aux1.sig
    if state == False:
        insertar(lista, dato2)

barrido(lista)

#5
#La notación O sirve para determinar el rendimiento del programa en base a lo que demora en procesarlo.
#El orden de complejidad de la busqueda secuencial es O(n), debido a que depende de la cantidad de elementos del array, ya que debe ir comparando.
