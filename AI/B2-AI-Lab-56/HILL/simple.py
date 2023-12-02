import math

currentNode = [[0], [0]]
currentScore = 0
flag = 0


def swap(board, x, y, p, q):
    temp = board[x][y]
    board[x][y] = board[p][q]
    board[p][q] = temp


def setCurrent_node(board, score):
    print("f(A):", score)
    global currentScore, currentNode, flag
    if score == 0:
        print("Goal State achieved.")
        flag = 1
    if score < currentScore:
        currentScore = score
        currentNode = board
        print("Current Node:", board)
        flag = 1


def printarr(board):
    for row in board:
        print(*row)
    print()


def validpositions(board):
    global flag
    score = 0
    gap_row = 0
    gap_col = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                gap_row = i
                gap_col = j
                break

    if gap_row < 2 and flag == 0:
        swap(board, gap_row, gap_col, gap_row + 1, gap_col)
        printarr(board)
        score = calculate_score(board)
        setCurrent_node(board, score)
        swap(board, gap_row, gap_col, gap_row + 1, gap_col)

    if gap_col < 2 and flag == 0:
        swap(board, gap_row, gap_col, gap_row, gap_col + 1)
        printarr(board)
        score = calculate_score(board)
        setCurrent_node(board, score)
        swap(board, gap_row, gap_col, gap_row, gap_col + 1)

    if gap_row >= 1 and flag == 0:
        swap(board, gap_row, gap_col, gap_row - 1, gap_col)
        printarr(board)
        score = calculate_score(board)
        setCurrent_node(board, score)
        swap(board, gap_row, gap_col, gap_row - 1, gap_col)

    if gap_col >= 1 and flag == 0:
        swap(board, gap_row, gap_col, gap_row, gap_col - 1)
        printarr(board)
        score = calculate_score(board)
        setCurrent_node(board, score)
        swap(board, gap_row, gap_col, gap_row, gap_col - 1)


def calculate_score(board):
    distance = 0
    ideal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    for i in range(3):
        for j in range(3):
            distance += (board[i][j] - ideal[i][j]) ** 2
    score = math.sqrt(distance)
    return score


def main():
    board = [[0] * 3 for _ in range(3)]
    for i in range(3):
        board[i] = list(map(int, input().split()))

    global currentScore
    currentScore = calculate_score(board)
    print("Current Score:", currentScore)
    validpositions(board)


if __name__ == "__main__":
    main()






