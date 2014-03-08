__author__ = 'nazareth'
import socket

HOST = 'localhost'
PORT = 3336
i = 1
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))
print 'Connecting with the server -- ', HOST
clientSocket.sendall('Hello, World!!')
data = clientSocket.recv(1024)
if data:
    print data
else:
    print 'Nothing Received from the server.'

clientSocket.close()
print 'Shutting down Client.'