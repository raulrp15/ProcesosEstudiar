# Importo flask para la configuracion de la api
from flask import *
# Importo JWTManager para requerir un token a las gestiones
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
 Creo un BluePrint para gestionar las peticiones a la URL de juegos
'''
juegosBP = Blueprint('juegos', __name__)

'''
 Creo una cadena con la ruta hacia el fichero .json de juegos
'''
ruta_juegos = 'MyApi/app/json/juegos.json'

'''
 Creo un metodo para autoincrementar el id del juego insertado
 Return -> El ID siguiente al mas alto encontrado en la BD
'''
def find_next_id_game():
    return max(juego['id'] for juego in leer_fichero(ruta_juegos)) + 1

'''
 Creo un metodo para recoger todos los juegos de la la BD
 Return -> Lista en metodo Json
'''
@juegosBP.get('/')
@jwt_required()
def get_all_games():
    juegos = leer_fichero(ruta_juegos)
    return jsonify(juegos)

'''
 Creo un metodo para recoger solo un juego mediante su ID
 Return -> Json del juego pedido, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@juegosBP.get('/<int:id>')
@jwt_required()
def get_one_game(id):
    juegos = leer_fichero(ruta_juegos)
    for juego in juegos:
        if juego['id'] == id:
            return juego, 200
    return {'error': 'Juego no encontrado'}, 404

'''
 Creo un metodo para añadir un juego a la BD
 Return -> Json del juego añadido, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@juegosBP.post('/')
@jwt_required()
def add_game():
    juegos = leer_fichero(ruta_juegos)
    if request.is_json:
        juego = request.get_json()
        juego['id'] = find_next_id_game()
        juegos.append(juego)
        escribir_fichero(ruta_juegos, juegos)
        return juegos, 201
    return {'error': 'Contenido debe ser Json'}, 415

'''
 Creo un metodo para modificar un archivo entero *PUT*
 o solo un campo *PATCH*
 Return -> Json del juego modificado, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
