#include <iostream>

using namespace std;

// Structure to represent a board position
struct Board {
    int state[3][3];
    int emptyRow;
    int emptyCol;
};

// Function to print the board position
void printBoard(const Board& board) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << board.state[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// Function to generate all possible moves from a given board position
void generateMoves(const Board& board, Board moves[4], int& numMoves) {
    numMoves = 0;
    int emptyRow = board.emptyRow;
    int emptyCol = board.emptyCol;

    // Move up
    if (emptyRow > 0) {
        moves[numMoves] = board;
        swap(moves[numMoves].state[emptyRow][emptyCol], moves[numMoves].state[emptyRow - 1][emptyCol]);
        moves[numMoves].emptyRow--;
        numMoves++;
    }

    
    if (emptyRow < 2) {
        moves[numMoves] = board;
        swap(moves[numMoves].state[emptyRow][emptyCol], moves[numMoves].state[emptyRow + 1][emptyCol]);
        moves[numMoves].emptyRow++;
        numMoves++;
    }

    // Move left
    if (emptyCol > 0) {
        moves[numMoves] = board;
        swap(moves[numMoves].state[emptyRow][emptyCol], moves[numMoves].state[emptyRow][emptyCol - 1]);
        moves[numMoves].emptyCol--;
        numMoves++;
    }

    // Move right
    if (emptyCol < 2) {
        moves[numMoves] = board;
        swap(moves[numMoves].state[emptyRow][emptyCol], moves[numMoves].state[emptyRow][emptyCol + 1]);
        moves[numMoves].emptyCol++;
        numMoves++;
    }
}`

int main() {
    Board initialBoard;

    cout << "Enter the initial board position (space-separated numbers from 0-8):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> initialBoard.state[i][j];
            if (initialBoard.state[i][j] == 0) {
                initialBoard.emptyRow = i;
                initialBoard.emptyCol = j;
            }
        }
    }

    cout << "Initial Board Position:" << endl;
    printBoard(initialBoard);

    Board possibleMoves[4];
    int numMoves;

    generateMoves(initialBoard, possibleMoves, numMoves);

    cout << "Possible Moves:" << endl;
    for (int i = 0; i < numMoves; i++) {
        printBoard(possibleMoves[i]);
    }

    return 0;
}

