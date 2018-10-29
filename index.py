from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from os import curdir, sep
import cgi

memory = []
form = '''<!DOCKTYPE html>
                <title>Udacian</title>
                <form method="POST" action="http://localhost:8000/">
                    <textarea name="name">name</textarea>
                    <br>
                    <textarea name="city">city</textarea>
                    <br>
                    <textarea name="enrollment">enrollment</textarea>
                    <br>
                    <textarea name="nanodegree">nanodgree</textarea>
                    <br>
                    <textarea name="status">status</textarea>
                    <br>
                    <button type="submit">Post it!</button>
                </form>
                <pre>
                    {}
                </pre> 
            '''

class MessaageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        incomingForm = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                    'REQUEST_METHOD':'POST',
                    'CONTENT_TYPE':self.headers['Content-Type']
                })
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Response".encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(form.encode())
        


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessaageHandler)
    httpd.serve_forever()