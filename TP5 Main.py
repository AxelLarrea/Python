from Tablas_Hash import crear_tabla, agregar_ta, bernstein_troopers, hash_division_troopers, bernstein_palabra, hash_division, hash_cifrado
from random import choice, randint
from Listas import barrido
from Tablas_Hash import buscar_ta, quitar_ta, bernstein_catedra, hash_diccionario, hash_guia
from Tablas_Hash import agregar_tc, buscar_tc, quitar_tc

'''
#Ejercicio 1

class Palabra(object):
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
    
    def __str__(self):
        return self.palabra+ ' = ' +self.significado

tabla = crear_tabla(3)

#A Agregar palabra y su significado a un diccionario
for i in range(3):
    palabra = input('Ingrese palabra: ')
    significado = input('Ingrese significado de la palabra: ')
    pal = Palabra(palabra, significado)
    agregar_ta(tabla, hash_diccionario, pal, 'palabra')

#B Determinar si una palabra existe y mostrar su significado
x = input('Ingrese palabra a buscar: ')
pos = buscar_ta(tabla, hash_diccionario, Palabra(x,''), 'palabra')
if pos is not None:
    print('La palabra es:', pos.info.palabra,', y su significado es:', pos.info.significado)

#C Borrar una palabra
y = input('Ingrese palabra a eliminar: ')
print('La palabra eliminada:', quitar_ta(tabla, hash_diccionario, Palabra(y, ''), 'palabra'))

for i in tabla:
    if i is not None:
        barrido(i)

#Ejercicio 2

class Guia(object):
    def __init__(self, numero, nombre, apellido, direccion):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

    def __str__(self):
        return self.numero + ' ' + self.nombre + ' ' + self.apellido + ', ' + self.direccion

tabla = crear_tabla(2)

for i in range(2):
    numero = input('Ingrese numero de telefono: ')
    nombre = input('Ingrese nombre del titular: ')
    apellido = input('Ingrese apellido del titular: ')
    direccion = input('Ingrese direccion del titular: ')
    guia = Guia(numero, nombre, apellido, direccion)
    agregar_ta(tabla, hash_guia, guia, 'numero')
    print()
print()

for i in tabla:
    if i is not None:
        barrido(i)

#Ejercicio 3

class Catedra(object):
    def __init__(self, codigo, nombre, modlidad, horas):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modlidad
        self. horas = horas
        self.docentes = []
    
    def __str__(self):
        return self.codigo+' '+self.nombre+' '+str(self.docentes)

tabla = crear_tabla(4)

#A Cargar cátedras con la info correspondiente
catedra = Catedra('ALG_34211', 'algoritmos y estructuras de datos', 'anual', 4)
agregar_tc(tabla, bernstein_catedra, catedra)
catedra = Catedra('ALG_34212', 'programacion orientada a objetos', 'anual', 5)
agregar_tc(tabla, bernstein_catedra, catedra)
catedra = Catedra('ALG_34213', 'fundamentos de programacion', 'anual', 5)
agregar_tc(tabla, bernstein_catedra, catedra)
catedra = Catedra('ALG_34223', 'programacion avanzada', 'cuatrimestral', 4)
agregar_tc(tabla, bernstein_catedra, catedra)

#B Agregar docentes vinculados con la cátedra
posicion = buscar_tc(tabla, bernstein_catedra, Catedra('ALG_34211','','',0))
if(posicion is not None):
    print('Cargar docente')
    tabla[posicion].docentes.append('Tito')
posicion = buscar_tc(tabla, bernstein_catedra, Catedra('ALG_34211','','',0))
if(posicion is not None):
    print('Cargar docente')
    tabla[posicion].docentes.append('Walter')

for catedra in tabla:
    print(catedra)

#Ejercicio 9

tabla = crear_tabla(10)
tabla2 = crear_tabla(10)
def desifrar(dato):
    dic = {"#?&": '0',"abc": '1',"def":'2',"ghi":'3',"jkl":'4',"mnñ":'5',"opq":'6',"rst":'7',"uvw":'8',"xyz":'9'}
    cadena = ''
    for i in range (0, len(dato),3):
        cadena += dic[dato[i:i+3]]
    return chr(int(cadena))
def cifrar(dato):
    valor = str(ord(dato))
    valor_cirado = ["#?&","abc","def","ghi","jkl","mnñ","opq","rst","uvw","xyz"]
    cadena = ""
    for num in valor:
        numInt = int(num)
        cadena += valor_cirado[numInt]
    cadena += "%"
    return cadena
a = 'Holaaaaaaaaa Mundo des tda hash'
a_cifrado = ''
for letra in a:
    valor = buscar_ta(tabla, hash_cifrado, Palabra(letra, ''), 'palabra')
    cifrado = ''
    if(valor is None):
        cifrado = cifrar(letra)
        palabra = Palabra(letra, cifrado)
        agregar_ta(tabla, hash_cifrado, palabra, 'palabra')
    else:
        cifrado = valor.info.significado
    a_cifrado += cifrado
print(a_cifrado)
lista = a_cifrado.split('%')
lista.pop()
msj = ''
for letras in lista:
    valor = buscar_ta(tabla2, bernstein_palabra, Palabra(letras, ''), 'palabra')
    decifrado = ''
    if(valor is None):
        decifrado = desifrar(letras)
        palabra = Palabra(letras, decifrado)
        agregar_ta(tabla2, bernstein_palabra, palabra, 'palabra')
    else:
        decifrado = valor.info.significado
    msj += decifrado
print(msj)
# for i in tabla:
#     print(i)

#print(a_cifrado)
#valor = buscar_ta(tabla, hash_cifrado, Palabra('H', ''), 'palabra')

#print(valor.info.significado)

#Ejercicio 6

letras = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
tabla_legion = crear_tabla(10)
tabla_codigos = crear_tabla(1000)
class Stormtrooper(object):
    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo
    
    def __str__(self):
        return self.legion+' '+str(self.codigo)
for i in range(1,2000):
    legion = choice(letras)
    codigo = randint(1000, 9999)
    trooper = Stormtrooper(legion, codigo)
    agregar_ta(tabla_legion, bernstein_troopers, trooper, 'legion')
    agregar_ta(tabla_codigos, hash_division_troopers, trooper, 'codigo')
posicion = bernstein('FN', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = bernstein('CT', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = hash_division(537, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])
print()
posicion = hash_division(781, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])
'''