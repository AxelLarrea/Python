''' 
from Pilas import Pila, Apilar, Desapilar, Pila_Llena, Pila_Vacia

pila = Pila()
pila2 = Pila()
while not Pila_Llena(pila):
    x = int(input('Ingrese un número'))
    Apilar(pila, x)

while not Pila_Vacia(pila):
    x = Desapilar(pila)
    print(x)
    Apilar(pila2, x)

while not Pila_Vacia(pila2):
    x = Desapilar(pila2)
    print(x)
    Apilar(pila, x)

print(pila.datos)

'''
