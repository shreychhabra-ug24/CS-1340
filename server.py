import socket
#using nested dictionaries to store course information alongwith prerequisites and semester offered

cs_courses = {"Probability and Statistics (PnS)": {"prerequisite": "Math in Grades XI and XII OR QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Monsoon"}, "Linear Algebra": {"prerequisite": "Check With Math Department", "semester": "Monsoon"}, "Calculus": {"prerequisite": "Check With Math Department", "semester": "Monsoon"}, "Introduction to Computer Science(ICS)": {"prerequisite": "Math in Grades XI and XII OR a minimum of B in QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Spring"},
            "Discrete Mathematics": {"prerequisite": "Math in Grades XI and XII OR a minimum of B in QRMT (FC-0306)+Calculus Enabler(MAT-1000)", "semester": "Spring"}, "Data Structures and Algorithms(DSA)": {"prerequisite": "ICS, Discrete Mathematics", "semester": "Monsoon"}, "Introduction to Machine Learning(IML)": {"prerequisite": "PnS, Linear Algebra, DSA", "semester": "Monsoon"}, "Data Science and Management": {"prerequisite": "DSA, IML", "semester": "Spring"}, 
            "Theory of Computation": {"prerequisite": "DSA", "semester": "Spring"}, "Design and Analysis of Algorithms": {"prerequisite": "DSA, Linear Algebra", "semester": "Spring"}, "Programming Languages and Translation": {"prerequisite": "DSA, Theory of Computation", "semester": "Monsoon"}, "Information Security": {"prerequisite": "DSA, PnS", "semester": "Monsoon"},
            "Computer Organisation and Systems(COS)": {"prerequisite": "ICS", "semester": "Spring"}, "Design Practices in CS": {"prerequisite": "DSA, COS", "semester": "Monsoon"}, "Computer Networks": {"prerequisite": "ICS, DSA", "semester": "Monsoon"}, "Embedded Systems": {"prerequisite": "COS", "semester": "Spring"},
            "Capstone Project": {"prerequisite": "", "semester": "Monsoon"}}

def handle_client(clientsocket):
    while True:
        option = clientsocket.recv(1024).decode()
        
        if option == '1':
            response = "Minimum of 86 CS credits in 4 year BSc Hons in CS. "
        elif option == '2':
            response = "74 credits from CS core. 12 credits from CS electives."
        elif option == '3':
            course_names = "\n".join(cs_courses.keys()) #joins the keys of the dictionary with a newline character to return as string
            response = course_names
        elif option == '4':
            course_info = "\n".join([f"{course}: Prerequisite - {cs_courses[course]['prerequisite']}" for course in cs_courses])
            response = course_info
        elif option == '5':
            course_info = "\n".join([f"{course}: {cs_courses[course]['semester']}" for course in cs_courses])
            response = course_info
        elif option == '6':
            response = "Minimum 6 non academic ccredits: 4 for co-curricular courses and 2 for internship experience. "
        elif option == '7':
            response = "A total of 36 credits for foundation courses. "
        elif option == '8':
            response = "Minimum of 150 credits for degree completion, where 144 are academic credits including 86 for CS, 36 for FC, 22 open credits (any course), and 6 non-academic credits. "
        elif option == '9':
            response = "The Physics and Biology course offering is yet to be decided, but may be taken any time in the 4 year degree. Alongside electives, they are not mentioned in the Core Course list and must be taken when required. "
        elif option == '10':
            response = "Minimum grade of B in Introduction to Computer Science and Discrete Math. To take ICS and Discrete Math, minimum grade of B in QRMT+Calculus if math not taken in grades XI and XII. "
        elif option == '11':
            response = "Goodbye! "
            clientsocket.send(response.encode())
            # close the connection with the client
            clientsocket.close()
            break
        clientsocket.send(response.encode())
        if not response:
            response = "Invalid option. Please try again."

#main function with driver code to connect to client side

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('172.25.208.1', 80))
    server.listen(5)
    print("Waiting for connection...")
    #ensures that the connection is persistent and handles repeated requests from the client
    while True:
        clientsocket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(clientsocket)

if __name__ == "__main__":
    main()
