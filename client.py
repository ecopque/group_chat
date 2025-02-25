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
        self.client.connect((HOST, PORT))

        login = Tk() # tkinter * # Instance/GUI graphical interface.
        login.withdraw() # tkinter * # Hide the main window.

        self.loaded_window = False # Has not yet been loaded or initialized.
        self.active = True # Ready to send and receive messages.

        self.name = simpledialog.askstring('Name', 'Enter your name: ', parent=login) # dialog box will appear over the login window.
        self.room = simpledialog.askstring('Room', 'Enter the room: ', parent=login)

    def window(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('Group Chat')

chat = Chat()