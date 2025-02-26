

def broadcast(my_room, my_messagem):
    for i1 in rooms_dict[my_room]:
        if isinstance(my_messagem, str):
            my_messagem = my_messagem.encode()
        i1.send(my_messagem)