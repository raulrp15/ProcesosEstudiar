# Importo flask para la configuracion de la api
from flask import *
# Importo JWTManager para el manejo de tokens
from flask_jwt_extended import JWTManager
# Importo el Blueprint de juegos
from app.Juegos.routes import juegosBP

# Importo secrets para generar una criptografia segura
import secrets

'''
 Creo una instancia flask para la gestion de las rutas
 __name__ es una variable especial en python para 
 que recoga el nombre del modulo en el que se encuentra
'''
app = Flask(__name__)

'''
 Configuro el token de la app 
 para que no sea la misma cada vez que se inicie
'''
app.config['JWT_SECRET_KET'] = secrets.token_hex(16)

''' Se guarda en una variable el token '''
jwt = JWTManager(app)

'''
 Registro los blueprints para cada pagina
 Facilita el manejo de las URLs de la pagina
'''
app.register_blueprint(juegosBP, url_prefix='/juegos')
app.register_blueprint(pegiBP, url_prefix='/pegi')
app.register_blueprint(usersBP, url_prefix='/usuarios')
