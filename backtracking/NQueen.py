def print_solution(board):
    """Hàm in ra bàn cờ với các quân hậu được đặt."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col, n):
    """Kiểm tra xem có thể đặt quân hậu tại vị trí (row, col) hay không."""
    # Kiểm tra hàng ngang bên trái
    for i in range(col):
        if board[row][i]:
            return False

    # Kiểm tra đường chéo trên bên trái
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queen(board, col, n):
    """Hàm giải bài toán N-Queen bằng đệ quy."""
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Đặt quân hậu tại vị trí (i, col)
            board[i][col] = True

            # Đệ quy để đặt quân hậu ở cột tiếp theo
            res = solve_n_queen(board, col + 1, n) or res

            # Backtrack: gỡ quân hậu khỏi vị trí (i, col)
            board[i][col] = False

    return res


def n_queen(n):
    """Hàm khởi tạo bàn cờ và bắt đầu giải bài toán N-Queen."""
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queen(board, 0, n):
        print("Không có lời giải cho bài toán N-Queen với N =", n)


# Chạy thử với N = 2
if __name__ == "__main__":
    n = 4
    n_queen(n)