from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import mimetypes
from pathlib import Path
import socket


class HttpStatus():
    OK = 200
    NOT_FOUND = 404
    FOUND = 302


class ServerConfig:
    HOST = "0.0.0.0"
    SOCKET_PORT = 5001
    HTTP_SERVER_PORT = 3000
    BASE_DIR = Path(__file__).resolve().parent.parent


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def send_data_to_socket(slef, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ServerConfig.HOST, ServerConfig.SOCKET_PORT))
            sock.sendall(data)
    
    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-length"]))     
        self.send_data_to_socket(data)
        self.send_response(HttpStatus.FOUND)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        pr_url = urlparse(self.path)
        match pr_url.path:
            case "/":
                self.send_html_file(ServerConfig.BASE_DIR/ "front_end" / "index.html")
            case "/message":
                self.send_html_file(ServerConfig.BASE_DIR / "front_end" / "message.html")  
            case _:
                file = Path(ServerConfig.BASE_DIR/ "front_end/static" / pr_url.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html_file(ServerConfig.BASE_DIR / "front_end" / "error.html", HttpStatus.NOT_FOUND)

    def send_html_file(self, filename, status=HttpStatus.OK):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fh:
            self.wfile.write(fh.read())

    def send_static(self, filename):
        self.send_response(HttpStatus.OK)
        mime_type = mimetypes.guess_type(filename)[0]
        self.send_header("Content-type", mime_type or "text/html")
        self.end_headers()
        with open(filename, "rb") as fh:
            self.wfile.write(fh.read())


def run_http_server(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = (ServerConfig.HOST, ServerConfig.HTTP_SERVER_PORT)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run_http_server()
