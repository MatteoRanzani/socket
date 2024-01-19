import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    primoNumero=float(input("inserisci primo numero"))
    operazione=input("inserisci operazione")
    secondoNumero=float(input("inserisci secondo numero"))
    messaggio={
        "primoNumero":primoNumero,
        "operazione":operazione,
        "secondoNumero":secondoNumero
    }
    messaggio=json.dumps(messaggio)
    sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
    data=sock.recv(1024)
    print("risultato: ", data.decode())