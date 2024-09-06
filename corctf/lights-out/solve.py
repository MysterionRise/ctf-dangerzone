import socket


def create_vector_representations(n: int, m: int) -> list[list[int]]:
    vectors = []
    for i in range(n * m):
        vector = [0] * (n * m)
        vector[i] = 1
        if i % m != 0:
            vector[i - 1] = 1  # left
        if i % m != m - 1:
            vector[i + 1] = 1  # right
        if i >= m:
            vector[i - m] = 1  # up
        if i < m * (n - 1):
            vector[i + m] = 1  # down
        vectors.append(vector)
    return vectors


def create_augmented_matrix(vectors: list[list[int]], board: list[int]) -> \
        list[list[int]]:
    matrix = [vec + [board[i]] for i, vec in enumerate(vectors)]
    return matrix


def gauss_jordan_elimination(matrix: list[list[int]]) -> list[list[int]]:
    rows, cols = len(matrix), len(matrix[0])
    r = 0
    for c in range(cols - 1):
        if r >= rows:
            break
        pivot = None
        for i in range(r, rows):
            if matrix[i][c] == 1:
                pivot = i
                break
        if pivot is None:
            continue
        if r != pivot:
            matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        for i in range(rows):
            if i != r and matrix[i][c] == 1:
                for j in range(cols):
                    matrix[i][j] ^= matrix[r][j]
        r += 1
    return matrix


def is_solvable(matrix: list[list[int]]) -> bool:
    rref = gauss_jordan_elimination(matrix)
    for row in rref:
        if row[-1] == 1 and all(val == 0 for val in row[:-1]):
            return False
    return True


def get_solution(board: list[int], n: int, m: int) -> list[int] | None:
    vectors = create_vector_representations(n, m)
    matrix = create_augmented_matrix(vectors, board)
    if not is_solvable(matrix):
        return None
    rref_matrix = gauss_jordan_elimination(matrix)
    return [row[-1] for row in rref_matrix[:n * m]]


def parse_board(data: str) -> tuple[list[int], int, int]:
    lines = data.split('\n')[26:]
    board_lines = []
    for line in lines:
        if line.strip() == "":
            break
        board_lines.append(line.strip())
    n = len(board_lines)
    m = len(board_lines[0])
    board = []
    for line in board_lines:
        board.extend([1 if char == '#' else 0 for char in line])
    return board, n, m


def print_board(board: list[int], n: int, m: int) -> str:
    board_str = ""
    for i in range(n):
        for j in range(m):
            board_str += '#' if board[i * m + j] else '.'
        board_str += '\n'
    return board_str


def main() -> None:
    host = 'be.ax'
    port = 32421

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(4096).decode()
        while not data.strip().endswith("Your Solution:"):
            data += s.recv(4096).decode()

        board, n, m = parse_board(data)
        print(n)
        print(m)
        print("Parsed Board:")
        print(print_board(board, n, m))

        solution = get_solution(board, n, m)
        if solution is None:
            print("No solution found.")
            return

        solution_string = ''.join('#' if x == 1 else '.' for x in solution)
        print(f'Sending solution: {solution_string}')
        s.sendall((solution_string + '\n').encode())

        final_response = s.recv(4096).decode()
        print(final_response)


if __name__ == "__main__":
    main()
