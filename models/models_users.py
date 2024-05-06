from app import db

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(500), nullable = False)
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


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable = False)
    expiration_at = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return{
            'id':self.id,
            'token':self.token,
            'expiration_at':self.expiration_at
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id'),
        token = json_data.get('token'),
        expiration_at = json_data.get('expiration_at')
        return Token(id=id, token=token, expiration_at=expiration_at)


