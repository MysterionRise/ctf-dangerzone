import socket
import re
import math


def solve_problem(problem):
    if "factorial" in problem:
        number = int(re.search(r'\d+', problem).group())
        return math.factorial(number)


def main():
    server_address = ('147.182.245.126', 33001)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)

        problem = s.recv(1024).decode('utf-8')
        print("Problem received:", problem)
        result = solve_problem(problem)
        print("Result to send:", result)
        s.sendall(str(result).encode('utf-8'))
        flag = s.recv(1024).decode('utf-8')
        print("Flag received:", flag)


if __name__ == "__main__":
    main()
