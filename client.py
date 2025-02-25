# File: /group_chat/client.py

import socket #1:
import threading #1:
from tkinter import * #1:
import tkinter #1:
from tkinter import simpledialog #1:

class Chat: #2:
    def __init__(self): #2:
        HOST = 'localhost' #2:
        PORT = 55556 #2:

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #2:
        self.client.connect((HOST, PORT)) #2:

        login = Tk() #3: # tkinter * # Instance/GUI graphical interface.
        login.withdraw() #3: # tkinter * # Hide the main window.

        self.loaded_window = False #3: # Has not yet been loaded or initialized.
        self.active = True #3: # Ready to send and receive messages.

        self.name = simpledialog.askstring('Name', 'Enter your name: ', parent=login) #3: # dialog box will appear over the login window.
        self.room = simpledialog.askstring('Room', 'Enter the room: ', parent=login) #3:
        
        thread = threading.Thread(target=self.connect) #7:
        thread.start() #7:

        self.window() #4:

    def window(self): #4:
        self.root = Tk() #4:
        self.root.geometry('800x800') #4:
        self.root.title('Group Chat') #4:

        self.text_box = Text(self.root) #4:
        self.text_box.place(relx=0.05, rely=0.01, width=700, height=600) #4:

        self.send_message = Entry(self.root) #4:
        self.send_message.place(relx=0.05, rely=0.8, width=500, height=20) #4:

        self.button_send = Button(self.root, text='Send', command=self.Send_Message) #5:
        self.button_send.place(relx=0.7, rely=0.8, width=100, height=20) #5:
        self.root.protocol('WM_DELETE_WINDOW', self.close) #5:

        self.root.mainloop() #4: # Make window say open.

    def close(self): #6:
        self.root.destroy() #6:
        self.client.close() #6:

    def connect(self): #7:
        while True: #7:
            received = self.client.recv(1024) #7:
            if received == b'ROOM': #7:
                self.client.send(self.room.encode()) #7:
                self.client.send(self.name.encode()) #7:
            else:
                self.text_box.insert('end', received.decode()) #7:

    def Send_Message(self): #8:
        message = self.send_message.get()
        self.client.send(message.encode())

chat = Chat()