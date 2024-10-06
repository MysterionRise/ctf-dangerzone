import socket


def generate_turbo_tactical_list():
    result = []
    for i in range(1, 501):
        if i % 3 == 0 and i % 7 == 0:
            result.append("TURBOTACTICAL")
        elif i % 3 == 0:
            result.append("TURBO")
        elif i % 7 == 0:
            result.append("TACTICAL")
        else:
            result.append(str(i))
    return result


def send_data_to_server():
    data = generate_turbo_tactical_list()
    server_ip = '147.182.245.126'
    server_port = 33001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        print("connected!")

        for entry in data:
            s.sendall((entry + '\n').encode())

        response = s.recv(1024).decode()
        print(f"Server response: {response}")


if __name__ == "__main__":
    send_data_to_server()
