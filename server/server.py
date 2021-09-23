#!/usr/bin/env python3

import socket
import os
from datetime import datetime

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65439        # Port to listen on (non-privileged ports are > 1023)
SEPARATOR = '<SEPARATOR>'
BUFFER_SIZE = 200


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        filename, filesize = data.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        with open(os.path.join('server_files',filename), "wb") as f:
            i = 0 
            
            while True:
                print(f'iter: {i}')
                bytes_read = conn.recv(BUFFER_SIZE)
                print(repr(bytes_read))
                if not bytes_read:
                    break
                f.write(bytes_read)
                i += 1
        conn.sendall(bytes('siema', 'u'))
        print('end of conn')

    print('123')