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

@app.route("/users", methods = ["POST"])
def crt_users():
    New_user = request.get_json()

    for u in users:
        if New_user["id"] == u["id"]:
            return jsonify({"erro:":"id ja existente"}), 409
         
        if New_user["usuario"] == u["usuario"] or New_user["usuario"] == "":
            return jsonify({"erro:":"usuario ja existente ou vazio"}), 409
        
    if len(New_user["senha"]) >= 9:
        return jsonify({"erro":"senha longa demais"})
        
    users.append(New_user)
    return jsonify(users)


@app.route("/users", methods = ["GET"])
def get_users():
    return users

@app.route("/users/<int:id>", methods = ["DELETE"])
def del_aluno(id):
    
     for i, u in enumerate(users):
          if id == u["id"]:
               del users[i]
               return jsonify(users)


app.run(debug=True)