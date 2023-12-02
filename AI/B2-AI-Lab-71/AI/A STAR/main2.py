import copy
import numpy as np


class Node:
    def __init__(self, matrix, parent, goal_state, f_A):
        self.matrix = matrix
        self.parent = parent
        self.goal_state = goal_state
        self.g_A = self.calculategA(self.goal_state)
        self.f_A = f_A
        self.next = None
        self.value = self.g_A + self.f_A

    def calculategA(self, goal_state):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != 0:
                    goal_i, goal_j = divmod(self.matrix[i][j] - 1, 3)
                    count += abs(i - goal_i) + abs(j - goal_j)
        return count

class PriorityQueue:
    def __init__(self, goal_state, starting_state):
        self.head = None
        self.tail = None
        self.goal_state = goal_state
        self.starting_state = starting_state

    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.value > node.value:
            node.next = self.head
            self.head = node
            return
        prev = self.head
        current = self.head.next

        while current is not None and current.value <= node.value:
            prev = current
            current = current.next

        prev.next = node
        node.next = current

    def getMin(self):
        if self.head is None:
            return None
        if self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    def isSafe(self):
        return self.goal_state == self.starting_state

    def ifExists(self, state):
        temp = self.head
        while temp is not None:
            if np.array_equal(temp.matrix, state):
                return True
            temp = temp.next
        return False

    def print(self):
        temp = self.head
        while temp is not None:
            print("1).", temp.matrix, temp.value)
            temp = temp.next

class Main:
    def __init__(self):
        self.moves = 0
        self.matrix = [[1, 2, 4], [3, 5, 6], [0, 8, 7]]
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.i_blank = 2 
        self.j_blank = 0
        self.outputMatrix = [[[] for _ in range(3)] for _ in range(3)]

    def takeInput(self):
        self.i_blank = int(input("Enter the blank position (row): "))
        self.j_blank = int(input("Enter the blank position (column): "))
        for i in range(3):
            for j in range(3):
                if i == self.i_blank and j == self.j_blank:
                    continue
                number = int(input(f"Enter the number at position {i}th row and {j}th column: "))
                if 1 <= number <= 8:
                    self.matrix[i][j] = number
                else:
                    print("Not a valid number")

    def generateAllMoves(self):
        self.outputMatrix = [copy.deepcopy(self.matrix) for _ in range(4)]
        n = self.i_blank
        p = self.j_blank
        self.possibleMoves = [(n - 1, p), (n, p - 1), (n, p + 1), (n + 1, p)]
        if 0 <= n < 3 and 0 <= p < 3:
            self.moves = 4
            count = 0
            for i in range(4):
                if 0 <= self.possibleMoves[i][0] < 3 and 0 <= self.possibleMoves[i][1] < 3:
                    self.outputMatrix[count][n][p] = self.matrix[self.possibleMoves[i][0]][self.possibleMoves[i][1]]
                    self.outputMatrix[count][self.possibleMoves[i][0]][self.possibleMoves[i][1]] = 0
                    count += 1
        return self.outputMatrix

    def calculateBestMoves(self):
        s = []
        for i in range(self.moves):
            array = np.array(self.outputMatrix[i])
            s.append(np.sum(abs(array - np.array(self.goal_state))))
        return s

puzzle = Main()
starting_state = puzzle.matrix
pq = PriorityQueue(puzzle.goal_state, starting_state)
pq.insert(Node(starting_state, starting_state, puzzle.goal_state, 0))
count = 0
temp = Node(starting_state, starting_state, starting_state, 0)
while temp is not None and not np.array_equal(temp.matrix, puzzle.goal_state):
    temp = pq.getMin()
    if temp is None:
        print("No solution found.")
        break

    _i = 0
    _j = 0
    for i in range(3):
        for j in range(3):
            if temp.matrix[i][j] == 0:
                _i = i
                _j = j
                break

    puzzle.matrix = temp.matrix
    puzzle.i_blank = _i
    puzzle.j_blank = _j
    goal_states = puzzle.generateAllMoves()
    scores = puzzle.calculateBestMoves()
    print("min", temp.matrix)
    print("goal_states", goal_states)
    print("scores", scores)

    for i in range(len(scores)):
        if not pq.ifExists(goal_states[i]):
            pq.insert(Node(goal_states[i], temp.matrix, puzzle.goal_state, scores[i]))
    pq.print()
