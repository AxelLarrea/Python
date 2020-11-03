from Grafos import Grafo, grafo_vacio, insertar_vertice, buscar_vertice, insertar_arista
from Archivos import leer, abrir, guardar, cerrar

#Ejercicio 1


class Vuelo():

    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

tabla = []
print(tabla)

file = abrir('Star_Wars')

for i in tabla:
    vuelito = Vuelo(i[0], i[1], i[2])
    guardar(file, vuelito)

pos = 0
while(pos < len(tabla)):
    personaje = leer(file, pos)
    print(pos)
    print(len(file))
    pos += 1
cerrar(file)
