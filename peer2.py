
import socket

clt=socket.socket()
clt1=("10.1.87.164",5999)
clt.connect(clt1)
print(clt.recv(1024).decode())
while(1):
    message=input("Enter the message to peer: ")
    clt.send(bytes(str(message),"utf-8"))
    data=clt.recv(1024).decode()
    print("peer: ",data)
    if(data=="stop"):
        k="Bye"
        clt.send(bytes(str(k),"utf-8"))
        break
    else:
        pass
