from flask import Flask #, flash
from flask import render_template, jsonify, request, redirect, url_for
from Archivos import abrir, leer, cerrar, guardar
from Arbol_Binario import insertar_nodo, inorden, por_nivel, busqueda, busqueda_proximidad

app = Flask(__name__)

arbol_nombre = None
arbol_ranking = None
arbol_especie = None

jedis = []

pos = 0

file = open('jedis.dat')
linea = file.readline()
pos = 0
while linea:
    linea = linea.replace('\n', '')
    jedis.append(linea)
    arbol_nombre = insertar_nodo(arbol_nombre, linea.split(';')[0], pos)
    arbol_ranking = insertar_nodo(arbol_ranking, linea.split(';')[1], pos)
    arbol_especie = insertar_nodo(arbol_especie , linea.split(';')[2], pos)
    pos += 1
    linea = file.readline()    
file.close()

# while (pos <len(file)):
#     jedi = leer(file, pos)
#     jedis.append(jedi)
#     arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
#     arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
#     arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
#     pos += 1

# cerrar(file)


@app.route('/')
def index():
    return render_template('/index.html', jedis = jedis, arbol = arbol_nombre)

@app.route('/inorden')
def inorden_nombre():
    jedis_orden = []
    file = abrir('../jedis')
    inorden_name(arbol_nombre, file, jedis_orden)
    cerrar(file)
    return render_template('/index.html', jedis = jedis_orden)

@app.route('/buscar')
def buscar_jedi():
    return render_template('/buscar.html')

@app.route('/buscar_nombre', methods=['POST'])
def buscar_jedi_nombre():
    nombre = str(request.form['valor1'])
    pos = busqueda(arbol_nombre, nombre)
    
    if(pos is not None):
        file = abrir('../jedis')
        jedi = leer(file, pos.nrr)
        cerrar(file)
        return render_template('/detalle.html', jedi=jedi)
    else:
        return render_template('/buscar.html')



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)