#import socket module
from socket import *

def main(): 
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSocket.bind(('',80))
    serverSocket.listen(1)
    
    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            print(message)

            filename = message.split()[1]
            print(filename)
            f = open(filename[1:])

            outputdata = f.read()
            print(outputdata)

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()

        except IOError:
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
            connectionSocket.close()

    serverSocket.close()
    pass

if __name__ == '__main__':
    main()