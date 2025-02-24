# File: /group_chat/server.py

import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

rooms_dict = {}

while True:
    client, addr = server.accept()
    print(f'client.server.accept()::: {client}')
    print(f'addr.server.accept()::: {addr}')
    print()
    client.send(b'ROOM')

    room = client.recv(1024).decode()
    name = client.recv(1024).decode()
    print(f'room::: {room}.')
    print(f'name::: {name}.')

    print()
    if room not in rooms_dict.keys():
        rooms_dict[room] = []

    rooms_dict[room].append(client)
    print(f'rooms_dict::: {room}.')