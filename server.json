import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("server in attesa di messaggi..")
while True:
    data=sock.recv(1024)
    if not data:
        break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']
    print(primoNumero)
    print(operazione)
    print(secondoNumero)
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
    print(risultato)