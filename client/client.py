#!/usr/bin/env python3

import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65439        # The port used by the server

filename = '../client_files/text1.txt'
file_size = os.path.getsize(filename)
BUFFER_SIZE = 200
SEPARATOR = '<SEPARATOR>'

def send_file(filename, file_size, host=HOST, port=PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(f"{filename}{SEPARATOR}{file_size}".encode('utf-8'))
            with open(filename) as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE).encode('utf-8')         
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)

send_file(filename=filename, file_size=file_size)