import numpy as np

current_node = None
current_score = 0
flag = 0


def swap(board, x, y, p, q):
    temp = board[x][y]
    board[x][y] = board[p][q]
    board[p][q] = temp


def set_current_node(board, score):
    global current_score, current_node, flag
    print("f(A):", score)
    if score == 0:
        print("Goal State achieved.")
        flag = 1
    if score < current_score:
        current_score = score
        current_node = board
        print("Current Node:", current_node)


def print_arr(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def valid_positions(board):
    global flag
    gap_row, gap_col = np.where(board == 0)
    gap_row, gap_col = gap_row[0], gap_col[0]

    if gap_row < 2 and flag == 0:
        swap(board, gap_row, gap_col, gap_row + 1, gap_col)
        print_arr(board)
        score_val = score(board)
        set_current_node(board, score_val)
        swap(board, gap_row, gap_col, gap_row + 1, gap_col)

    if gap_col < 2 and flag == 0:
        swap(board, gap_row, gap_col, gap_row, gap_col + 1)
        print_arr(board)
        score_val = score(board)
        set_current_node(board, score_val)
        swap(board, gap_row, gap_col, gap_row, gap_col + 1)

    if gap_row >= 1 and flag == 0:
        swap(board, gap_row, gap_col, gap_row - 1, gap_col)
        print_arr(board)
        score_val = score(board)
        set_current_node(board, score_val)
        swap(board, gap_row, gap_col, gap_row - 1, gap_col)

    if gap_col >= 1 and flag == 0:
        swap(board, gap_row, gap_col, gap_row, gap_col - 1)
        print_arr(board)
        score_val = score(board)
        set_current_node(board, score_val)
        swap(board, gap_row, gap_col, gap_row, gap_col - 1)


def score(board):
    ideal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    distance = np.sum((board - ideal) ** 2)
    return np.sqrt(distance)


if __name__ == "__main__":
    board = np.zeros((3, 3), dtype=int)
    for i in range(3):
        board[i] = list(map(int, input().split()))

    current_node = board
    current_score = score(board)
    print("Current Score:", current_score)
    valid_positions(current_node)
