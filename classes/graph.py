from classes.node import Node
import collections

# Source: ethesis.nitrkl.ac.in/5575/1/110CS0081-1.pdf
class GraphBFS():
    def bfs(self, start_matrix, goal_matrix):
        start = Node(start_matrix)
        goal = Node(goal_matrix)

        prev = None
        list_of_visited = []
        #list_of_states = [start]
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
            new_positions = [ state for state in state.possible_movements() if not(state in list_of_visited) ]
            list_of_states += new_positions
            list_of_visited.append(state)
    
        return None