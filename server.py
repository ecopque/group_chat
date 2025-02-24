# File: /group_chat/server.py

import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

rooms_dict = {}

def broadcast(my_room, my_message):
    for i1 in rooms_dict[my_room]:
        if isinstance(my_message, str):
            my_message = my_message.encode()
        # i1.send(my_message)
        print(i1)

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
    print(f'rooms_dict::: {rooms_dict}.')

    print(f'Status: {name} connected to room {room}.')

    broadcast(room, 'Entered the room.')