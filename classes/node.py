# [
# [5, 6, 1],
# [2, 3, 4],
# [7, x, 8]
# ]
# i = 2, j = 1, max_size = 3

from copy import deepcopy
import collections
from math import floor

wildcard = 'x'
class Node():
    state = None
    #moves = []
    moves = collections.deque()


    def __init__(self, state, moves = [], weight = 0):
        self.state = state
        self.moves = moves
        self.n = len(state)
        self.weight = weight

    def __eq__(self, other):
        if other is None:
            return False
        N = len(self.state)
        for row in range(N):
            for col in range(N):
                if self.state[row][col] != other.state[row][col]:
                    return False
        return True

    def __ne__(self, other):
        if other is None:
            return False
        N = len(self.state)
        for row in range(N):
            for col in range(N):
                if self.state[row][col] != other.state[row][col]:
                    return True
        return False

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def flatten(self):
        return str(self.state)

    def calculate_weight(self, goal):
        self.weight = self.manhattan_distance(goal)
        return self.weight

    def swap(self, i, j, new_i, new_j):
        temp = self.state[i][j]
        self.state[i][j] = self.state[new_i][new_j]
        self.state[new_i][new_j] = temp
        
    def insert_move(self, move):
        self.moves.append(move)

    def possible_movements(self):
        # Find the x
        row = col = -1
        max_size = len(self.state[0])
        for i in range(max_size):
            for j in range(max_size):
                if self.state[i][j] == wildcard:
                    row = i
                    col = j
                    break

        movements = []
        # Right
        if col+1 < max_size:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row, col+1)
            new_state.insert_move('Right')
            movements.append(new_state)
        # Left
        if col-1 >= 0:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row, col-1)
            new_state.insert_move('Left')
            movements.append(new_state)
        # Down
        if row+1 < max_size:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row+1, col)
            new_state.insert_move('Down')
            movements.append(new_state)
        # Up
        if row-1 >= 0:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row-1, col)
            new_state.insert_move('Up')
            movements.append(new_state)
        
        return movements

    def __str__(self):
        ret = ''
        for x in range(self.n):
            for y in range(self.n):
                ret += str(self.state[x][y]) + ' '
            ret +='\n'

        return ret

    def manhattan_distance(self, other):
        total_manhattan_distance = 0

        initial_positions = dict()
        goal_positions = dict()

        # sets the goal positions of each element
        for x in range(self.n):
            for y in range(self.n):
                goal = other.state[x][y]
                goal_positions[goal] = (x, y)

        # checks the lookup table for the goal positions of each element
        for x in range(self.n):
            for y in range(self.n):
                e = self.state[x][y]
                goal_x, goal_y = goal_positions[e]
                manhattan_distance = abs(goal_x - x) + abs(goal_y - y)
                total_manhattan_distance += abs(goal_x - x) + abs(goal_y - y)

        return total_manhattan_distance