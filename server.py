# File: /group_chat/server.py

import socket #1:
import threading #1:

HOST = 'localhost' #2:
PORT = 55556 #2:

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #3:
server.bind((HOST, PORT)) #3:
server.listen() #3:

rooms_dict = {} #6:

def broadcast(my_room, my_message): #7:
    for i1 in rooms_dict[my_room]: #7:
        if isinstance(my_message, str): #7:
            my_message = my_message.encode() #7:
        i1.send(my_message) #7:

def send_message(name, room, client): #8:
    while True: #8:
        listen_message = client.recv(1024) #8:
        my_message = f'{name} {listen_message.decode()}\n' #8:
        broadcast(room, my_message) #8:
        
while True: #4:
    client, addr = server.accept() #4:
    print(f'client.server.accept()::: {client}') #4:
    print(f'addr.server.accept()::: {addr}') #4:
    print()
    client.send(b'ROOM') #4:

    room = client.recv(1024).decode() #5:
    name = client.recv(1024).decode() #5:
    print(f'room::: {room}.') #5:
    print(f'name::: {name}.') #5:

    print()
    if room not in rooms_dict.keys(): #6:
        rooms_dict[room] = [] #6:

    rooms_dict[room].append(client) #6:
    print(f'rooms_dict::: {rooms_dict}.') #6:
    print(f'Status: {name} connected to room {room}.') #6:

    broadcast(room, f'{name} entered the room.\n')
    thread = threading.Thread(target=send_message, args=(name, room, client)) #8:
    thread.start() #8: