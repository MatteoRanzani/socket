import socket
import json
import sys
import random
import os
import time
import threading
import multiprocessing

SERVER_IP = "127.0.0.1"
SERVER_PORT = 22224
BUFFER_SIZE = 1024
NUM_MESSAGES = 15

def genera_richieste(address, port):
    try: 
        start_time_thread = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, SERVER_PORT))
    except:
        print(f"{threading.current_thread().name} errore nel collegamento")

    primoNumero = random.randint(1,20)
    ind=random.randint(0,3)
    oper = ["+" , "-", "*", "/"]
    #print(ind)
    operazione=oper[ind]
    secondoNumero = random.randint(1,20)
    message = {
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero,
        }
    message = json.dumps(message)
    s.sendall(message.encode("UTF-8"))
    data = s.recv(BUFFER_SIZE)
    print("risultato: ",data.decode())
    end_time_thread = time.time()
    print(f"{threading.current_thread().name} execution time = ", end_time_thread - start_time_thread)


if __name__ == '__main__':
    start_time= time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_IP, SERVER_PORT,)) for _ in range(NUM_MESSAGES)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("Total thread time= ", end_time - start_time)
