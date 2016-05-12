# -*- coding: utf-8 -*-
import socket
import sys

destinations = {
    'destination0': {'interface': 'localhost', 'Cost': 0},
    'destination1': {'interface': '10.80.0.12', 'Cost': 2},
    'destination2': {'interface': '128.235.211.21', 'Cost': 4},
    'destination3': {'interface': '128.235.209.204', 'Cost': 6}}

for destination, values in destinations.iteritems():
    currentInterface = values['interface']
    if currentInterface != "localhost":
        print(currentInterface)
        s = socket.socket()
        host = currentInterface
        port = 88
        s.connect((host,port))
        localDestinations= str(destinations)
        s.send(localDestinations.encode())
        message = s.recv(1024).decode()
        s.close()
        print ('Client: Connection terminated')
        print(message)
        destinations = (message)
