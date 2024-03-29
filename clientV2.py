import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 22018
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(NUM_MESSAGES):
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = str(input("Inserisci l operazione: (+, -, *, /, %)"))
    secondoNumero = float(input("Inserisci il secondo numero: "))
    message = {
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero,
    }
    message = json.dumps(message)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((SERVER_IP, SERVER_PORT))
        sock_service.sendto(message.encode("UTF-8"), (SERVER_IP,SERVER_PORT))
        data = sock_service.recv(BUFFER_SIZE)
    print("risultato: ",data.decode())