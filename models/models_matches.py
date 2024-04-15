from app import db

class Matches(db.Model):

    Jogador_ID = db.Column(db.Integer)
    id_sala = db.Column(db.Integer)
    Ordem = db.Column(db.Integer)
    Moedas = db.Column(db.Integer)
    Carta_1 = db.Column(db.Integer, nullable=False)
    Carta_2 = db.Column(db.Integer, nullable=False)
    Acao = db.Column(db.Integer)
    Afetado = db.Column(db.Integer)
    id_partida = db.Column(db.Integer, primary_key=True) 

    def to_json(self):
        return{            

            'Jogador_ID': self.Jogador_ID,
            'id_sala': self.id_sala,
            'Ordem': self.Ordem,
            'Moedas': self.Moedas,
            'Carta_1': self.Carta_1,
            'Carta_2': self.Carta_2,
            'Acao': self.Acao,
            'Afetado': self.Afetado,
            'id_partida': self.id_partida
        }
            
        
    @staticmethod
    def from_json(json_data):
            Jogador_ID = json_data.get('Jogador_ID')
            id_sala = json_data.get('id_sala')
            Ordem = json_data.get('Ordem')
            Carta_1 = json_data.get('Carta_1')
            Carta_2 = json_data.get('Carta_2')
            Acao = json_data.get('Acao')
            Afetado = json_data.get('Afetado')
            id_partida = json_data.get('id_partida')
            return Matches(Jogador_ID=Jogador_ID, id_sala=id_sala, Ordem=Ordem, Carta_1=Carta_1, Carta_2=Carta_2, Acao=Acao, Afetado=Afetado, id_partida=id_partida  )