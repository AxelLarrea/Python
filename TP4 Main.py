from Listas_de_listas import busqueda, barrido, tamanio, lista_vacia
from Listas_de_listas import Lista, barrido_con_sublista, nodoLista, insertar, eliminar
from random import randint, choice
'''


#Ejercicio 1

lista = Lista()

while (tamanio(lista) < randint(0, 20)):
    dato = randint(0, 99)
    insertar(lista, dato)

barrido(lista)
print()
print('La cantidad de elementos de la lista es:', tamanio(lista))



#Ejercicio 2

lista = Lista()

while (tamanio(lista) < 20):
    dato = randint(97, 122)
    insertar(lista, chr(dato))

print('Datos de la lista:')
barrido(lista)
print()

dato = eliminar(lista, 'a')
while(dato is not None):
    dato = eliminar(lista, 'a')

dato = eliminar(lista, 'e')
while(dato is not None):
    dato = eliminar(lista, 'e')

dato = eliminar(lista, 'i')
while(dato is not None):
    dato = eliminar(lista, 'i')

dato = eliminar(lista, 'o')
while(dato is not None):
    dato = eliminar(lista, 'o')

dato = eliminar(lista, 'u')
while(dato is not None):
    dato = eliminar(lista, 'u')

print('Datos de la lista sin vocales:')
barrido(lista)



#Ejercicio 3

lista = Lista()
lista_par = Lista()
lista_impar = Lista()

for i in range(10):
    insertar(lista, randint(0, 50))

print('Los datos de la lista son: ')
barrido(lista)
print()

aux = lista.inicio

while(aux is not None):
    if(aux.info % 2 == 0):
        insertar(lista_par, aux.info)
    else:
        insertar(lista_impar, aux.info)
    aux= aux.sig

print('Lista par: ')
barrido(lista_par)
print()
print('Lista impar: ')
barrido(lista_impar)



#Ejercicio 4

lista = Lista()

while (tamanio(lista) < 10):
    insertar(lista, randint(0, 99))

barrido(lista)
print('El tamaño de la lista es:', tamanio(lista))

pos = int(input('Posicion en la que insertar el nodo: '))

nodito = nodoLista()
nodito.info = 2020
aux = lista.inicio
if (pos >= 0 and pos <= tamanio(lista)):
    if (pos < tamanio(lista)):
        for i in range(1, pos-1):
            aux = aux.sig
        nodito.sig = aux.sig
        aux.sig = nodito
    else:
        while (aux.sig is not None):
            aux = aux.sig
        aux.sig = nodito

barrido(lista)
print('El tamaño de la lista es:', tamanio(lista))



#Ejercicio 5

lista = Lista()

while (tamanio(lista) < 10):
    dato = randint(0,99)
    insertar(lista, dato)

barrido(lista)

aux = lista.inicio
cont = 0
while (aux is not None):
    x = aux.info
    for i in range(1, x):
        if (x % i  == 0):
            cont += 1
    if (cont < 3):
        eliminar(lista, x)
    aux = aux.sig
    cont = 0
print('Lista sin números primos: ')
barrido(lista)



#Ejercicio 6

lista = Lista()
dc = 0
marvel = 0

nombre = ['Linterna Verde', 'Wolverine', 'Dr. Strange', 'Capitana Marvel', 'Mujer Maravilla','Flash', 'Star-Lord', 'Iron-Man']
anio = ['1940', '1974', '1963', '1968', '1941', '1959', '1976','1963']
casa = ['DC', 'Marvel', 'DC', 'Marvel', 'DC', 'DC', 'Marvel','Marvel']
biografia = ['Caracterizado por su anillo de poder, posee la capacidad de crear manifestaciones de luz sólidad con solo pensarlo',
            'Su nombre es: James Logan, y sus característica son sus sentidos afinados, capacidad física mejorada y sus reconocibles garras',
            'Su nombre es: Stephen Strange, es el hechicero supremo, encargado de proteger la tierra de amenazas mágicas y místicas',
            'Su nombre es: Carol Danvers, es una superheroína la cual tiene genes Kree. Gracias a estos genes puede viajar a la velocidad de la luz y poseer un poder inmenso',
            'Princesa guerrera del Amazonas, conocida como Diana Prince, posee un Lazo de La Verdad, brazaletes mágicos irrompibles, además de poderes superhumanos y superiores habilidades de combate',
            'Posee supervelocidad en todos aspectos, tales como moverse y pensar, puede atravesar materia sólida y también posee reflejos superhumanos',
            'Su nombre es: Peter Quill, es conocido por su grupo Guardianes de las Galaxias',
            'Su nombre es: Tony Stark, es un excéntrico multillonario, filántropo y playboy. Posee una increíble armadura super resistente, equipada con armas y esta también le permite volar']

for i in range(0, len(anio)):
    insertar(lista, [nombre[i], anio[i], casa[i], biografia[i]])
barrido(lista)
print()

aux = lista.inicio
while (aux is not None):
    dato = aux.info
    
    #A : Borrar a Linterna Verde
    if (dato[0] == 'Linterna Verde'):
        print(dato[0],'ha sido eliminado')
        eliminar(lista, dato)
    
    #B : Mostrar año de aparicion de Wolverine
    if (dato[0] == 'Wolverine'):
        print('La fecha de aparición de', dato[0],'es:', dato[1])
    
    #C : Cambiar casa de Dr. Strange a Marvel
    if (dato[0] == 'Dr. Strange'):
        print('La casa de Dr. Strange es:', dato[2])
        dato[2] = 'Marvel'
        print('La casa a sido cambiada, ahora es:', dato[2])
    
    #D : Mostrar superhéroes que en su biografía tengan la palabra 'traje' o 'armadura'
    if (dato[3].find('traje') >= 0 or dato[3].find('armadura') >= 0):
        print('Este/a héroe/heroína posee traje o armadura:', dato[0])
    
    #E : Mostrar casa y nombre de héroes/heroínas cuya aparición sea anterior a 1963
    if (dato[1] < str(1963)):
        print('El/la héroe/heroína', dato[0], 'perteneciente a', dato[2],'apareció antes de 1963')
    
    #F : Mostrar casa a la que pertenecen Capitana Marvel y Mujer Maravilla
    if(dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla'):
        print(dato[0],'pertenece a', dato[2])
    
    #G : Mostrar info de Flash y Star-Lord
    if(dato[0] == 'Flash' or dato[0] == 'Star-Lord'):
        print('Biografía de:', dato[0], dato[3])
    
    #H : Listar superhéroes que comienzan con letra B,M y S
    if(dato[0][0] == 'B' or dato[0][0] == 'M' or dato[0][0] == 'S'):
        print('Este héroe comienza con B, M, o S:', dato[0])
    
    #I : Determinar cuantos superhéroes hay de cada casa de cómics
    if(dato[2] == 'DC'):
        dc += 1
    else:
        marvel += 1
    aux = aux.sig
print('Marvel tiene un total de', marvel,'héroes/heroínas')
print('DC tiene un total de', dc,'héroes/heroínas')



#Ejercicio 7

lista = Lista()
lista1 = Lista()
lista2 = Lista()
cont = 0

while (tamanio(lista) < 3):
    dato = randint(0, 5)
    insertar(lista, dato)
    insertar(lista2, dato)

while (tamanio(lista1) < 3):
    dato = randint(0, 5)
    insertar(lista1, dato)

print('Barrido lista 1: ')
barrido(lista)
print()

print('Barrido lista 2: ')
barrido(lista1)
print()

aux = lista.inicio
aux1 = lista1.inicio

#A: Concatenar dos listas, una tras la otra
while aux1 is not None:
    dato = aux1.info
    insertar(lista, dato)
    aux1 = aux1.sig
print('Listas concatenadas: ')
barrido(lista)
print()

#B: concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden
#C: contar cuántos elementos repetidos hay entre dos listas
aux1 = lista1.inicio
for i in range(0, tamanio(lista1)):
    dato = aux.info
    dato1 = aux1.info
    if(dato1 == dato):
        cont += 1
        eliminar(lista2, dato)
    else:
        insertar(lista2, dato1)
    aux = aux.sig
    aux1 = aux1.sig

print('Listas concatenadas sin elementos repetidos: ')
barrido(lista2)
print()
print('Hay un total de', cont,'elementos repetidos')
print()

#D: eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido
aux2 = lista2.inicio
while aux2 is not None:
    dato = aux2.info
    print('Contenido del nodo a eliminar:', dato)
    eliminar(lista2, dato)
    aux2 = aux2.sig



#Ejercicio 9

class Alumnos(object):
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' - ' + str(self.legajo)

class Parciales(object):
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha
    
    def __str__ (self):
        return self.materia + '' + str(self.nota)

lista = Lista()

for i in range(3):
    nombre = input('Ingrese nombre del alumno: ')
    apellido = input('Ingrese apellido del alumno: ')
    legajo = input('Ingrese legajo del alumno: ')
    alumno = Alumnos(nombre, apellido, legajo)
    insertar(lista, alumno,'apellido')
    print()

legajo = input('Ingrese legajo a buscar: ')
while legajo != '':
    pos = busqueda(lista, legajo, 'legajo')
    if pos is not None:
        materia = input('Ingrese materia del parcial: ')
        nota = int(input('Ingrese nota del parcial: '))
        fecha = input('Ingrese fecha del parcial: ')
        parcial = Parciales(materia, nota, fecha)
        insertar(pos.sublista, parcial, 'materia')
    else:
        print('No existe ese legajo')
    legajo = input('Ingrese legajo a buscar: ')

#A Mostrar alumnos ordenado por apellido
barrido(lista)

aux = lista.inicio
while aux is not None:
    parcial = aux.sublista.inicio
    promo = True
    promedio = 0
    while parcial is not None:
        if parcial.info.nota < 7:
            promo = False
        promedio += parcial.info.nota
        parcial = parcial.sig

    #B Indicar alumnos que no desaprobaron ningun parcial
    if promo == True:
        print('Alumno/a que no desaprobó ningún parcial:', aux.info)
    
    #E Mostrar promedio de cada alumno
    if tamanio(aux.sublista) > 0:
        prom = promedio/tamanio(aux.sublista)
        print('Promedio del alumno',aux.info,':', prom)
    
    #C Determinar alumnos con promedio mayor a 8.89
    if prom > 8.89:
        print('Este alumno posee un promedio mayor a 8.89:', aux.info)
    
    #D Mostrar toda la info de los alumnos con apellido comenzado en L
    if aux.info.apellido[0].upper() == 'L':
        print('Alumno cuyo apellido comienza con L:', aux.info)
    aux = aux.sig
    print()



#Ejercicio 10

top = ['Harry Styles - Watermelon Sugar','One Direction - You & I','Niall Horan - On The Loose','One Direction - History','One Direction - Little Things'
    ,'FKJ - Tadow','Calvin Harris - Under Control','Zomboy - Nuclear','Zayn - Dusk Till Dawn','Zayn - Like I Would','Liam Payne - Strip That Down'
    ,'One Direction - Cmon Cmon','One Direction - 18','Ed Sheeran - Perfect','Ed Sheeran - Thinking Out Loud','Harry Styles - Falling','Harry Styles - Sign Of The Time'
    ,'Niall Horan - Nice To Meet Ya','Logic - 1-800-2738255','Halsey - Sorry','Halsey - Without Me','NF - I You Want Love','David Guetta - Memories'
    ,'Skillet - Never Surrender','Skillet - One Day Too Late', 'Suicide Silence - You Only Live Once', 'Metallica - One','Iron Maiden - The Trooper'
    ,'Asking Alexandria - The Final Episode','Artic Monkeys - 505','Harry Styles - Lights Up','Robin Schulz - Ok','Robin Schulz - Show Me Love'
    ,'Jack & Jack - Groove','The Neighbourhood - Prey','The Neighbourhood - Sweater Weather','Vicentico - Creo Que Me Enamoré','Years & Years - Desire'
    ,'Years & Years - King','Linkin Park - Burn It Down']
class Canciones(object):
    def __init__(self, artista, nombre, duracion, reproducciones):
        self.artista = artista
        self.nombre = nombre
        self.duracion = duracion
        self.reproducciones = reproducciones
    
    def __str__(self):
        return self.artista + ' - ' + self.nombre + ', Duracion:' + self.duracion + ', Reproducciones:' + str(self.reproducciones)

lista = Lista()

for i in range(2):
    artista = input('Ingrese nombre del artista: ')
    nombre = input('Ingrese nombre de la cancion: ')
    duracion = input('Ingrese duracion de la cancion: ')
    reproducciones = randint(100000, 10000000)
    cancion = Canciones(artista, nombre, duracion, reproducciones)
    insertar(lista, cancion,'artista')
    print()

extensa = ''
aux = lista.inicio
while aux is not None:
    
    #A Cancion más extensa
    if aux.info.duracion > extensa:
        extensa = aux.info.duracion
        bio = aux.info
    
    #C Obtener canciones de banda Artic Monkeys
    if aux.info.artista == 'Artic Monkeys':
        print('Canciones de Artic Monkeys:', aux.info.nombre)
    
    #D Mostrar nombres de artistas con una sola palabra como nombre
    if len(aux.info.artista.split()) == 1:
        print('Este artista contiene una palabra como nombre:', aux.info.artista)
    aux = aux.sig
print()

print('Info de la cancion más extensa:', bio)
print()

#B Obtener top 5, top 10 y top 40
opcion = int(input('Ingrese una de las siguientes opciones: 1 = TOP 5, 2 = TOP10, 3 = TOP40, 0 = SALIR'))
while not opcion == 0:
    if opcion == 1:
        print('TOP 5')
        for i in range(0, 5):
            print(i+1,'-',top[i])
    if opcion == 2:
        print('TOP 10')
        for i in range(0, 10):
            print(i+1,'-',top[i])
    if opcion == 3:
        print('TOP 40')
        for i in range(0, 40):
            print(i+1,'-',top[i])
    opcion = int(input('Ingrese una de las siguientes opciones: 1 = TOP 5, 2 = TOP10, 3 = TOP40, 0 = SALIR'))



#Ejercicio 11

class Personaje(object):

    def __init__(self, nombre, altura, edad, genero, especie, planeta, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodios = episodios

    def __str__(self):
        return self.nombre + ' | ' + str(self.altura) + ' | ' + str(self.edad) + ' | ' + self.genero + ' | ' + self.especie + ' | ' + self.planeta + ' | ' + str(self.episodios)

lista = Lista()

datos = Personaje('Leia Organa', 168, 33, 'F', 'Humano', 'Tatooine', [1, 3, 5, 6])
insertar(lista, datos, 'nombre')
datos = Personaje('Han Solo', 172, 36, 'M', 'Humano', 'Alderaan', [1, 2, 5, 6, 7])
insertar(lista, datos, 'nombre')
datos = Personaje('Darth Vader', 181, 53, 'M', 'Humano', 'Polis Massa', [3, 5, 6, 7, 8])
insertar(lista, datos, 'nombre')
datos = Personaje('Chewbacca', 190, 41, 'M', 'Wookie', 'Dandoran', [1, 2, 4, 6, 9])
insertar(lista, datos, 'nombre')
datos = Personaje('Luke Skywalker', 176, 31, 'M', 'Humano', 'Tatooine', [1, 2, 3, 5, 6])
insertar(lista, datos, 'nombre')
datos = Personaje('C3PO', 171, 40, 'M', 'Droide', 'Tatooine', [1, 2, 3, 4, 5, 6])
insertar(lista, datos, 'nombre')
datos = Personaje('Yoda', 69, 900, 'M', 'Yoda', 'Desconocido', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')
datos = Personaje('R2D2', 110, 40, 'M', 'Droide', 'Tatooine', [1, 2, 3, 4, 5, 6, 7])
insertar(lista, datos, 'nombre')
datos = Personaje('Kylo Ren', 170, 37, 'M', 'Humano', 'Tatooine', [4, 5, 6])
insertar(lista, datos, 'nombre')

#A Listar los personajes de género femenino
aux = lista.inicio
while aux is not None:
    if aux.info.genero == 'F':
        print('Personaje femenino:', aux.info.nombre)
    aux = aux.sig
print()

#B Listar todos los personaje droides que aparecieron en las 6 primeras pelis
aux = lista.inicio
while aux is not None:
    control = False
    if aux.info.especie == 'Droide':
        for i in range(0, 5):
            if aux.info.episodios[i] == i+1 and i+1 <= 7:
                control = True
            else:
                control = False
    if control:
        print(aux.info.nombre,'es un Droide')
    aux = aux.sig
print()

#C Mostrar toda la información de Darth Vader y Han Solo
aux = lista.inicio
while aux is not None:
    if aux.info.nombre == 'Darth Vader' or aux.info.nombre == 'Han Solo':
        print(aux.info)
    aux = aux.sig
print()

#D Listar los personajes que aparecen en el episodio VII y en los tres anteriores
aux = lista.inicio
while aux is not None:
    if (4 in aux.info.episodios) and (5 in aux.info.episodios) and (6 in aux.info.episodios) and (7 in aux.info.episodios):
        print(aux.info.nombre,'aparece desde el capítulo 4 al 7')
    aux = aux.sig
print()

#E Mostrar los personajes con edad mayor a 850 años y de ellos el mayor
aux = lista.inicio
mayor = 0
while aux is not None:
    control = False
    if aux.info.edad >= 850:
        print(aux.info.nombre,'tiene más de 850 años')
    if aux.info.edad >= 850 and aux.info.edad > mayor:
        mayor = aux.info.edad
        pers = aux.info
    aux = aux.sig
print('El mayor de ellos es:', pers.nombre)
print()

#F Eliminar a los que aparecieron en los capítulos 4,5,6
aux = lista.inicio
while aux is not None:
    if (4 in aux.info.episodios) and (5 in aux.info.episodios) and (6 in aux.info.episodios) and len(aux.info.episodios) == 3:
        print(aux.info.nombre,'ha sido eliminado/a de la lista')
        eliminar(lista, aux.info)
    aux = aux.sig
print()

#G Listar los personajes de especie humana cuyo planeta de origen es Alderaan
aux = lista.inicio
while aux is not None:
    if aux.info.planeta == 'Alderaan' and aux.info.especie == 'Humano':
        print(aux.info.nombre,'es un humano proveniente de Alderaan')
    aux = aux.sig
print()

#H Mostrar los personajes cuya altura es menor a 70cm
aux = lista.inicio
while aux is not None:
    if aux.info.altura < 70:
        print(aux.info.nombre,'mide menos de 70cm')
    aux = aux.sig
print()

#I Determinar en qué episodios aparece Chewbacca y mostrar su info
aux = lista.inicio
while aux is not None:
    if aux.info.nombre == 'Chewbacca':
        print(aux.info.nombre,'aparece en los episodios', aux.info.episodios)
        print('Toda su info:',aux.info)
    aux = aux.sig
print()



#Ejercicio 12

lista = Lista()

for i in range(10):
    insertar(lista, randint(0, 100))

barrido(lista)
print()

cont = 0
aux = lista.inicio
tam = tamanio(lista)
print('Tamaño de lista', tam)
while (aux is not None):
    cont += 1
    if cont == tam-1:
        eliminar(lista, aux.info)
        break
    aux = aux.sig
barrido(lista)



#Ejercicio 14

class Persona(object):
    
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

lista = Lista()
nombres = ['Axel', 'Fernando', 'Gastón', 'Marimar', 'Magalí']
for i in range(5):
    dato = Persona(nombres[i], randint(0, 100))
    insertar(lista, dato, 'nombre')

aux = lista.inicio

while aux is not None:
    x = randint(1, 6)
    print('A', aux.info.nombre,'le salió un:', x)
    if x == 5:
        print(aux.info.nombre,'ganó la partida')
        break
    if aux.sig is None:
        aux = lista.inicio
    else:
        aux = aux.sig



#Ejercicio 16

lista = Lista()
actividades = Lista()
en_tiempo = Lista()
fuera_tiempo = Lista()

nombres = ['Axel', 'Rodrigo', 'Walter', 'Facundo', 'Florencia']

for i in range(10):
    fecha_ini = [2020, randint(1, 12), randint(1, 31)]
    fecha_fin = [2020, randint(1, 12), randint(1, 31)]
    fecha_fin_ef = [2020, randint(1, 12), randint(1, 31)]
    datos = [randint(100, 1000), randint(1, 5), fecha_ini, fecha_fin, fecha_fin_ef, choice(nombres)]
    insertar(lista, datos)

barrido(lista)

prom_tareas = 0
costo_total_pro = 0
aux = lista.inicio
while aux is not None:
    #A Promedio de tareas
    prom_tareas += aux.info[1]

    #B Costo total de proyecto
    costo_total_pro += aux.info[0]

    #C Actividades realizadas por una persona
    print('Actividades realizadas por',aux.info[5])
    print('Actividades: ni idea a qué se refiere xD')
    print('Tiempo de ejecución:',aux.info[1])

    #D Actividades entre dos fechas dadas
    if aux.info[2][1] >= 3 and aux.info[3][1] >= 3:
        insertar(actividades, aux.info)
    
    #E Mostrar las tareas finalizas en tiempo y fuera de tiempo
    if aux.info[3][1] > aux.info[4][1] and aux.info[3][2] > aux.info[4][2]:
        insertar(fuera_tiempo, [aux.info[0], aux.info[1], aux.info[5]])
    else:
        insertar(en_tiempo, [aux.info[0], aux.info[1], aux.info[5]])
    aux = aux.sig
print()

print('Tiempo promedio de tareas:', prom_tareas/tamanio(lista))
print('Costo total del proyecto: $' + str(costo_total_pro))
print('Actividades entre dos fechas dadas:')
barrido(actividades)
print()

if not lista_vacia(fuera_tiempo):
    print('Lista con tareas finalizadas fuera de tiempo:')
    barrido(fuera_tiempo)
    print()
if not lista_vacia(en_tiempo):
    print('Lista con tareas finalizas en tiempo:')
    barrido(en_tiempo)



#Ejercicio 17

lista = Lista()
vuelo_turista = Lista()
total_por_vuelo = Lista()
vuelos_abril = Lista()
vuelo_eliminado = Lista()
vuelos_tailandia = Lista()

empresa = ['American Airlines', 'Aerolíneas Argentinas', 'LATAM Airlines', 'British Airways', 'Sky Airline']
destino = ['Irlanda', 'Inglaterra', 'España', 'India', 'Rusia', 'Rodas', 'Atenas', 'Greta', 'Miconos', 'Tailandia']
clase = ['Turista', 'Primera']
estado = ['Ocupado', 'Desocupado']
num_asiento = 1
control = True

for i in range(10):
    fecha_salida = [2020, randint(1, 12), randint(1, 31)]
    asientos = randint(30, 140)
    datos = [choice(empresa), randint(0, 2000), asientos, fecha_salida, choice(destino), randint(400, 2000)]
    insertar(lista, datos)

aux = lista.inicio
while aux is not None:
    for j in range(asientos):
        asiento_avion = busqueda(lista, aux.info)
        if asiento_avion is not None:
            dato = [num_asiento, choice(clase), choice(estado)]
            num_asiento += 1
            insertar(asiento_avion.sublista, dato)
    num_asiento = 1
    aux = aux.sig

# print('EMPRESA | VUELO | ASIENTOS | FEC. SALIDA | DESTINO | KMS')
barrido(lista)
print()
total_turista = 0
total_primera_clase = 0
aux = lista.inicio
while aux is not None:
    #A Mostrar vuelos con destinos a Atenas, Miconos, Rodas
    if (aux.info[4] == 'Atenas') or (aux.info[4] == 'Miconos') or (aux.info[4] == 'Rodas'):
        print('Info de vuelo con destino a:', aux.info[4])
        print(aux.info)
        print()
    
    #B Mostrar los vuelos con asientos clase turista disponible
    avion = aux.sublista.inicio
    while avion is not None:
        if (avion.info[1] == 'Turista') and (avion.info[2] == 'Disponible'):
            insertar(vuelo_turista, aux.info)
            break
    #C Mostrar el total recaudado por cada vuelo, clase turista ($75/km) y primera clase ($203/km)
        if avion.info[2] == 'Ocupado':
                if avion.info[1] == 'Turista':
                    total_turista += (75 * aux.info[5])
                else:
                    total_primera_clase += (203 * aux.info[5]) 
        avion = avion.sig
    insertar(total_por_vuelo, [aux.info[1], total_turista, total_primera_clase])

    #D Mostrar los vuelos programados para una determinada fecha
    if aux.info[3][1] == 4:
        insertar(vuelos_abril, aux.info)
    
    #G Mostrar las empresas y los kilómetros de vuelos con destino a Tailandia
    if aux.info[4] == 'Tailandia':
        insertar(vuelos_tailandia, [aux.info[0], aux.info[5]])
    aux = aux.sig

barrido_con_sublista(lista)
print()

print('Vuelos programados para abril:')
barrido(vuelos_abril)
print()

#E Vender un asiento (o pasaje) para un determinado vuelo
num_vuelo = int(input('Ingrese el numero de vuelo: '))
num_asiento = int(input('Ingrese el numero del asiento: '))
clase = input('Ingrese la clase: ')
aux = lista.inicio
while aux is not None:
    if num_vuelo == aux.info[1]:
        pos = busqueda(lista, aux.info)
        if pos is not None:
            aux2 = pos.sublista.inicio
            while aux2 is not None:
                if aux2.info[0] == num_asiento and aux2.info[2] == 'Desocupado':
                    aux2.info[1] = 'Ocupado'
                    print('Se ha vendido el pasaje')
                    break
                aux2 = aux2.sig
    aux = aux.sig

print()

#F Eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, indicar la cantidad de dinero a devolver
num_vuelo = int(input('Ingrese numero del vuelo a eliminar: '))
aux = lista.inicio
while aux is not None:
    if num_vuelo == aux.info[1]:
        pos = busqueda(lista, aux.info)
        if pos is not None:
            eliminar(lista, aux.info)
            vuelo_eliminado = aux
            print('Vuelo eliminado')
            break
    aux = aux.sig
print()

devolver = 0
km = vuelo_eliminado.info[5]
vuelo = vuelo_eliminado.sublista.inicio
while vuelo is not None:
    if vuelo.info[1] == 'Ocupado':
        if vuelo.info[2] == 'Turista':
            devolver += 75 * km
        else:
            devolver += 203 * km
    vuelo = vuelo.sig 
print('Total a devolver: $' + str(devolver))

print('Empresas con vuelos a Tailandia y su distancia:')
if not lista_vacia(vuelos_tailandia):
    barrido(vuelos_tailandia)
else:
    print('No hay vuelos programados con destino a Tailandia')



#Ejercicio 18
class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return self.archivo + ' | ' + self.timestamp + ' | ' + self.mensaje + ' | ' + str(self.cant_lineas)

lista = Lista()

insertar(lista, 'AxelSixx')
insertar(lista, 'ElChili')
insertar(lista, 'Douu')
insertar(lista, 'OtpZed')

commit = Commit('test.py', '11-11-20 20:30', 'app testing', 46)
pos = busqueda(lista, 'AxelSixx', 'nombre')
insertar(pos.sublista, commit, 'archivo')
commit = Commit('database.py', '11-11-20 19:00', 'debugged', 120)
pos = busqueda(lista, 'AxelSixx', 'nombre')
insertar(pos.sublista, commit, 'archivo')
commit = Commit('app.java', '11-11-20 19:00', 'modelado de la interfaz', 0)
pos = busqueda(lista, 'ElChili', 'nombre')
insertar(pos.sublista, commit, 'archivo')
commit = Commit('api.py', '11-11-20 19:00', 'establecimiento de conexiones', -34)
pos = busqueda(lista, 'Douu', 'nombre')
insertar(pos.sublista, commit, 'archivo')
commit = Commit('busqueda.html', '11-11-20 19:00', 'update', 87)
pos = busqueda(lista, 'OtpZed', 'nombre')
insertar(pos.sublista, commit, 'archivo')
commit = Commit('main.css', '11-11-20 19:00', 'correciones', -2)
pos = busqueda(lista, 'OtpZed', 'nombre')
insertar(pos.sublista, commit, 'archivo')

barrido_con_sublista(lista)

#A Obtener el usuario con mayor cantidad de commits (pueden ser varios)
aux = lista.inicio
mayor_commit = 0
while aux is not None:
    if tamanio(aux.sublista) > mayor_commit:
        mayor_commit = tamanio(aux.sublista)
    aux = aux.sig
aux = lista.inicio
while aux is not None:
    if tamanio(aux.sublista) == mayor_commit:
        print('Colaborador con mayor cantidad de commits:', aux.info)
        print('Cantidad de commits:', mayor_commit)
    aux = aux.sig
print()

#B Obtener el usuario que haya agregado en total mayor cantidad de líneas y el que haya eliminado menor cantidad de líneas
mayor = 0
usuario_mayor = ''
aux = lista.inicio
while aux is not None:
    aux2 = aux.sublista.inicio
    mayor_aux = 0
    while aux2 is not None:
        mayor_aux += aux2.info.cant_lineas
        aux2 = aux2.sig
    if mayor_aux > mayor:
        mayor = mayor_aux
        usuario_mayor = aux.info
    aux = aux.sig
print('El usuario', usuario_mayor, 'agrego la mayor cantidad de lineas:', mayor)

menor = 0
usuario_menor = ''
aux = lista.inicio
while aux is not None:
    sublista = aux.sublista.inicio
    menor_aux = 0
    while sublista is not None:
        menor_aux += sublista.info.cant_lineas
        sublista = sublista.sig
    if menor_aux < menor:
        menor = menor_aux
        usuario_menor = aux.info
    aux = aux.sig
print('El usuario', usuario_menor, 'elimino la mayor cantidad de lineas:', menor)

#C Mostrar los usuarios que realizaron cambios sobre el archivo test.py después de las 19:45 sin importar la fecha
aux = lista.inicio
while aux is not None:
    pos = busqueda(aux.sublista, 'test.py', 'archivo')
    if pos is not None:
        if pos.info.timestamp.split(' ')[1] > '19:45':
            print('El usuario', aux.info, 'realizo cambios en test.py')
    aux = aux.sig

#D Indicar los usuarios que hayan realizado al menos un commit con cero líneas agregados o eliminadas
aux = lista.inicio
while aux is not None:
    pos = busqueda(aux.sublista, 0, 'cant_lineas')
    if pos is not None:
        print('El usuario', aux.info, 'realizo un commit con 0 lineas')
    aux = aux.sig
print()

#E Determinar el nombre del usuario que realizó el último commit sobre el archivo app.py indicando toda la información de dicho commit
aux = lista.inicio
while aux is not None:
    pos = busqueda(aux.sublista, 'api.py', 'archivo')
    if pos is not None:
        print('El usuario', aux.info, 'realizo cambios en api.py')
        barrido(aux.sublista)
    aux = aux.sig

#Ejercicio 21

lista = Lista()
lista_criterio = Lista()

class Pelicula(object):
    def __init__ (self, nombre, valoracion, estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.estreno = estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return self.nombre + ' | ' + str(self.valoracion) + ' | ' + str(self.estreno) + ' | ' + str(self.recaudacion)


pelis = ['Avengers - End Game', 'American Pie', 'John Wick 3', 'Interstellar', 'Koe no Katachi', 'Captain America - Civil War']
fechas = [2019, 1999, 2019, 2014, 2016, 2016]

for i in range(6):
    dato = Pelicula(pelis[i], randint(0,10), fechas[i], randint(1000000,1000000000))
    insertar(lista, dato, 'nombre')

#A Filtrar películas por año, es decir mostrar películas determinadas
fecha = int(input('Ingresa fecha de la cual ver películas: '))
aux = lista.inicio
while aux is not None:
    if aux.info.estreno == fecha:
        print('Nombre de película:',aux.info.nombre)
        print('Año de estreno:',aux.info.estreno)
    aux = aux.sig
print()

#B Mostrar los datos de la película que más recaudó
mayor = 0
aux = lista.inicio
while aux is not None:
    if aux.info.recaudacion > mayor:
        mayor = aux.info.recaudacion
        best_reca = aux.info
    aux = aux.sig
print('Película que más recaudó:', best_reca.nombre,'con $'+ str(mayor))
print()

#C Indicar las películas con mayor valoración del público, puede ser más de una 
max_valor = 0
aux = lista.inicio
while aux is not None:
    if aux.info.valoracion > max_valor:
        max_valor = aux.info.valoracion
    aux = aux.sig

aux = lista.inicio
print('Películas con mayor valoración:')
while aux is not None:
    if aux.info.valoracion == max_valor:
        print(aux.info.nombre)
    aux = aux.sig
print()

#D Ordenar según un criterio ingresado, nombre, valoración, año de estreno o recaudación
criterio = input('Ingrese criterio de orden: ')
print('- nombre')
print('- valoracion')
print('- estreno')
print('- recaudacion')
print()

aux = lista.inicio
while aux is not None:
    dato = aux.info
    insertar(lista_criterio, dato, criterio)
    aux = aux.sig
print()
if criterio == 'Nombre':
    print('Lista ordenada por nombre:')
    barrido(lista_criterio)
elif criterio == 'valoracion':
    print('Lista ordenada por valoracion:')
    barrido(lista_criterio)
elif criterio == 'estreno':
    print('Lista ordenada por año de estreno:')
    barrido(lista_criterio)
elif criterio == 'recaudacion':
    print('Lista ordenada por recaudacion:')
    barrido(lista_criterio)
'''