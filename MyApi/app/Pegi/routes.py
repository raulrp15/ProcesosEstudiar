# Importo flask para la configuracion de la api
from flask import *
# Importo jwt_required para requerir un token a las gestiones
from flask_jwt_extended import jwt_required
# Importo las funciones de leer y escribir ficheros
from app.GestFicheros.Gestion import *

'''
 Creo una instancia flask para la gestion de las rutas
 __name__ es una variable especial en python para
 que recoga el nombre del modulo en el que se encuentra
'''
app = Flask(__name__)

'''
 Creo un BluePrint para gestionar las peticiones a la URL de pegi
'''
pegisBP = Blueprint('pegi', __name__)

'''
 Creo una cadena con la ruta hacia el fichero .json de pegi
'''
ruta_pegis = 'MyApi/app/json/pegi.json'

'''
 Creo un metodo para autoincrementar el id del pegi insertado
 Return -> El ID siguiente al mas alto encontrado en la BD
'''
def find_next_id_pegi():
    return max(pegi['id'] for pegi in leer_fichero(ruta_pegis)) + 1

'''
 Creo un metodo para recoger todos los pegis de la la BD
 Return -> Lista en metodo Json
'''
@pegisBP.get('/')
@jwt_required()
def get_all_pegis():
    pegis = leer_fichero(ruta_pegis)
    return jsonify(pegis)

'''
 Creo un metodo para recoger solo un pegi mediante su ID
 Return -> Json del pegi pedido, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@pegisBP.get('/<int:id>')
@jwt_required()
def get_one_pegi(id):
    pegis = leer_fichero(ruta_pegis)
    for pegi in pegis:
        if pegi['id'] == id:
            return pegi, 200
    return {'error': 'Pegi no encontrado'}, 404

'''
 Creo un metodo para recoger todos los juegos de ese pegi
 Return -> Lista de todos los juegos de ese pegi, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@pegisBP.get('/<int:id>/juegos')
@jwt_required()
def get_juegos_pegi(id):
    juegos = leer_fichero(ruta_pegis)
    juegosPegi = []
    for juego in juegos:
        if juego['pegi'] == id:
            juegosPegi.append(juego)
    if len(juegosPegi) > 0:
        return jsonify(juegosPegi), 200
    return {'error': 'Pegi no encontrado'}, 404

'''
 Creo un metodo para añadir un pegi a la BD
 Return -> Json del pegi añadido, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@pegisBP.post('/')
@jwt_required()
def add_pegi():
    pegis = leer_fichero(ruta_pegis)
    if request.is_json:
        pegi = request.get_json()
        pegi['id'] = find_next_id_pegi()
        pegis.append(pegi)
        escribir_fichero(ruta_pegis, pegis)
        return pegis, 201
    return {'error': 'Contenido debe ser Json'}, 415

'''
 Creo un metodo para modificar un archivo entero *PUT*
 o solo un campo *PATCH*
 Return -> Json del pegi modificado, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@pegisBP.put('/<int:id>')
@pegisBP.patch('/<int:id>')
@jwt_required()
def update_game(id):
    pegis = leer_fichero(ruta_pegis)
    if request.is_json:
        pegiAct = request.get_json()
        for pegi in pegis:
            if pegi['id'] == id:
                pegi.update(pegiAct)
                escribir_fichero(ruta_pegis, pegis)
                return pegi, 200
        return {'error': 'Pegi no encontrado'}, 404

'''
 Creo un metodo para borrar un pegi mediante su ID
 Return -> Json del pegi borrado, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@pegisBP.delete('/<int:id>')
@jwt_required()
def delete_game(id):
    pegis = leer_fichero(ruta_pegis)
    for pegi in pegis:
        if pegi['id'] == id:
            pegis.remove(pegi)
            escribir_fichero(ruta_pegis, pegis)
            return '{}', 200
    return {'error': 'Pegi no encontrado'}, 404