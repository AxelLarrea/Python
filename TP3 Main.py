from Cola_Dinamico import Cola, arribo, atencion, cola_vacia, tamanio, en_frente, mover_final
from random import randint
from Pila_Dinamico import Pila, apilar, desapilar, pila_vacia, tamanio

'''
#Ejercicio 1

cola = Cola()
cola2 = Cola()

while not cola_llena(cola):
    x = input('Ingrese las letras deseadas: ')
    arribo(cola, x)
print('Lista de letras: ')
for i in range(0, tamanio(c)):
    print(mover_final(c))

while not cola_vacia(cola):
    x = atencion(cola)
    if ((x != 'a') and (x != 'e') and (x != 'i') and (x != 'o') and (x != 'u')):
        arribo(cola2, x)

while not cola_vacia(cola2):
    x = atencion(cola2)   
    print('Lista de letras sin vocales: ', x)

# Ejercicio 2

cola = Cola()
pila = Pila()

while (tamanio(cola) < 5):
    x = int(input('Ingrese los números deseados: '))
    arribo(cola, x)

print('Los datos ingresados son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)

print('Los datos al revés son: ')

while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)

#Ejercicio 3
cola = Cola()
cola2 = Cola()
pila = Pila()
status = False

print('Ingrese su palabra letra por letra: ')
while (tamanio(cola) < 4):
    x = input('Ingrese la letra correspondiente: ')
    arribo(cola, x)
    arribo(cola2, x)

print('Los datos ingresados son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)

while not (pila_vacia(pila) and cola_vacia(cola2)):
    x = desapilar(pila)
    y = atencion(cola2)
    if (x == y):
        status = True

if (status == True):
    print('Es palindromo')
else:
    print('No es palindromo')

#Ejercicio 4

cola = Cola()
cola2 = Cola()
cont = 0

while (tamanio(cola) < 10):
    x = randint(0,100)
    arribo(cola, x)

print('Los datos son: ')
for i in range(0, tamanio(cola)):
    print(mover_final(cola))

while not cola_vacia(cola):
    x = atencion(cola)
    for i in range(1, x):
        if ((x % i) == 0):
            cont += 1
    if (cont == 2):
        arribo(cola2, x)

print('Los datos sin números compuestos: ')
for i in range(0, tamanio(cola2)):
    print(mover_final(cola2))

#Ejercicio 5

pila = Pila()
cola = Cola()

while (tamanio(pila) < 10):
    x = int(input('Ingrese numeros: '))
    apilar(pila, x)

while not pila_vacia(pila):
    x = desapilar(pila)
    arribo(cola, x)

print('Los datos invertidos son: ')
while not cola_vacia(cola):
    x = atencion(cola)
    print(x)

#Ejercicio 6

cola = Cola()
cont = 0

while (tamanio(cola) < 5):
    x = randint(0, 10)
    arribo(cola, x)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))

c = randint(0, 10)

for i in range (0, tamanio(cola)):
    x = atencion(cola)
    if (x == c):
        cont += 1

print('La cantidad de ocurrencias de', c, 'es:', cont )

#Ejercicio 7

cola = Cola()

while (tamanio(cola) < 10):
    x = int(input('Ingrese un número: '))
    arribo(cola, x)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))

c = atencion(cola)
atencion(cola)
arribo(cola, c)

print ('Dato a poner al frente:', c)

while not (en_frente(cola) == c):
    mover_final(cola)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))
'''
#Ejercicio 8 TERMINAR

cola = Cola()

x = int(input('Ingrese un número: '))
arribo(cola, x)
while (tamanio(cola) < 10):
    x = int(input('Ingrese un número: '))
    if (x > (en_frente(cola))):
        arribo(cola, x)
    else:
        arribo(cola, x)
        mover_final(cola)

for i in range (0, tamanio(cola)):
    print(mover_final(cola))