from flask import Flask, request, jsonify

rooms = [
    {
        "room_id":555,
        "status_room":0,
        "player_1_id": 1,
        "player_2_id": 2,
        "player_3_id": 3,
        "player_4_id": 4
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
    return jsonify(rooms)