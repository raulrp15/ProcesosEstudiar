# Importo app para generar una pagina en estado local
from app import app

''' Creo una funcion main para crear la pagina '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)