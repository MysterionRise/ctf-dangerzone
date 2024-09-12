import socket
import re
from math import gcd


def greatest_prime_factor(n):
    """Return the greatest prime factor of n."""

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    greatest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            greatest_factor = i
    return greatest_factor


def least_common_multiple(a, b):
    """Return the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)


def solve_challenge(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    cnt = 0
    while cnt <= 102:
        cnt += 1
        data = s.recv(1024).decode()
        print(data)

        if "Give me" in data:
            if "greatest prime factor" in data:
                number = int(
                    re.search(r'greatest prime factor of (\d+)', data).group(
                        1))
                answer = greatest_prime_factor(number)
            elif "greatest common divisor" in data:
                numbers = list(map(int, re.search(
                    r'greatest common divisor of (\d+) and (\d+)',
                    data).groups()))
                answer = gcd(numbers[0], numbers[1])
            elif "least common multiple" in data:
                numbers = list(map(int, re.search(
                    r'least common multiple of (\d+) and (\d+)',
                    data).groups()))
                answer = least_common_multiple(numbers[0], numbers[1])
            else:
                print("Unknown question type.")
                continue

            s.sendall(str(answer).encode() + b'\n')


if __name__ == "__main__":
    server = "challs.n00bzunit3d.xyz"
    port = 10005
    solve_challenge(server, port)
