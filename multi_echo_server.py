#!/usr/bin/env python3

import socket
import sys
from multiprocessing import Process

# define global address and buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# get ip

def main():
    
    #create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        # allow reused addresses, bind, and set to listening mode
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)

        while True:
            #connect proxy_start 
            conn, addr = proxy_start.accept() 
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

                
def handle_echo(addr, conn):
    print("Connect by", addr)

    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()
