def read_board(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "0" in line or any(c.isdigit() for c in line):
                row = [int(x) for x in line]
            if len(row) != 9:
                raise ValueError(f"Invalid row in {filename}: {row}")
            board.append(row)
    if len(board) != 9:
        raise ValueError(f"{filename} must have 9 rows")
    return board
def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
def get_domain(board, row, col):
    return [num for num in range(1, 10) if is_valid(board, row, col, num)]
def find_empty(board):
    best_cell = None
    best_domain_size = 10
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domain_size = len(get_domain(board, i, j))
                if domain_size < best_domain_size:
                    best_domain_size = domain_size
                    best_cell = (i, j)
                if domain_size == 1:
                    return (i, j)
    return best_cell
backtrack_calls = 0
failures = 0
def backtrack(board):
    global backtrack_calls, failures
    backtrack_calls += 1
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    domain = get_domain(board, row, col)
    if len(domain) == 0:
        failures += 1
        return False
    for num in domain:
        board[row][col] = num
        if backtrack(board):
            return True
        board[row][col] = 0  
    failures += 1
    return False
def solve(filename):
    global backtrack_calls, failures
    backtrack_calls = 0
    failures = 0
    try:
        board = read_board(filename)
    except Exception as e:
        print("Error:", e)
        return
    print("Input:", filename)
    print_board(board)
    if backtrack(board):
        print("Solved:")
        print_board(board)
    else:
        print("No solution found")
    print("Backtrack calls:", backtrack_calls)
    print("Failures:", failures)
    print("-" * 40)
solve("easy.txt")
solve("medium.txt")
solve("hard.txt")
solve("veryhard.txt")
