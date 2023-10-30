import socket
#using nested dictionaries to store course information alongwith prerequisites and semester offered

cs_courses = {"Probability and Statistics": {"prerequisite": "Math in Grades XI and XII OR QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Monsoon"}, "Linear Algebra": {"prerequisite": "Check With Math Department", "semester": "Monsoon"}, "Calculus": {"prerequisite": "Check With Math Department", "semester": "Monsoon"}, "Introduction to Computer Science": {"prerequisite": "Math in Grades XI and XII OR a minimum of B in QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Spring"},
            "Discrete Mathematics": {"prerequisite": "Math in Grades XI and XII OR a minimum of B in QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Spring"}, "Data Structures and Algorithms": {"prerequisite": "Introduction to Computer Science, Discrete Mathematics", "semester": "Monsoon"}, "Introduction to Machine Learning": {"prerequisite": "Probability and Statistics, Linear Algebra, Data Structures and Algorithms", "semester": "Monsoon"}, "Data Science and Management": {"prerequisite": "Data Structures and Algorithms, Introduction to Machine Learning", "semester": "Spring"}, 
            "Theory of Computation": {"prerequisite": "Data Structures and Algorithms", "semester": "Spring"}, "Design and Analysis of Algorithms": {"prerequisite": "Data Structures and Algorithms, Linear Algebra", "semester": "Spring"}, "Programming Languages and Translation": {"prerequisite": "Data Structures and Algorithms, Theory of Computation", "semester": "Monsoon"}, "Information Security": {"prerequisite": "Data Structures and Algorithms, Probability and Statistics", "semester": "Monsoon"},
            "Computer Organisation and Systems": {"prerequisite": "Introduction to Computer Science", "semester": "Spring"}, "Design Practices in CS": {"prerequisite": "Data Structures and Algorithms, Computer Organisation and Systems", "semester": "Monsoon"}, "Computer Networks": {"prerequisite": "Introduction to Computer Science, Data Structures and Algorithms", "semester": "Monsoon"}, "Embedded Systems": {"prerequisite": "Computer Organisation and Systems", "semester": "Spring"},
            "Capstone Project": {"prerequisite": "", "semester": "Monsoon"}}

def handle_client(client_socket):
    while True:
        option = client_socket.recv(1024).decode()
        
        if option == '1':
            client_socket.send("Minimum of 86 CS credits in 4 year BSc Hons in CS. ".encode())
        elif option == '2':
            client_socket.send("76 credits from CS core. 12 credits from CS electives.".encode())
        elif option == '3':
            course_names = "\n".join(cs_courses.keys())
            client_socket.send(course_names.encode())
        elif option == '4':
            course_info = "\n".join([f"{course}: Prerequisite - {cs_courses[course]['prerequisite']}" for course in cs_courses])
            client_socket.send(course_info.encode())
        elif option == '5':
            course_info = "\n".join([f"{course}: {cs_courses[course]['semester']}" for course in cs_courses])
            client_socket.send(course_info.encode())
        elif option == '6':
            client_socket.send("You chose option 6".encode())
        elif option == '7':
            client_socket.send("You chose option 7".encode())
        elif option == '8':
            client_socket.send("You chose option 8".encode())
        elif option == '9':
            client_socket.send("You chose option 9".encode())
        elif option == '10':
            client_socket.send("You chose option 10".encode())
        elif option == '11':
            client_socket.send("Goodbye!".encode())
            break
        else:
            client_socket.send("Invalid option. Please try again.".encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('172.25.208.1', 12345))
    server.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
