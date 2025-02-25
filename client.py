# File: /group_chat/client.py

import socket #1:
import threading #1:
from tkinter import * #1:
import tkinter #1:
from tkinter import simpledialog #1:

class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 55556

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(HOST, PORT)

        login = Tk() # tkinter *
        login.withdraw() # tkinter *

        self.loaded_window = False
        self.active = True

        self.name = simpledialog.askstring('Name', 'Enter your name: ', parent=login)