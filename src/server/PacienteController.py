import os, json
from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from server.instance import server

app, api = server.app, server.api

cur_path = os.path.dirname(__file__)
pathJSON = os.path.join(cur_path, '..', 'pacientes.json')


@api.route('/pacientes')
class PatientList(Resource):
  @cross_origin()	
  def get(self, ):
    db = open(pathJSON, 'r', encoding='utf-8')

    jsonDB = json.load(db)

    db.close()
    
    return jsonDB

  def post(self, ):
    response = api.payload
    print(response)
    jsonDB.append(response)
    return response, 200