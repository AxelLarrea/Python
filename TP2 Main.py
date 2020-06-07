'''
from Pila_Dinamico import Pila, apilar, desapilar, pila_vacia, cima, tamanio
'''
from Pilas import Pila, Pila_Llena, Pila_Vacia, Desapilar, Apilar
from random import randint

'''
#Ejercicio 1

pila = Pila()
Total = 0

while not Pila_Llena(pila):
    x = int(input('Ingrese un número: '))
    Apilar(pila, x)


while not Pila_Vacia(pila):
    x = Desapilar(pila)
    y = Desapilar(pila)
    if(x == y):
        Total += 1
print('El total de ocurrencias es: ', Total)

#Ejercicio 2

pila = Pila()
pilapar = Pila()
pilaimpar = Pila()

while not Pila_Llena(pila):
    x = randint(1,100)
    print(x)
    Apilar(pila, x)

while not Pila_Vacia(pila):
    x = Desapilar(pila)
    if(x % 2 == 0):
        Apilar(pilapar, x)
    else:
        Apilar(pilaimpar, x)


print("pila par")
while not Pila_Vacia(pilapar):
    x = Desapilar(pilapar)
    print(x)

print("pila impar")
while not Pila_Vacia(pilaimpar):
    x = Desapilar(pilaimpar)
    print(x)


#Ejercicio 3

pila = Pila()
pila_aux = Pila()

while not Pila_Llena(pila):
    x = int(input('Ingrese un número: '))
    Apilar(pila, x)


while not Pila_Vacia(pila):
    Total = 0
    x = Desapilar(pila)
    while not Pila_Vacia(pila):
        y = Desapilar(pila)
        if(x == y):
            Total += 1
            y = 0
        Apilar(pila_aux, y)
    x = 0
    Apilar(pila_aux, x)

print('El total de ocurrencias es: ', Total)

while not Pila_Vacia(pila_aux):
    z = Desapilar(pila_aux)
    print(z)

#Ejercicio 4

pila = Pila()
pila_aux = Pila()

while not Pila_Llena(pila):
    x = int(input('Ingrese un número: '))
    Apilar(pila, x)

while not Pila_Vacia(pila):
    x = Desapilar(pila)
    print(x)
    Apilar(pila_aux, x)

#Ejercicio 5

status = True
pila = Pila()
pila_aux = Pila()
pila2 = Pila()
x = ''
y = ''

print('Ingrese su palabra letra por letra')
while not Pila_Llena(pila):
    x = (input('Ingrese su letra correspondiente: '))
    Apilar(pila, x)
    Apilar(pila_aux, x)
    
while not Pila_Vacia(pila_aux):
    y = Desapilar(pila_aux)
    Apilar(pila2, y)

while not (Pila_Vacia(pila) and Pila_Vacia(pila2)):
    x = Desapilar(pila)
    y = Desapilar(pila2)
    if (x != y):
        status = False
    else:
        status = True

if (status == True):
    print('Es palindromo')
else:
    print('No es palindromo')


#Ejercicio 6

pila = Pila()

while not Pila_Llena(pila):
    x = input('Ingrese la palabra a invertir letra por letra: ')
    Apilar(pila, x)

while not Pila_Vacia(pila):
    x = Desapilar(pila)
    print(x)

#Ejercicio 7

pila = Pila()

while not Pila_Llena(pila):
    x = input('Ingrese la palabra: ')
    Apilar(pila, x)

c = Desapilar(pila)
print('- Palabra a eliminar:', Desapilar(pila))
Apilar(pila, c)

while not Pila_Vacia(pila):
    x = Desapilar(pila)
    print(x)
'''


