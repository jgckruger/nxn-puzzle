from classes.node import Node
import collections
import numpy as np

# Source of the image of BFS for 8-puzzle ethesis.nitrkl.ac.in/5575/1/110CS0081-1.pdf
class GraphBFS():
    def cvtNumber(self, arr):
        rpta = 0
        for i, x in enumerate(arr):
            rpta += int(x * 10**i)
        return rpta

    def bfs(self, start_matrix, goal_matrix, should_use_hash_set = False):
        start = Node(start_matrix)
        goal = Node(goal_matrix)

        prev = None
        list_of_visited = set()
        #list_of_states = [start]

        matrix_visited = np.zeros((int(9e8+1)))
        list_of_states = collections.deque([start]) 
        height = 0
        comp = 0

        
        while len(list_of_states):
            #state = list_of_states.pop(0)
            state = list_of_states.popleft()
            state_height = len(state.moves)
            if height != state_height:
                height = state_height
                print('Current height: ', height)
            comp += 1
            if state == goal:
                print('Comparisons: ', comp)
                print('Final solution length: ', len(state.moves))
                return state.moves
            
            #new_positions = [ state for state in state.possible_movements() if not(state.flatten() in list_of_visited) ]
            new_positions = []
            for state in state.possible_movements():
                arr = [x for row in state.state for x in row]
                num = self.cvtNumber(arr)
                if matrix_visited[num] == 0:
                    matrix_visited[num] = 1
                    new_positions.append(state)

            list_of_states += new_positions
            #if should_use_hash_set:
            #    list_of_visited.add(state.flatten())
    
        return None