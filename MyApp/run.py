from functions import *

if __name__ == '__main__':
    url = 'http://127.0.0.1:5050/'
    token = login(url)
    opc = -1
    while opc != 0:
        print('1. Administrar juegos\n2. Administrar usuarios\n0. Salir')
        opc = int(input())
        if opc == 1:
            print(see_all_games(url, token))