# Importo flask para la configuracion de la api
from flask import *
# Importo request para la gestion de peticiones
import requests

'''
 Creo un metodo grafico para el login del usuario
 Param1 -> Una cadena con el url generico de la pagina
'''
def login(url):
    status = 0
    while status != 201:
        try:
            username = input('Username: ')
            password = input('Password: ')
            token, status = login_user(username, password, url)
            return token
        except Exception as e:
            print(e)

'''
 Creo un metodo para el login del usuario, 
 generando un token para que pueda ver los datos
 Param1 -> Una cadena con el username del user
 Param2 -> Una cadena con la contrasenya del user
 Param3 -> Una cadena con el url generico de la pagina
 Return -> Token del user, codigo de estado VALIDO
'''
def login_user(username, password, url):
    url_completa = url + 'usuarios/login'
    response = requests.post(url_completa, json={'username': username, 'password': password}, headers={'Content-Type': 'application/json'})
    token = response.json().get('token')
    return token, response.status_code

'''
 Creo un metodo para registrar un usuario en la BD
 Param1 -> Una cadena con el username del user
 Param2 -> Una cadena con la contrasenya del user
 Param3 -> Una cadena con el url generico de la pagina
 Return -> Token del user, codigo de estado VALIDO
'''
def register_user(username, password, url):
    url_completa = url + 'usuarios/register'
    response = requests.post(url_completa, json={'username': username, 'password': password}, headers={'Content-Type': 'application/json'})
    token = response.json().get('token')
    return token, response.status_code

'''
 Creo un metodo para ver todos los juegos de la BD
 Param1 -> Una cadena con el url generico de la pagina
 Param2 -> Una cadena con el token del user
 Return -> Lista en metodo Json
'''
def see_all_games(url, token):
    try:
        url_completa = url + 'juegos'
        response = requests.get(url_completa, headers={'Authorization': 'Bearer ' + token})
        if response.status_code == 200:
            result = ''
            for juego in response.json():
                result += f'Id: {juego["id"]}\nNombre: {juego["nombre"]}\n Pegi: {juego["pegi"]}\n Descripcion: {juego["descripcion"]}\n------------------\n'
            return result
        else:
            return 'Ha surgido un error'
    except Exception as e:
        return str(e)

'''
 Creo un metodo para ver solo un juego de la BD
 Param1 -> Una cadena con el url generico de la pagina
 Param2 -> Una cadena con el token del user
 Param3 -> Una cadena con el ID del juego
 Return -> Json del juego pedido, codigo de estado VALIDO
'''
def see_one_game(url, token, id):
    try:
        url_completa = url + 'juegos/' + id
        response = requests.get(url_completa, headers={'Authorization': 'Bearer ' + token})
        if response.status_code == 200:
            result = ''
            result += f'Id: {response.json()["id"]}\nNombre: {response.json()["nombre"]}\n Pegi: {response.json()["pegi"]}\n Descripcion: {response.json()["descripcion"]}\n------------------\n'
            return result
        else:
            return 'Ha surgido un error'
    except Exception as e:
        return str(e)
    
'''
 Creo un metodo para agregar un juego en la BD
 Param1 -> Una cadena con el url generico de la pagina
 Param2 -> Una cadena con el token del user
 Param3 -> Una cadena con el Json del juego
 Return -> Json del juego agregado, codigo de estado VALIDO
'''
def add_game(url, token, json):
    try:
        url_completa = url + 'juegos'
        response = requests.post(url_completa, json=json, headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
        if response.status_code == 200:
            result = ''
            result += f'Id: {response.json()["id"]}\nNombre: {response.json()["nombre"]}\n Pegi: {response.json()["pegi"]}\n Descripcion: {response.json()["descripcion"]}\n------------------\n'
            return result
        else:
            return 'Ha surgido un error'
    except Exception as e:
        return str(e)
    
'''
 Creo un metodo para modificar un juego entero de la BD
 Param1 -> Una cadena con el url generico de la pagina
 Param2 -> Una cadena con el token del user
 Param3 -> Una cadena con el Json del juego modificado
 Param4 -> Una cadena con el ID del juego
 Return -> Json del juego modificado, codigo de estado VALIDO
'''
def modify_game(url, token, json, id):
    try:
        url_completa = url + 'juegos/' + id
        response = requests.put(url_completa, json=json, headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
        if response.status_code == 200:
            result = ''
            result += f'Id: {response.json()["id"]}\nNombre: {response.json()["nombre"]}\n Pegi: {response.json()["pegi"]}\n Descripcion: {response.json()["descripcion"]}\n------------------\n'
            return result
        else:
            return 'Ha surgido un error'
    except Exception as e:
        return str(e)
    
'''
 Creo un metodo para eliminar un juego de la BD por su ID
 Param1 -> Una cadena con el url generico de la pagina
 Param2 -> Una cadena con el token del user
 Param3 -> Una cadena con el ID del juego
 Return -> Json del juego eliminado, codigo de estado VALIDO
'''
def delete_game(url, token, id):
    try:
        url_completa = url + 'juegos/' + id
        response = requests.delete(url_completa, headers={'Authorization': 'Bearer ' + token})
        if response.status_code == 200:
            return 'Se ha eliminado correctamente'
        else:
            return 'Ha surgido un error al eliminar'
    except Exception as e:
        return str(e)