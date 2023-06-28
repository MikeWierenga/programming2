import socketserver
from http.server import SimpleHTTPRequestHandler as SimpleHandler
import re 
import dataprovider
class ServerHandler(SimpleHandler):
    def send_200(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('dingen','kerl')
        self.end_headers()

    def do_GET(self):
        print(self.path)
        path = self.path.split('/')
        print(path)
        print(len(path))
        if path[1] == 'data':
            d = dataprovider.DataProvider()
        if path[2] == "all":

            self.send_200()
            json = d.get_data()
            self.wfile.write(json.encode('utf-8'))
        
        elif re.search("[0-9]{4}", path[2]) != None and len(path) == 3:
      
            self.send_200()
            json = d.get_data(int(path[2]))
        
            self.wfile.write(json.encode('utf-8'))
        
        elif re.search("[0-9]{4}", path[2]) != None and re.search("[0-9]{4}", path[3]) != None:
            self.send_200()
            json = d.get_data([int(path[2]), int(path[3])])
            self.wfile.write(json.encode('utf-8'))
            
        elif (re.search("[0-9]{4}", path[2]) == None or re.search("[0-9]{4}", path[3]) == None):
            self.send_error(400)
        else:
            self.send_error(404)
    
port = 9000
socketserver.TCPServer.allow_reuse_address = True
http = socketserver.TCPServer(('localhost',port), ServerHandler)
print (f'serving on port {port}')
print(f'localhost/{port}')
http.serve_forever()
