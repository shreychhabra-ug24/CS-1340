import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('172.25.208.1', 80))
    print("1: Number of CS credits in 4 year BSc Hons in CS. ")
    print("2: Breakdown of CS credits. ")
    print("3: List of Core CS courses. ")
    print("4: List of Core CS Courses with their Prequisites. ")
    print("5: List of Core CS courses and what semester they're offered in. ")
    print("6: Non Academic Credits. ")
    print("7: Foundation Course Credits. ")
    print("8: Total Credits for degree and remaining credits. ")
    print("9: Physics and Biology Courses, and Electives. ")
    print("10: Minimum Grade Requirements. ")

    while True:
        print("Choose an option (1-10) or enter 11 to quit:")
        option = input("> ")
        if option not in [str(i) for i in range(1, 12)]:
        #if option not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            print("Invalid input. Please try again.")
            continue

        client.send(option.encode())
        response = client.recv(1024).decode()
        print(response)

        if option == '11':
            break

    client.close()

if __name__ == "__main__":
    main()
