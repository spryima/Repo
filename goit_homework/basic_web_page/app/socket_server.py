import json
import logging
from pathlib import Path
import socketserver
from urllib.parse import unquote_plus
from datetime import datetime


class ServerConfig:
    HOST = "0.0.0.0"
    SOCKET_PORT = 5001
    BUFFER_SIZE = 1024
    BASE_DIR = Path(__file__).resolve().parent.parent


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(ServerConfig.BUFFER_SIZE).strip()
        print("{} wrote:".format(self.client_address[0]))
        data_parse = unquote_plus(self.data.decode())
        file_path = Path(ServerConfig.BASE_DIR / "storage" / "data.json")
        try:
            data = {}
            if file_path.exists() and file_path.stat().st_size > 0:
                with open(file_path, "r", encoding="utf-8") as fh:            
                    data = json.load(fh)  
            data[datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")] = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
            with open(file_path, "w") as fh:                         
                json.dump(data, fh, ensure_ascii=False)                    
        except ValueError as err:
            logging.error(f"{data_parse} - {err}")                        
        except OSError as err:
            logging.error(f"{data_parse} - {err}")  


def run_socket_server():
    with socketserver.TCPServer((ServerConfig.HOST, ServerConfig.SOCKET_PORT), MyTCPHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    run_socket_server()
