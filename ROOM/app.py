from flask import Flask, request, jsonify

app = Flask(__name__)

rooms = [
    {
        'room_id': 0,
        'status_room': 0,
        'player_1_id': 0,
        'player_2_id': 0,
        'player_3_id': 0,
        'player_4_id': 0
    }
]

#Rota POST
@app.route('/create_room', methods=['POST'])
def create_room():
    new_room = request.get_json()
    room_id = new_room['room_id']


    for room in rooms:
        if room['room_id'] == room_id:
            return jsonify({'erro': 'Essa sala já existe'}), 400 
        

    rooms.append(new_room)
    return jsonify({'mensagem': 'Sala criada com sucesso'}), 201       





#Rota DELETE
@app.route('/delete_room/<int:room_id>', methods=['DELETE'])
def delete_room (room_id):

    for room in rooms:
        if room['room_id'] == room_id:
            rooms.remove(room)
            return jsonify({'mensagem': 'sala deletada com sucesso'}), 200
        
    return({'error': 'Sala não encontrado'}), 404









    
app.run(debug=True)