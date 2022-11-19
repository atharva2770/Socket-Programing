import socket

s = socket.socket()

#It will accept connection
print('Socket Created')

#Bind socket with port number
s.bind(('localhost',9999))

#Start listenling to client means we have to wait for client to connect
#at one time how many client we want to connect
s.listen(3)
print('Waiting for connection')

while True:
    c,add = s.accept()
    name = c.recv(1024).decode()            ##Receiving Data from client
    print("Connected with ", add,name)

    c.send(bytes('Welcome to Server' , 'utf-8'))
    c.close()
