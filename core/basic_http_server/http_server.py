from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

class HTTPRequestHangler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello world")

    def do_POST(self):
        pass


def check_shutdown_command(httpd):
    while True:
        cmd = input("To shutdown server type enything >>")
        if cmd:
            httpd.shutdown()
            break


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8002), HTTPRequestHangler)        
    thread_httpd = Thread(target=httpd.serve_forever)
    thread_httpd.start()

    check_shutdown_command(httpd)

