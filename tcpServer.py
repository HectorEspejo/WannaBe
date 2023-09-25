#----TCP SERVER----#

import socket

# 'threading' library is used to create multiple threads

import threading

bindIP = "0.0.0.0"

bindPort = 4444

# Server uses IPv4 and will be on TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server starts to listen

server.bind((bindIP, bindPort))

# Maximum backlog connections is 5

server.listen(5)

print("[*] Listening on %s:%d" % (bindIP, bindPort))

# Client handler

def handleClient(clientSocket):
    request = clientSocket.recv(1024)

    print("[*] Received: %s" % request)

    # Sending back a packet

    clientSocket.send(b"ACK!")

    clientSocket.close()

while True:
    # When client connects we receive socket and its details
    client,addr = server.accept()

    print("[*] Accepted connection from %s:%d" % (addr[0],addr[1]))

    # Client thread to handle incoming data

    clientHandler = threading.Thread(target=handleClient,args=(client,))
    clientHandler.start()