

import socket
s=socket.socket()
server_address=('10.1.87.164',5999)
s.bind(server_address)
s.listen(2)
print("Waiting for connection")
clt,client_address=s.accept()
print("Connection established",client_address)
p="Welcome!"
clt.send(bytes(str(p),"utf-8"))
message=clt.recv(1024).decode()
while(1):
    if message!="stop" and message!="Bye":
        print("Peer: ",message)
        data=input("Enter the message to peer: ")
        clt.send(bytes(str(data),"utf-8"))
        message=clt.recv(1024).decode()
    else:
        data="stop"
        clt.send(bytes(str(data),"utf-8"))
        break
clt.close()
