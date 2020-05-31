from Cola_Dinamico import Cola, arribo, atencion, cola_vacia, tamanio, en_frente, mover_final
from random import randint
'''
from Colas import Cola, arribo, atencion, cola_vacia, cola_llena, tamanio, en_frente, mover_final

#Ejercicio 1

cola = Cola()
cola2 = Cola()

while not cola_llena(cola):
    x = input('Ingrese las letras deseadas: ')
    arribo(cola, x)
print('Lista de letras: ', cola.datos)

while not cola_vacia(cola):
    x = atencion(cola)
    if ((x != 'a') and (x != 'e') and (x != 'i') and (x != 'o') and (x != 'u')):
        arribo(cola2, x)

while not cola_vacia(cola2):
    x = atencion(cola2)   
    print('Lista de letras sin vocales: ', x)

# Ejercicio 2

cola = Cola()
cola2 = Cola()

while not cola_llena(cola):
    x = int(input('Ingrese los números deseados: '))
    arribo(cola, x)

print('Los datos ingresados son: ', cola.datos)



print('Los datos al revés son: ', cola.datos)        
'''
#Ejercicio 4

cola = Cola()

while not cola_vacia(cola):
    x = randint(0,100)
    arribo(cola, x)
print(cola)