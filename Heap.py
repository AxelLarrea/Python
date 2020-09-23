class Heap(object):
    """Crear un montículo."""

    def __init__(self, tamanio):
        """Crea un montículo vacio."""
        self.vector = [None] * tamanio
        self.tamanio = 0


def intercambio(vector, indice1, indice2):
    """Intercambia dos valores de la tabla."""
    vector[indice1], vector[indice2] = vector[indice2], vector[indice1]


def agregar(heap, dato):
    """Agrega un dato en el montículo."""
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    """Quita el elemento en la cima del montículo."""
    intercambio(heap.vector, 0, heap.tamanio-1)
    dato = heap.vector[heap.tamanio-1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato


def flotar(heap, indice):
    """Flota el elemento en la posición índice."""
    while(indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
        #print('flotando', heap.vector[indice])
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre


def hundir(heap, indice):
    """Hunde el elemento en la posición índice."""
    hijo_izq = (indice * 2) + 1
    control = True
    while(control and hijo_izq < heap.tamanio):
        #print('hundir', heap.vector[indice])
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if(hijo_der < heap.tamanio):
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der

        if (heap.vector[indice] < heap.vector[aux]):
            #print('se hundio')
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
            #print('luego de hundir', heap.vector)
        else:
            control = False
        


def cantidad_elementos(heap):
    """Devuelve la cantidad de elementos en el montículo."""
    return heap.tamanio


def heap_vacio(heap):
    """Devuelve true si el montículo esta vacio."""
    return heap.tamanio == 0


def heap_lleno(heap):
    """Devuelve true si el montículo esta lleno."""
    return heap.tamanio == len(heap.vector)


def monticulizar(heap):
    """Transforma un vector en un mantículo."""
    for i in range(len(heap.vector)):
        flotar(heap, i)

def heapsort(heap):
    """Método de ordenamiento heapsort."""
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux



monticulo = Heap(20)
vector = [3, 2, 8, 0, 4, 6, 88, 99, 1, 2]

monticulo.vector = vector
monticulo.tamanio = 10

monticulizar(monticulo)

print(monticulo.vector)

# agregar(monticulo, 4)
# #print(monticulo.vector)
# agregar(monticulo, 15)
# #print(monticulo.vector)
# agregar(monticulo, 6)
# #print(monticulo.vector)
# agregar(monticulo, 1)
# #print(monticulo.vector)
# agregar(monticulo, 34)
# #print(monticulo.vector)
# agregar(monticulo, 40)
# #print(monticulo.vector)
# agregar(monticulo, 10)
# #print(monticulo.vector)
# print('tamanio del heap', monticulo.tamanio)
# heapsort(monticulo)
# print(monticulo.vector)
# print('tamanio del heap', monticulo.tamanio)