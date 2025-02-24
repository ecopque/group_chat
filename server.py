# File: /group_chat/server.py

import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    client, addr = server.accept()
    print(f'client.server.accept()::: {client}')
    print(f'addr.server.accept()::: {addr}')
    print()
    client.send(b'ROOM')
    room = client.recv(1024).decode()
    name = client.recv(1024).decode()
    print(room)
    print(name)