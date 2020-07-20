class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = Lista()


class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or criterio(lista.inicio.info,campo)>criterio(nodo.info,campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo)<criterio(nodo.info,campo)):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    


def eliminar(lista, clave, campo=None):
    dato = None
    if(criterio(lista.inicio.info,campo) == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo) != clave):
            act = act.sig
            ant = ant.sig
        
        if(act is not None):
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1

    return dato



def busqueda(lista, clave, campo=None):
    aux = lista.inicio
    while(aux is not None and criterio(aux.info, campo) != clave):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def barrido_con_sublista(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        barrido(aux.sublista)

        aux = aux.sig  

def tamanio(lista):
    return lista.tamanio


def lista_vacia(lista):
    return lista.inicio is None


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]


'''
class Alumno(object):

    def __init__(self, apellido, nombre, legajo):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo

    def __str__(self):
        return self.apellido + " " + self.nombre

class Parcial(object):

    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return self.materia + " " + self.nota


lista = Lista()

for i in range(3):
    apellido = input('ingrese apellido ')
    nombre = input('ingrese nombre ')
    legajo = input('ingrese legajo ')

    alumno = Alumno(apellido, nombre, legajo)
    insertar(lista, alumno, 'apellido')


legajo = input('ingrese legajo ')
while(legajo != ''):
    pos = busqueda(lista, legajo, 'legajo')
    if(pos is not None):
        materia = input('ingrese materia ')
        nota = int(input('ingrese nota'))
        fecha = ''#input('ingrese fecha')
        parcial = Parcial(materia, nota, fecha)
        insertar(pos.sublista, parcial, 'materia')

    legajo = input('ingrese legajo ')


# * punto A
barrido(lista)

# * punto B, C, D, E
aux = lista.inicio
while(aux is not None):
    promedio = 0
    parciales = aux.sublista.inicio
    control = True
    while(parciales is not None):
        if(parciales.info.nota < 6):
            control = False
        promedio += parciales.info.nota
        parciales = parciales.sig
        
    
    if(control and tamanio(aux.sublista) > 0):
        print('aprobo todos los examenes', aux.info)

    if(tamanio(aux.sublista) > 0 ):
        promedio = promedio / tamanio(aux.sublista) 
    print(promedio, aux.info)
    if(promedio>8.89):
        print('promedio mayor a ..', aux.info, promedio)

    if(aux.info.apellido[0].upper() == 'L'):
        print('comienza con..', aux.info)


    aux = aux.sig
'''