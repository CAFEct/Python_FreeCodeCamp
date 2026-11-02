from operator import truediv


def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    stack = []

    while stack:
        board = stack.pop()
        row = len(board)

        if row == n:
            solutions.append(board)
            continue

        for col in range(n -1, -1, -1):
            is_safe = True
            for i in range(row):
                c = board[i]
                if c == col or abs(c - col) == abs(i - row):
                    is_safe = False
                    break

            if is_safe:
                stack.append(board+[col])
        return solutions
