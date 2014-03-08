__author__ = 'nazareth'
import socket

HOST = ''
PORT = 3336
msg = 'Msg Received'
trialSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
trialSocket.bind((HOST, PORT))
print 'Created a Server -- Waiting ...'
trialSocket.listen(1)
conn, addr = trialSocket.accept()
print 'Connected By ', addr
while 1:
    data = conn.recv(1024)
    print 'Client Sent -- ', data
    if not data:
        break
    conn.send(msg)

conn.close()
