# Importo flask para la configuracion de la api
from flask import *
# Importo las funciones de leer y escribir ficheros
from app.GestFicheros.Gestion import *
# Importo bcrypt para encriptar contrasenyas
import bcrypt
from bcrypt import *
# Importo create_access_token para generar el acceso mediante token
from flask_jwt_extended import create_access_token

'''
 Creo una cadena con la ruta hacia el fichero .json de users
'''
ruta_users = 'MyApi/app/json/users.json'

'''
 Creo un BluePrint para gestionar las peticiones a la URL de users
'''
usersBP = Blueprint('usuarios', __name__)

'''
 Creo un metodo para registrar un user en la BD
 Return -> Token del user, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@usersBP.post('/register')
def register_user():
    users = leer_fichero(ruta_users)
    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password, salt).hex()
        user['password'] = hash_password
        users.append(user)
        escribir_fichero(ruta_users, users)
        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    else:
        return {'error': 'Contenido debe ser Json'}, 415

'''
 Creo un metodo para loguear un users de la BD
 Return -> Token del user, codigo de estado VALIDO
 Return -> Json con mensaje de error, codigo de estado ERROR
'''
@usersBP.post('/login')
def login_user():
    if request.is_json:
        user = request.get_json()
        username = user['username']
        password = user['password']
        users = leer_fichero(ruta_users)
        for u in users:
            if u['username'] == username and bcrypt.checkpw(password.encode('utf-8'), bytes.fromhex(u['password'])):
                return {'token': create_access_token(identity=username)}, 201
        return None, 401
    return {'error': 'Contenido debe ser Json'}, 415

@usersBP.get('/login')
def get_users():
    users = leer_fichero(ruta_users)
    return jsonify(users)