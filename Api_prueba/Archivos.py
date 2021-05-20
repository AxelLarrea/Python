import shelve


def abrir(ruta):
    return shelve.open(ruta)

def cerrar(archivo):
    archivo.close()

def leer(archivo, pos):
    return archivo[str(pos)]

def guardar(archivo, reg):
    """para guardar un nuevo registro"""
    archivo[str(len(archivo))] = reg

def modificar(archivo, pos, reg):
    """modifica un registro existente"""
    archivo[str(pos)] = reg



# class Persona(object):

#     def __init__(self, nombre, dni):
#         self.nombre = nombre
#         self.dni = dni

#     def __str__(self):
#         return self.nombre +' '+ str(self.dni)


# class Persona2(object):
    
#     def __init__(self, nombre, dni, tel):
#         self.nombre = nombre
#         self.dni = dni
#         self.tel = tel

#     def __str__(self):
#         return self.nombre +' '+ str(self.dni)+' '+ str(self.tel)

#file = abrir('jedis.txt')

'''
for i in range(3):
    nombre = input('ingrese nombre')
    dni = int(input('ingrese dni'))
    persona = Persona(nombre, dni)
    guardar(file, persona)
'''
# pos = 0

# while(pos < len(file)):
#     persona = leer(file, pos)
#     pos += 1
#     print(persona)

# cerrar(file)