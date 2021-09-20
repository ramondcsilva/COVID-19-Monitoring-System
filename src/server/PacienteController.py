import os, json
from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS, cross_origin

# Define um app rest com o flask
app = Flask(__name__)
# Define o uso de Cors para habilitar conexoes diversas
cors = CORS(app)
# Configura o header do cors
app.config['CORS_HEADERS'] = 'Content-Type'

from server.instance import server

# inicia instancia do server rest
app, api = server.app, server.api

# define o local do json que sera usado
cur_path = os.path.dirname(__file__)
pathJSON = os.path.join(cur_path, '..', 'pacientes.json')


# Aplica uma rota para transporte e aceitacao de dados
@api.route('/pacientes')
class PatientList(Resource):

  # Caso algum protocolo HTTP no metodo get seja requisitado, ele devolve o JSON onde eh guardado os pacientes
  @cross_origin()	
  def get(self, ):
    # abre o arquivo json
    db = open(pathJSON, 'r', encoding='utf-8')
    # carrega ele como json
    jsonDB = json.load(db)
    # fecha arquivo
    db.close()
    # devolve json requisitado
    return jsonDB

  def post(self, ):
    response = api.payload
    print(response)
    #jsonDB.append(response)
    return response, 200