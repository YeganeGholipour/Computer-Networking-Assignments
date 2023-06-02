# udp-pinger-client

from socket import *
import time

serverName = "127.0.0.1"
serverport = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
numMessage = 0
while numMessage < 10:
    message = "This is a PING message"
    start_time = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverport))
    time.sleep(1)
    try:
        response, serverAddress = clientSocket.recv(2048)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"ping for the {numMessage+1} message: ", elapsed_time)
    except TimeoutError:
        print(f"packet {numMessage+1} lost")
    numMessage += 1
clientSocket.close()
