# Importo json para poder cargar y añadir Jsons a un archivo .json
import json

'''
 Creo un metodo que lee un fichero .json
 Param1 -> Una cadena con la ruta del archivo .json
 Return -> Un objeto con todo el json de ese archivo
'''
def leer_fichero(ruta):
    archivo = open(ruta, 'r')
    objeto = json.load(archivo)
    archivo.close()
    return objeto

''' 
 Creo un metodo que lee inserta en un fichero .json 
 todo el json recibido, sobrescribiendolo
 Param1 -> Una cadena con la ruta del archivo .json
 Param2 -> Un objeto con cadenas Json
'''
def escribir_fichero(ruta, objeto):
    archivo = open(ruta, 'w')
    json.dump(objeto, archivo)
    archivo.close()