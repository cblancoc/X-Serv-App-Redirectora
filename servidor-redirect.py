#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1235))

mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        rand_num = random.randrange(1000000000000000)
        new_url = str(rand_num)
        recvSocket.send("HTTP/1.1 301 Moved Permanently\r\n" +
                        "Location: " + new_url + "\r\n\r\n"
                        "<html><body>Hola. " +
                        "<p>This page has moved to " +
                        "<a href=" + new_url + ">" + 
                        new_url + "/</a>.</p>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
    
