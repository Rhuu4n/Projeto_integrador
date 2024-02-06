rooms = [
    {
        "id":1,
        ""
    }
]



def create_room():
    new_room = request.get_json()
    room_id = new_room['room_id']


    for room in rooms:
        if room['room_id'] == room_id:
            return jsonify({'erro': 'Essa sala já existe'}), 400 
        

    rooms.append(new_room)
    return jsonify({'mensagem': 'Sala criada com sucesso'}), 201       


    
def get_rooms ():
    return (rooms)