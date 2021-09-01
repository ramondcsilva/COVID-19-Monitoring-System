# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:03:51 2021

@author: Ramon Silva
"""

import socket, time, threading as th
from ServerController import UpdateDataWriteJSON

class ServerTCP(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print('Server Iniciado...')
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            th.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                
                if data:
                    # Set the response to echo back the recieved data 
                    response = data
                    client.send(response)                    
                    UpdateDataWriteJSON(data) 
                    
                else:
                    dataSave = response.decode('utf-8').split(",")
                    raise print(dataSave[0],' Desconectado.')
                    
                time.sleep(2)
                
            except:
                client.close()
                return False
    
    def closeCliente(self, client):
        client.close()        

    def closeServer(self):
        self.sock.close
        
        
if __name__ == "__main__":
    host = 'localhost'
    port = 8080
    ServerTCP(host,port).listen()