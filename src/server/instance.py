from flask import Flask
from flask_restplus import Api
app = Flask(__name__)

# Classe server rest
class Server():
  # construtor do server rest  
  def __init__(self, ):
    self.app = Flask(__name__)
    self.api = Api(self.app,
      version='1.0',
      title='Sample Patient API',
      description='A simple Patient API',
      doc='/docs'    
    )

  # inicia o server rest
  def run(self, ):
    # modo debug false para manipular diretamente os dados
    self.app.run(
      debug=False
    )  
    
# inicia server quando compilado    
server = Server()    