# [
# [5, 6, 1],
# [2, 3, 4],
# [7, x, 8]
# ]
# i = 2, j = 1, max_size = 3

from copy import deepcopy

wildcard = 'x'
class Node():
    state = None
    moves = []

    def __init__(self, state, moves = []):
        self.state = state
        self.moves = moves

    def __eq__(self, other):
        if other is None:
            return False
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] != other.state[row][col]:
                    return False
        return True

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
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == wildcard:
                    row = i
                    col = j
                    break

        movements = []
        # Left
        if col+1 < max_size:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row, col+1)
            new_state.insert_move('Left')
            movements.append(new_state)
        # Right
        if col-1 >= 0:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row, col-1)
            new_state.insert_move('Right')
            movements.append(new_state)
        # Up
        if row+1 < max_size:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row+1, col)
            new_state.insert_move('Up')
            movements.append(new_state)
        # Down
        if row-1 >= 0:
            new_state = Node(deepcopy(self.state), self.moves.copy())
            new_state.swap(row, col, row-1, col)
            new_state.insert_move('Down')
            movements.append(new_state)
        
        return movements