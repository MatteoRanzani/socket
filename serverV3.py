import socket
import json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
BUFFER_SIZE = 1024

def ricevi_comandi(sock_service, addr_client):
    while True:
        with sock_service as sock_client:
            data=sock_client.recv(BUFFER_SIZE)
            if not data:
                break
        
                data=data.decode()
                data=json.loads(data)
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
        


def ricevi_connessioni(sock_listen):
    print("In sttesa di connesioni")
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(SERVER_ADDRESS, SERVER_PORT):
    try:
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
        sock_listen.listen(5)
        print("Server in ascolto")
    except socket.error as errore:
        print(f"Qualcosa è andato storto \n{errore}")
    ricevi_connessioni(sock_listen)


if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")