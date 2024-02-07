from flask import Flask,jsonify
from controllers.controller_matchs import get_matchs,matchs
 
app = Flask(__name__)
 
app.route("/matchs", methods=["GET"])(get_matchs)
 
 
@app.route("/matchs/<int:id>", methods= ["GET"])
def get_matches_by_id(id):
    for i, match in enumerate (matchs):
        if id == match["id"]:
            return jsonify(match[i])
 
 
    return jsonify({"Erro":"Partida Nao Encontrada"}),404
 
app.run(debug=True)