# File: /group_chat/test.py

import socket

HOST = 'localhost'
PORT = 55556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

