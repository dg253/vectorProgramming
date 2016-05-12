# -*- coding: utf-8 -*-
from socket import *
from socket import socket
import sys
host = '128.235.209.204'
port = 88
socket = socket(AF_INET,SOCK_STREAM)
socket.bind((host, port))
socket.listen(1)

destinations = {
    'destination0': {'interface': '52.38.130.148', 'Cost': 4},
    'destination1': {'interface': '128.235.208.35', 'Cost': 3},
    'destination2': {'interface': '128.235.211.21', 'Cost': 2},
    'destination3': {'interface': 'localhost', 'Cost': 0}}

print ('Successful socket binding')
while True:
    client, addr = socket.accept()
    print ('Established connection with:', addr)
    message = client.recv(1024).decode()
    print(message)
    table = str(table)
    client.send(table.encode())
    client.close()
else:
    client.close()
print('Cannot connect.  Try again.')
