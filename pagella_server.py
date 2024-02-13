import socket
import json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
BUFFER_SIZE = 1024


diz = {   
    'Antonio Barbera': [   ['Matematica', 8, 1],
                           ['Italiano', 6, 1],
                           ['Inglese', 9.5, 0],
                           ['Storia', 8, 2],
                           ['Geografia', 8, 1]],
    'Giuseppe Gullo': [   ['Matematica', 9, 0],
                          ['Italiano', 7, 3],
                          ['Inglese', 7.5, 4],
                          ['Storia', 7.5, 4],
                          ['Geografia', 5, 7]],
    'Nicola Spina': [   ['Matematica', 7.5, 2],
                        ['Italiano', 6, 2],
                        ['Inglese', 4, 3],
                        ['Storia', 8.5, 2],
                        ['Geografia', 8, 2]]
}

def ricevi_comandi(sock_service, addr_client):
    with sock_service as sock_client:
        while True:
            data=sock_client.recv(BUFFER_SIZE)
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            print(data)
            primoNumero=data['primoNumero']
            operazione=data['operazione']
            secondoNumero=data['secondoNumero']
            if(operazione != 'x' and operazione != '+' and operazione != '-' and operazione != '/'):
                print("operatore non accettabile")
                break
            else:
                if(operazione == 'x'):
                    risultato=primoNumero*secondoNumero
                elif(operazione == '+'):
                    risultato=primoNumero+secondoNumero
                elif(operazione == '-'):
                    risultato=primoNumero-secondoNumero
                else:
                    risultato=primoNumero/secondoNumero

            sock_client.sendall(str(risultato).encode())
            print(risultato)
    print("Connesione chiusa")    
