from Listas import Lista, insertar, eliminar, busqueda, tamanio, barrido

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla

#tabla = [0, 1, None, 3, 4]

def agregar_tc(tabla, hash, dato):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        #!completar
        print('Colision aplicar sondeo')
        if(posicion == len(tabla)-1):
            posicion = -1
        posaux = posicion
        while (tabla[posicion+1] is not None and hash(tabla[posicion+1], tabla) == posaux):
            posicion += 1
            if(posicion == len(tabla)-1):
                posicion = -1
        
        if(tabla[posicion+1] is None):
            tabla[posicion+1] = dato
        else:
            print('Hacer rehashing')

def agregar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato, criterio)

def quitar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return eliminar(tabla[posicion], dato.palabra, criterio)
    else:
        return None

def quitar_tc(tabla, hash, dato):
    dato = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion] == dato):
            dato = tabla[posicion]
            tabla[posicion] = None
            #! revisar si hay colision y realizar desplazamineto
        else:
            #! completar
            print('Aplicar funcion colision seguir buscando')
    return None

def buscar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return busqueda(tabla[posicion], dato.palabra, criterio)
    else:
        return None

def buscar_tc(tabla, hash, dato):
    pos = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion].codigo == dato.codigo):
            pos = posicion
        else:
            print('Aplicar funcion colision seguir buscando')
            if(posicion == len(tabla)-1):
                posicion = -1
            #! completar
            posaux = posicion
            while(tabla[posicion+1] is not None and hash(tabla[posicion+1], tabla) == posaux):
                posicion += 1
                if(posicion == len(tabla)-1):
                    posicion = -1
                if(tabla[posicion].codigo == dato.codigo):
                    pos = posicion
                    break
    return pos

def barrido_tc(tabla):
    '''Muestra los elementos de una tabla cerrada'''
    for indice in tabla:
        if indice is not None:
            print(indice)

def barrido_ta(tabla):
    '''Muestra elementos de una tabla abierta'''
    for i in tabla:
        if(i is not None):
            barrido(i)

def rehashing(tabla, hash):
    tam = len(tabla)*2
    nueva_tabla = crear_tabla(tam)
    for dato in tabla:
        if dato is not None:
            agregar_tc(nueva_tabla, hash, dato)
    return nueva_tabla

def hash_division(clave, tabla):
    return clave % len(tabla)

def hash_division_troopers(trooper, tabla):
    return trooper.codigo % len(tabla)

def bernstein(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_palabra(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena.palabra:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_troopers(trooper, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in trooper.legion:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_catedra(dato, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in dato.codigo[4:]:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_contacto(dato, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in dato.nombre + dato.apellido:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def cantidad_elementos_ta(tabla):
    cantidad = 0
    for elemento in tabla:
        if(elemento is not None):
            cantidad += tamanio(elemento)
    return cantidad
    #return sum(tamanio(lista) for lista in tabla if lista is not None)

def cantidad_elementos_tc(tabla):
    # cantidad = 0
    # for elemento in tabla:
    #     if(elemento is not None):
    #         cantidad += 1
    # return cantidad
    return len(tabla) - tabla.count(None)

def hash_diccionario(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)
    
def hash_cifrado(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)

def hash_guia(dato, tabla):
    return ord(dato.apellido[0].upper()) % len(tabla)

def hash_correo(dato, tabla):
    return ord(dato.apynom[0].upper()) % len(tabla)
'''
tabla = crear_tabla(10)
agregar_tc(tabla, hash_division, 15)
agregar_tc(tabla, hash_division, 25)
agregar_tc(tabla, hash_division, 27)
agregar_tc(tabla, hash_division, 5)
print(buscar_tc(tabla, hash_division, 5))
print(tabla)
'''
'''
tabla = crear_tabla(26)
# punto A
palabra = Palabra('hola', 'es un saludo')
agregar_ta(tabla, palabra, 'palabra')
palabra = Palabra('hielo', 'agua congelada')
agregar_ta(tabla, palabra, 'palabra')
palabra = Palabra('arbol', 'asdasdsadsda')
agregar_ta(tabla, palabra, 'palabra')
for i in tabla:
    if(i is not None):
        barrido(i)
print()
# punto B
pos = buscar_ta(tabla, Palabra('hola',''), 'palabra')
if(pos is not None):
    print('palabra', pos.info.palabra, 'significado', pos.info.significado)
print()
#punto C
print('elemento eliminado', quitar_ta(tabla, Palabra('hielo',''), 'palabra'))
for i in tabla:
    if(i is not None):
        barrido(i)
'''