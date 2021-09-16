# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:20:05 2021

@author: Ramon Silva
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/HttpClient.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

if __name__ == "__main__":
    httpd = HTTPServer(('localhost',9090),Serv)
    httpd.serve_forever()