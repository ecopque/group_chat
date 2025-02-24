# File: /group_chat/test.py

import socket

HOST = 'localhost'
PORT = 55556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = client.recv(1024).decode()
print(f'message.client.recv::: {message}')

if message == 'ROOM':
    client.send(b'Games')
    client.send(b'Edson')