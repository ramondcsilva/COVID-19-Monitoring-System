# -*- coding: utf-8 -*-

import socket, random

# numero randomico para simular dados do oximetro
rnd = random.randint(80,98)

#18.188.134.59
def client(host = 'localhost', port=8080): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address)
    
    # Send data 
    try: 
        while True:
            # Send data 
            message = "Saturacao sanguinea ="
            i = 0
            if i == 0:
                value = rnd
            dif = random.randint(-1,1)
            value = value + dif
            print ("Sending: %s" %message, value, "%")
            message = "Cliente3,Saturacao Sanguinea,"+str(value)
            sock.sendall(message.encode('utf-8')) 
            # Look for the response 
            # amount_received = 0 
            # amount_expected = len(message) 
            # while amount_received < amount_expected: 
            data = sock.recv(254) 
            # amount_received += len(data) 
            # print ("Received: %s" %data)
            i+=1
            if not data:
                break
            
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
        
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
        
    finally:
        sock.close() 
        print ("Closing connection to the server")

client()