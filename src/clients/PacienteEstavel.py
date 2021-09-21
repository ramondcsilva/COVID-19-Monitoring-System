# -*- coding: utf-8 -*-

import socket, random

# numero randomico para simular dados do oximetro
rndTemperatura = 36 #ºCelsius
rndArterial = 110 #mmHg
rndRespiratorio = 10 #movimento/minuto
rndCardiaco = 90 #b/minuto
rndSaturacao = 96 # Porcetagem

# Funcao que inicia a conexão do cliente com o ServerTCP
def client(host = 'localhost', port=8080): 
    # Cria um  TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta o Socket com o Server 
    server_address = (host, port) 
    print ("Conectando ao endereco %s:%s" % server_address) 
    sock.connect(server_address)
    
    # Envia os dados
    try: 
        while True:
            message = "Saturacao sanguinea ="
            i = 0
            # Inicia as variaveis com o valor randomico
            if i == 0:
                valueTemp = rndTemperatura
                valueSatu = rndSaturacao
                valueResp = rndRespiratorio
                valueCard = rndCardiaco
                valueArte = rndArterial
            
            
            #Limita os valores maximos
            if valueTemp == 40:
                valueTemp = valueTemp + random.randint(-1,0)
            if valueSatu == 98:
                valueSatu = valueSatu + random.randint(-1,0)
            if valueResp == 30:
                valueResp = valueResp + random.randint(-1,0)
            if valueCard == 121:
                valueCard = valueCard + random.randint(-1,0)
            if valueArte == 131:
                valueArte = valueArte + random.randint(-1,0)
                
            #Limita os valores minimos
            if valueTemp == 35:
                valueTemp = valueTemp + 1
            if valueSatu == 84:
                valueSatu = valueSatu + 1
            if valueResp == 8:
                valueResp = valueResp + 1
            if valueCard == 50:
                valueCard = valueCard + 1
            if valueArte == 70:
                valueArte = valueArte + 1    
                
            
            
            #print ("Enviando o dado: %s" %message, valueSatu, "%")
            # Envia mensagem para o Server
            message = "4,Nome,Kuro,Idade,26,Temperatura,"+str(valueTemp)+",PressaoArterialMaxima,"+str(valueArte)+",FrequenciaRespiratoria,"+str(valueResp)+",FrequenciaCardiaca,"+str(valueCard)+",SaturacaoSanguinea,"+str(valueSatu)+",Estado,x,Pontuacao,00"
            sock.sendall(message.encode('utf-8')) 
            
            # Recebe resposta do serverTCP
            data = sock.recv(2048) 
            
            i+=1
            if not data:
                break
            
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
        
    except Exception as e:         
        print ("Other exception: %s" %str(e)) 
        
    finally: 
        # Fecha conexao
        sock.close() 
        print ("Fechando a conexao com o server...")
        
client()