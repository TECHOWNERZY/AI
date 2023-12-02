import copy
import numpy as np
import queue

class Node:
    def __init__(self, matrix, parent, goal_state, h2_A, g_A):
        self.matrix = matrix
        self.parent = parent
        self.goal_state = goal_state
        self.g_A = g_A
        self.h1_A = self.calculatemisplaced(self.goal_state)
        self.h2_A = h2_A
        self.f_A = self.g_A + h2_A
        self.next = None
        self.value = self.f_A
    
    def calculatemisplaced(self, goal_state):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != goal_state[i][j]:
                    count += 1
        return count


class PriorityQueue:
    def __init__(self, goal_state, starting_state):
        self.head = None
        self.tail = None
        self.goal_state = goal_state
        self.starting_state = starting_state

    def insert(self, node, position=None):
        if position is None:
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
        else:
            if position == 0:
                node.next = self.head
                self.head = node
                return
            count = 0
            temp = self.head
            while count <= position - 1:
                temp = temp.next
                count = count + 1
            _temp = temp.next.next
            temp.next.next = None
            temp.next = node
            node.next = _temp

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
        count = 0
        while temp is not None:
            if np.array_equal(temp.matrix, state):
                count = count + 1
                return True, count
            temp = temp.next
            count = count + 1
        return False, -1

    def print(self):
        temp = self.head
        print("-------------------------------------")
        while temp is not None:
            print("->", temp.matrix, "value ->", temp.value)
            temp = temp.next

class Main:
    def __init__(self):
        self.moves = 0
        # self.matrix = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
        # self.goal_state = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
        self.matrix = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
        self.goal_state = [[6, 4, 7], [8, 5, 0], [3, 2 ,1]]

        self.i_blank = 2
        self.j_blank = 1
        self.outputMatrix = [[]]

    def generateAllMoves(self):
        self.outputMatrix = [copy.deepcopy(self.matrix) for _ in range(4)]
        n = self.i_blank
        p = self.j_blank
        self.possibleMoves = [(n - 1, p), (n, p - 1), (n, p + 1), (n + 1, p)]
        if (self.i_blank == 0 or self.i_blank == len(self.matrix) - 1) and (self.j_blank == 0 or self.j_blank == len(self.matrix) - 1):
            self.moves = 2
            count = 0
            for i in range(4):
                if (0 <= self.possibleMoves[i][0] <= 2) and (0 <= self.possibleMoves[i][1] <= 2):
                    self.outputMatrix[count][n][p] = self.matrix[self.possibleMoves[i][0]][self.possibleMoves[i][1]]
                    self.outputMatrix[count][self.possibleMoves[i][0]][self.possibleMoves[i][1]] = 0
                    count += 1
        elif self.i_blank + self.j_blank == 1 or self.j_blank == 2:
            self.moves = 3
            count = 0
            for i in range(4):
                if (0 <= self.possibleMoves[i][0] <= 2) and (0 <= self.possibleMoves[i][1] <= 2):
                    self.outputMatrix[count][n][p] = self.matrix[self.possibleMoves[i][0]][self.possibleMoves[i][1]]
                    self.outputMatrix[count][self.possibleMoves[i][0]][self.possibleMoves[i][1]] = 0
                    count += 1
        else:
            self.moves = 4
            count = 0
            for i in range(4):
                if (0 <= self.possibleMoves[i][0] <= 2) and (0 <= self.possibleMoves[i][1] <= 2):
                    self.outputMatrix[count][n][p] = self.matrix[self.possibleMoves[i][0]][self.possibleMoves[i][1]]
                    self.outputMatrix[count][self.possibleMoves[i][0]][self.possibleMoves[i][1]] = 0
                    count += 1
        return self.outputMatrix

    def calculateBestMoves(self):
        self.s = []
        for i in range(self.moves):
            array = np.array(self.outputMatrix[i])
            self.s.append(np.sum(np.sqrt(abs(np.square(array) - np.square(np.array(self.goal_state))))))
        return self.s
    
def updateParent(closed, open, newParent, parent, g_A):
    temp = closed.head
    temp1 = open.head
    while temp is not None:
        if np.array_equal(temp.parent, parent.matrix):
            while temp1 is not None:
                temp1.f_A = temp1.f_A - temp1.g_A + g_A + 1
                temp1.g_A = g_A + 1
                temp1 = temp1.next
            temp.parent = newParent
            temp.f_A = temp.f_A - temp.g_A + g_A + 1
            temp.g_A = g_A
            temp = temp.next

puzzle = Main()
starting_state = puzzle.matrix
pq = PriorityQueue(puzzle.goal_state, starting_state)
pq.insert(Node(starting_state, None, puzzle.goal_state, 0, 0))
count = 0
temp = Node(starting_state, starting_state, starting_state, 0, 0)
q = queue.Queue()

pq_c = PriorityQueue(puzzle.goal_state, starting_state)

while True:
    count = count + 1
    temp = pq.getMin()
    pq_c.insert(temp)
    q.put(temp)
    outputMatrix = puzzle.generateAllMoves()
    bestMoves = puzzle.calculateBestMoves()
    for i in range(len(outputMatrix)):
        exists, pos = pq.ifExists(outputMatrix[i])
        if exists:
            updateParent(pq_c, pq, temp.matrix, outputMatrix[i], temp.g_A)
            continue
        newNode = Node(outputMatrix[i], temp.matrix, puzzle.goal_state, bestMoves[i], temp.g_A + 1)
        pq.insert(newNode)

        if newNode.h1_A == 0:
            print("Reached Goal State!")
            while not q.empty():
                temp1 = q.get()
                print(temp1.matrix)
            exit(0)
