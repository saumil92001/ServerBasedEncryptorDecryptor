import socket
import sys

def TcpCLientEncrypt():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect(("127.0.0.1",80))
    message = input("Enter message to encrypt:- ")
    datalist = message+"~"
    server.send(datalist.encode())
    response = server.recv(1000)
    print("Encrypted message is :- \n"+response.decode())


def TcpClientDecrypt():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect(("127.0.0.1",80))
    message = input("Enter encrypted message:- ")
    datalist = message+"Saumil"
    server.send(datalist.encode())
    response = server.recv(1000)
    print("Decrypted message is :- \n"+str(response))


try:
    print("What do you want to do?\n\t1.)Encrypt Message\n\t2.)Decrypt Message ")
    choiceInput = int(input("Enter your choice: "))

    if choiceInput == 1:
        TcpCLientEncrypt()
    elif choiceInput == 2:
        TcpClientDecrypt()
    else:
        print("Invalid input")
        sys.exit(0)
except:
    print("Oops...Something went wrong")
    sys.exit(0)