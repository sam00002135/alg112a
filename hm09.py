
def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    if col == len(board):
        return [row[:] for row in board]

    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            result = solve_n_queens_util(board, col + 1)
            if result:
                solutions.extend(result)
            board[i][col] = 0

    return solutions

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    return solve_n_queens_util(board, 0)

# Example usage for N=8
solutions = solve_n_queens(8)
print(f"Number of solutions: {len(solutions)}")
for solution in solutions:
    print(solution)
