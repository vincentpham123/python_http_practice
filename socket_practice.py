import socket
#importing form python library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creating stream based socket, 
mysock.connect(('data.pr4e.org',80))
# making 'phone call' to port 80, this will blow up if software is not running
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

#encode is preparing the data for the internet
mysock.send(cmd)
# this sends data back that we choose to receive
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break 
    print(data.decode())
mysock.close()