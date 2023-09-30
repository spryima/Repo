import threading

from http_server import run_http_server
from socket_server import run_socket_server


if __name__ == "__main__":
    print("\n\n Press Ctrl+C to stop HTTP Server and Socket Server \n\n")

    t1 = threading.Thread(target=run_http_server, daemon=True)
    t2 = threading.Thread(target=run_socket_server, daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
