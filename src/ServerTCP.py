# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

# Biblioteca e modulos importados
import socket, time, threading as th
from ServerController import UpdateDataWriteJSON

# Classe Server 
class ServerTCP(object):
    # Construtor da Classe
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.sock.bind((self.host, self.port))

    # Funcao de escuta e troca de dados
    def listen(self):
        # Deixa o server em modo de escuta
        self.sock.listen(5)
        print('Server Iniciado...')
        
        
        while True:
            # Aceita conexao do cliente
            client, address = self.sock.accept()
            # Espera um tempo minimo
            client.settimeout(60)
            # Cria thread com a funcionalidade do metodo que repete requisicoes de um cliente conectado 
            th.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        # define o tamanho da mensagem recebida
        size = 2048
        while True:
            try:
                # mensagem recebida do clienteTCP
                data = client.recv(size)
                
                if data:
                    # Manda resposta de volta ao clienteTCP 
                    response = data
                    client.send(response)               
                    # Funcao que guarda dados recebidos do cliente em um JSON
                    UpdateDataWriteJSON(data) 
                    
                else:
                    # Caso o cliente não mande mais dados, ele salva seu nome
                    dataSave = response.decode('utf-8').split(",")
                    raise print(dataSave[0],' Desconectado.')
                    
                time.sleep(2)
                
            except:
                # Desconecta o cliente
                client.close()
                return False
    
    # Desconecta cliente
    def closeCliente(self, client):
        client.close()        

    # Fecha o Server
    def closeServer(self):
        self.sock.close
        

# Inicia o Server a partir de uma Classe Server, porta e ip     
if __name__ == "__main__":
    host = 'localhost'
    port = 8080
    ServerTCP(host,port).listen()