from flask import Flask
from flask_restplus import Api
app = Flask(__name__)

class Server():
  def __init__(self, ):
    self.app = Flask(__name__)
    self.api = Api(self.app,
      version='1.0',
      title='Sample Patient API',
      description='A simple Patient API',
      doc='/docs'    
    )


  def run(self, ):
    self.app.run(
      debug=False
    )  
    
server = Server()    