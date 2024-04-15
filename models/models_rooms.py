from app import db

class Salas(db.Model):
    id_sala = db.Column(db.Integer , primary_key=True)
    jogadorAtual = db.Column(db.String(255), nullable=False)
    estadoSala = db.Column(db.String(1024))
    numeroJogadores = db.Column(db.Integer)

    def to_json(self):
        return{
            'id_sala':self.id_sala,
            'jogadorAtual':self.jogadorAtual,
            'estadoSala':self.estadoSala,
            'numeroJogadores':self.numeroJogadores
        }

    @staticmethod
    def from_json(json_data):
        id_sala = json_data.get('id_sala'),
        jogadorAtual = json_data.get('jogadorAtual'),
        estadoSala = json_data.get('estadoSala'),
        numeroJogadores = json_data.get('numeroJogadores')
        return Salas(id_sala=id_sala, jogadorAtual=jogadorAtual, estadoSala=estadoSala, numeroJogadores=numeroJogadores)