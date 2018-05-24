#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','image/png')
		self.end_headers()
		#f = open(curdir + sep + 'logo.png')
		#self.wfile.write(f.read())
		with open(curdir + sep + 'logo.png', 'rb') as file:
			self.wfile.write(file.read())

		return

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' + str(PORT_NUMBER))
	server.serve_forever()

except KeyboardInterrupt:
	server.socket.close()
