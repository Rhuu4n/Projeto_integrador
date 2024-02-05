from flask import Flask, request, jsonify


app = Flask(__name__)

users = [
     {
          "id":1,
          "usuario":"Rhuan",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     },
     {
          "id":2,
          "usuario":"Hugo",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     }
]

@app.route("/users/<int:id>", methods = ["DELETE"])
def del_aluno(id):
    
     for i, u in enumerate(users):
          if id == u["id"]:
               del users[i]
               return jsonify(users)
          
app.run(debug=True)