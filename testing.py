

def broadcast(my_room, my_messagem):
    for i1 in rooms_dict[my_room]:
        if isinstance(my_messagem, str):
            my_messagem = my_messagem.encode()
        i1.send(my_messagem)

def send_message(name, room, client):
    while True:
        listen_message = client.recv(1024)
        my_message = f'{name} {listen_message.decode()}\n'
        broadcast(room, my_message)