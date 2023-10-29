import socket


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverHost = "172.25.208.1"
serverPort = 50000

clientSocket.connect((serverHost,serverPort))

x = int(input("Enter an integer: "))

clientSocket.send(str(x).encode('utf-8'))

result = clientSocket.recv(1024).decode('utf-8')


response_message, result = result.split(':', 1)

print(f"Server Response: {response_message}")
print(f"Result: {result}")

clientSocket.close()