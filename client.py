import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your Name ")
c.send(bytes(name,'utf-8'))

#Now We have to receive

print(c.recv(1024).decode())         ##1024 Buffer size