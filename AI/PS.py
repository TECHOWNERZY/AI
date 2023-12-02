# Write a program that takes input as a board position from 8 puzzle and generate all possible 
#moves in computer memory

# Structure to represent a board position
class Board:
    def __init__(self, state):
        self.state = state
        self.emptyRow, self.emptyCol = self.find_empty_cell()

    def find_empty_cell(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

# Function to print the board position
def print_board(board):
    for row in board.state:
        print(*row)
    print()

# Function to generate all possible moves from a given board position
def generate_moves(board):
    moves = []
    empty_row, empty_col = board.emptyRow, board.emptyCol

    # Move up
    if empty_row > 0:
        new_state = [row[:] for row in board.state]
        new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = new_state[empty_row - 1][empty_col], new_state[empty_row][empty_col]
        moves.append(Board(new_state))

    # Move down
    if empty_row < 2:
        new_state = [row[:] for row in board.state]
        new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = new_state[empty_row + 1][empty_col], new_state[empty_row][empty_col]
        moves.append(Board(new_state))

    # Move left
    if empty_col > 0:
        new_state = [row[:] for row in board.state]
        new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = new_state[empty_row][empty_col - 1], new_state[empty_row][empty_col]
        moves.append(Board(new_state))

    # Move right
    if empty_col < 2:
        new_state = [row[:] for row in board.state]
        new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = new_state[empty_row][empty_col + 1], new_state[empty_row][empty_col]
        moves.append(Board(new_state))

    return moves

# Main function
def main():
    initial_state = []

    print("Enter the initial board position (space-separated numbers from 0-8):")
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    initial_board = Board(initial_state)

    print("Initial Board Position:")
    print_board(initial_board)

    possible_moves = generate_moves(initial_board)

    print("Possible Moves:")
    for move in possible_moves:
        print_board(move)

if __name__ == "__main__":
    main()
    
