import socket 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.25.208.1'
port = 50000

serverSocket.bind((host, port))
print("yo")

while True:
    serverSocket.listen(4)
    print("Server is waiting for a connection ....")

    clientSocket, address = serverSocket.accept()
    print(f"connection from: {address}")

    data = clientSocket.recv(1024)
    if not data:
        break

    x = int(data.decode('utf-8'))

    z = x*x

    response_message = f"Thanks for connecting. Here is your answer: {z}"



    clientSocket.send(response_message.encode('utf-8'))


    clientSocket.close()

serverSocket.close()