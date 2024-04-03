from app import db

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(1024), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)

### Toda função dentro de classe recebe "SELF"
    def to_json(self):
        return{
            'id':self.id,
            'nome':self.nome,
            'senha':self.senha,
            'email':self.email,
            'nascimento':self.nascimento
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id'),
        nome = json_data.get('nome'),
        senha = json_data.get('senha'),
        email = json_data.get('email'),
        nascimento = json_data.get('nascimento')
        return User(id=id, nome=nome, senha=senha, email=email, nascimento=nascimento)
