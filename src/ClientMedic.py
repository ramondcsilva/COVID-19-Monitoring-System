# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:20:05 2021

@author: Ramon Silva
"""

import requests, time

url = 'http://127.0.0.1:5000/pacientes'

from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/test.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))



#while True: 
#    response = requests.get(url)
#    data = response.json()
#    time.sleep(5)
#    print(data['Cliente1'])
#


if __name__ == "__main__":
    httpd = HTTPServer(('localhost',9999),Serv)
    httpd.serve_forever()