import socket
import threading
from cryptography.fernet import Fernet


key = 'iQkW5Bm24LFyvtHHWx-u9AQ21EmrEJFEX1se8JO09XA='


bind_ip = '127.0.0.1'
bind_port = 80

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print("Listening on {0}:{1}".format(bind_ip,bind_port))


def encrypt(request):
    f = Fernet(key=key.encode())
    encryptedMessage = f.encrypt(request).decode()
    return encryptedMessage

def decrypt(request):
    f = Fernet(key=key.encode())
    decryptedMessage = f.decrypt(request).decode()
    return decryptedMessage

def handleClient(client):
    request = client.recv(10000)
    request = request.decode()
    print(request)
    if str("~") in request:
        request = request.strip("~")
        print("Recieved Request {0}".format(request))
        encryptedMessage = encrypt(request.encode())
        client.send(encryptedMessage.encode())
        client.close()
    elif str("Saumil") in request:
        request = request.strip("Saumil")
        print("Recieved Request {0}".format(request))
        decryptedMessage = decrypt(request.encode())
        client.send(decryptedMessage.encode())
        client.close()



while True:
    client,address = server.accept()
    print("Accepted connection from {0}:{1}".format(address[0],address[1]))

    clientHandler = threading.Thread(target=handleClient,args=(client,))
    clientHandler.start()

