from pwn import remote, context
import logging

context.log_level = 'error'


def parse_matrix(data):
    matrix = []
    optimal_value = 0
    for line in data:
        line = line.strip()
        if line.startswith('optimal:'):
            optimal_value = int(line.split()[1])
            break
        row = list(map(int, line.split()))
        matrix.append(row)
    return matrix, optimal_value


def get_path(eggs):
    n = len(eggs)
    dp = [[0] * n for _ in range(n)]
    path = [[None] * n for _ in range(n)]

    dp[0][0] = eggs[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + eggs[i][0]
        path[i][0] = 'd'
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + eggs[0][j]
        path[0][j] = 'r'

    for i in range(1, n):
        for j in range(1, n):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + eggs[i][j]
                path[i][j] = 'd'
            else:
                dp[i][j] = dp[i][j - 1] + eggs[i][j]
                path[i][j] = 'r'

    return dp, path


def reconstruct_path(path):
    n = len(path)
    i, j = n - 1, n - 1
    result = []
    while i > 0 or j > 0:
        result.append(path[i][j])
        if path[i][j] == 'd':
            i -= 1
        else:
            j -= 1
    result.reverse()
    return ''.join(result)


def main():
    host = '24.199.110.35'
    port = 43298
    connection = remote(host, port)

    for _ in range(10):
        data = []
        for i in range(1001):
            data.append(connection.recvline().decode().strip())

        eggs, optimal_value = parse_matrix(data)

        dp, path = get_path(eggs)
        input_path = reconstruct_path(path)
        input_ans = dp[-1][-1]

        connection.sendline(input_path.decode)

    final_output = connection.recvall().decode()
    print(final_output)


if __name__ == "__main__":
    main()
