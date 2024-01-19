import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 22224
BUFFER_SIZE = 1024
NUM_MESSAGES = 5


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))

    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = str(input("Inserisci l operazione: (+, -, *, /, %)"))
    secondoNumero = float(input("Inserisci il secondo numero: "))
    message = {
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero,
    }
    message = json.dumps(message)
    sock_service.sendall(message.encode("UTF-8"))

    data = sock_service.recv(BUFFER_SIZE)
    print("risultato: ",data.decode())