# File: /group_chat/test.py

import socket #1:

HOST = 'localhost' #2:
PORT = 55556 #2:

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #3:
client.connect((HOST, PORT)) #3:

message = client.recv(1024).decode() #4:
print(f'message.client.recv::: {message}') #4:

if message == 'ROOM': #5:
    client.send(b'Games') #5:
    client.send(b'Edson') #5: