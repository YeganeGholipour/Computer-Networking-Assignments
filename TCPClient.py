# TCPClient.py

from socket import *

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = "GET /somedir/page.file HTTP/1.1 \r\nHost: 127.0.0.1"
clientSocket.send(message.encode())
response = clientSocket.recv(1024)
clientSocket.close()
