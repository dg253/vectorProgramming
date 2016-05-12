# -*- coding: utf-8 -*-
from socket import *
import socket
import sys

host = '10.80.0.12'
port = 88
socketConnection = socket(AF_INET,SOCK_STREAM)
socketConnection.bind((host, port))
socketConnection.listen(1)

destinations = {
    'destination0': {'interface': '52.38.130.148', 'Cost': 1},
    'destination1': {'interface': 'localhost', 'Cost': 0},
    'destination2': {'interface': '128.235.211.21', 'Cost': 3},
    'destination3': {'interface': '128.235.209.204', 'Cost': 5}}

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
