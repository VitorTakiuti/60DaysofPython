import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1" #client and server must be at the same host web to build up the connection
port = 12345

client_socket.connect(host, port)

message = "Hi, I'm Goku!"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Server Response:{response}")

client_socket.close()