import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
from EMPLOYEE import EMPLOYEE
from POST import POST
from HOLIDAY import HOLIDAY
import Json
from mock import json_response

import json


HOST_NAME = 'localhost'
PORT_NUMBER = 9000

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def GetEmployee(self, p):
        if len(p) == 4:
            return Json.GetAll(EMPLOYEE(), conn)
            id = int(p[3])
            return Json.Stringify(EMPLOYEE._Find(id, conn))

    def Send200(self,mess):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(mess.json_response(body={"pay": {"lo": "ad"}}, headers={"i-like": "i-like"}))
        return

    def SendError(self,status,mess):
        self.send_response(status)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(mess.encode('utf-8'))
        return

    def GetData(self):
     if not self.headers.__contains__('Content-type'):
      return None
     h = self.headers.__getitem__('Content-type')
     n = int(h)
     return str(self.rfile.read(n),'utf-8')


    def do_GET(self):
        try:
            p = self.path.split('/')
            if len(p) >= 3:
                if p[2] == 'Employee': self.Send200(self.GetEmployee(p))
                return
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
    #
    # self.client.stub(
    #     request(),
    #     json_response(code=207, body={"pay": {"lo": "ad"}})
    # )
    #

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


# if __name__ == "__main__":
#     # my_data = js_r('num.json')
#     # print(my_data)
