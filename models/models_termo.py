from app import db

from app import db

class Palavra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palavra = db.Column(db.String(255), nullable=False)

### Toda função dentro de classe recebe "SELF"
    def to_json(self):
        return{
            'id':self.id,
            'palavra':self.palavra
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id'),
        palavra = json_data.get('palavra')
        return Palavra(id=id, palavra=palavra)