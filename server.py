import socket 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.25.208.1'
port = 50000

serverSocket.bind((host, port))
serverSocket.listen()

monsoon_list = [
    ["Introduction to Computer Programming", "CS-1101"],
    ["Introduction to Machine Learning", "CS-1390"],
    ["Programming Language Design and Implementation", "CS-1319"],
    ["Computer Networks", "CS-1340"],
    ["Computer Organization and Systems", "CS-1216"],
    ["Database Management Systems", "CS-2375"],
    ["Advanced Algorithms", "CS-2446"],
    ["Computational/Mathematical Biology", "CS-2456"],
    ["Linear Algebra", "CS-2210"],
    ["Soumyottam Chatterjee", "CS-2450"],
    ["Probability and Statistics", "CS-1209"],
    ["Biostatistics and Bioinformatics", "CS-2455"],
    ["Algebra 1", "CS-2250"],
    ["Computer Vision", "CS-2467"],
    ["Machine Learning for Finanace", "CS-2466"],
    ["An overview of usable privacy and security", "CS-2463"],
    ["Fairness of AI", "CS-2464"],
    ["Information and Coding Theory", "CS-2462"],
    ["Computing in the Cloud", "CS-2465"],
    ["Symbolic Logic", "CS-2160"],
    ["Data Structures", "CS-1203"],
    ["Statistics for Economics", "CS-1207"]
]

spring_list = [
    ["Introduction to Computer Programming", "CS-1101"],
    ["Computer Security and Privacy", "CS-2362"],
    ["Operating Systems", "CS-1217"],
    ["Theory of Computation", "CS-2349"],
    ["Algorithm Design and Analysis", "CS-1205"],
    ["Discrete Mathematics", "CS-1104"],
    ["Data Mining and Warehousing", "CS-2376"],
    ["Advanced Machine Learning", "CS-2490"],
    ["Blockchain and Cryptocurrencies", "CS-2361"],
    ["Linear Algebra", "CS-2210"],
    ["Fuzzy Cartographies", "CS-2209"],
    ["Mathematical Foundations of Data Sciences", "CS-2380"],
    ["Advanced Topics in Probability", "CS-2470"],
    ["The New Geography of the Information Age", "CS-2378"]
]

courses = {
    "CS-1101" : ["N/A"],                                    # ICP - NA
    "CS-1104" : ["N/A"],                                    # DM - NA
    "CS-1209" : ["N/A"],                                    # PS - NA
    "CS-1216" : ["CS-1101"],                                # COS - ICP
    "CS-1203" : ["CS-1101"],                                # DS - ICP
    "CS-1205" : ["CS-1101"],                                # Algos - ICP
    "CS-1217" : ["CS-1101", "CS-1216"],                     # OS - ICP, COS
    "CS-1390" : ["CS-1101", "CS-1209"],                     # IML - ICP, PS
    "CS-1319" : ["CS-1101", "CS-1216", "CS-1203"],          # PLDI - ICP, DS, COS
    "CS-1340" : ["CS-1101", "CS-1216"]                      # ICP, COS
}

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