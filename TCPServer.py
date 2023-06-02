from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to recieve your request.")

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        request = connectionSocket.recv(1024).decode("utf-8")
        parsingRequest = request.splitlines()
        getLine = parsingRequest[0]
        filePath = getLine.split(" ")[1]
    except (UnicodeDecodeError, ValueError, IndexError) as e:
        print(f"Exeption occured with parsing error: {e}")
        try:
            with open(filePath) as f:
                content = f.read()
                response = f"HTTP/1.1 200 OK \n\rContent-Type: text/html\r\n\n{content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found"

    connectionSocket.send(response.encode())
    connectionSocket.close()
