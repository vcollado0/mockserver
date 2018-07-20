import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

HOST_NAME = 'localhost'
PORT_NUMBER = 9000




class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def Send200(self,mess):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(mess.encode('utf-8')) #3.4
        #  self.wfile.write(codecs.encode(mess,'utf-8')) #2.7
        return

    def SendError(self,status,mess):
        self.send_response(status)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(mess.encode('utf-8')) #3.4
        #  self.wfile.write(codecs.encode(mess,'utf-8')) #2.7
        return

    def GetData(self):
     # h = self.headers.getheader('Content-Length') #2.7
     # if h == None #2.7
     if not self.headers.__contains__('Content-type'): #3.4
      return None
     h = self.headers.__getitem__('Content-type') #3.4
     n = int(h)
     return str(self.rfile.read(n),'utf-8') #3.4
     # return codecs.decode(self.rfile.read(n),'utf-8') #2.7

    def do_GET(self):
        try:
            self.SendError(400,'Expected one of Employee/,Post/,Holiday/')
        except (Exception) as e:
            self.SendError(403,sys.exc_info()[1])
            return

    def do_POST(self):
        try:
            s = self.GetData()
            self.SendError(400,'Expected one of Employee/,Post/,Holiday/')
        except (Exception) as e:
            self.SendError(500,sys.exc_info()[1])
            return

    def log_request(self, code=None, size=None):
        """Selectively log an accepted request."""
        return

if __name__ == '__main__':
    conn = sqlite3.connect('Payroll.db')
    print('Starting server, use <Ctrl-C> to stop')
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HTTPServer_RequestHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
    print('^C received, shutting down server')
