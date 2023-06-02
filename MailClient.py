from socket import *

# making the TCP connection

servername = "smtp.mail.yahoo.com"
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverPort))

# initial greetings
while True:
    response = clientSocket.recv(1024).decode("utf-8")
    parsedResponse = response.split(" ")[0]
    if parsedResponse == "220":
        clientSocket.send("HELO\r\n")
        server_welcome = clientSocket.recv(1024).decode("utf-8")
        if server_welcome == "250":
            clientSocket.send("MAIL FROM: <alexstylinson@gmail.com\r\n>")
        else:
            print("The server did not respond!")
            break
        server_mailFrom = clientSocket.recv(1024).decode()
        if server_mailFrom.split(" ")[0] == "250":
            clientSocket.send("RECPT TO: <yeganegholiour@gmail.com>\r\n")
        else:
            print("The server did not respond to the 'RECPT TO' part!!!")
            break
        server_rcpt = clientSocket.recv(1024).decode("utf-8")
        if server_rcpt.split(" ")[0] == "250":
            clientSocket.send("DATA \r\n")
        else:
            print("The server did not respond to 'DATA' part!!!")
            break
        server_data = clientSocket.recv(1024).decode()
        if server_data.split(" ")[0] == "354":
            header = "From: alexstylinson2002@gmail.com\r\nTo: yeganegholiour@gmail.com\r\nSubject: Mail client script \r\n"
            message = "This is yegane. i am writting a script for a mail client\r\n"
            clientSocket.send(header + message)
            clientSocket.send(".")
        else:
            print("The server did not respond to 'MESSAGE' part!!!")
            break
        server_message = clientSocket.recv(1024).decode()
        if server_message == "250":
            clientSocket.send("QUIT")
        else:
            print("The server did not respond to 'QUIT' part!!!")
            break
        server_quit = clientSocket.recv(1024).decode()
        if server_quit == "221":
            print("Sending mail was successful!!!!!")
        else:
            print("server did not quit!!!")

clientSocket.close()
