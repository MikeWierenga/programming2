import socketserver
from http.server import SimpleHTTPRequestHandler as SimpleHandler

class ServerHandler(SimpleHandler):
    def do_GET(self):
        print(self.path)
        
        if not self.path == '/data':
            self.send_response(400)
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.send_header('dingen','kerl')
            self.end_headers()
            self.wfile.write('henk'.encode('utf-8'))

port = 9000
socketserver.TCPServer.allow_reuse_address = True
http = socketserver.TCPServer(('localhost',port), ServerHandler)
print (f'serving on port {port}')
http.serve_forever()