#sockets - passing data between client and server

import socket

#Creating the seerver using socket parameters
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)
print(f"Server waiting for host connection: {host} with the port {port}")

#creating a loop to not stop the code while running
while True:
    client_socket, addr = server_socket.accept()
    #addr receive the IP and the port from the client
    print(f"Connection estabilished with {addr}")
    
    message = client_socket.recv(1024).decode() #message with 1024 bytes
    print(f"Message received: {message}")
    
    client_socket.send("Message Sucessfully received!".encode())
    client_socket.close()
    