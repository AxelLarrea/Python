from tda_archivo import abrir, leer, cerrar, guardar
from tda_arbol_bin import insertar_nodo, inorden, por_nivel, busqueda, inorden_lightsaber, busqueda_proximidad
#ejercicio 9

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

dic = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}


def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


por_nivel(bosque[0])


def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "AA31TF0AAMMMMMM0000"
from sys import getsizeof
cadena_cod = codificar(cadena, dic)
print(getsizeof(cadena_cod), getsizeof(b'00000110011011110100000'))
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)


#Ejercicio ?

arbol_nombre = None
arbol_ranking = None
arbol_especie = None

file = abrir('jedis')
pos = 0
while (pos <len(file)):
    jedi = leer(file, pos)
    arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
    arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
    arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
    pos += 1

cerrar(file)

#b
# file = abrir('jedis')
# inorden_lightsaber(arbol_nombre, file)
# cerrar(file)
#inorden(arbol_nombre)
# a=input()

#c
# por_nivel(arbol_especie)
# a=input()

#proximidad
busqueda_proximidad(arbol_nombre, 'l')

#d
pos = busqueda(arbol_nombre, 'luke skywalker')

if(pos is not None):
    print(pos.nrr)
    file = abrir('jedis')
    jedi = leer(file, pos.nrr)
    cerrar(file)
    print(jedi)