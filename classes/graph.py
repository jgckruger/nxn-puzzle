from classes.node import Node
import collections
import heapq

# Source of the image of BFS for 8-puzzle ethesis.nitrkl.ac.in/5575/1/110CS0081-1.pdf
class Graph():
    def astar(self, start_matrix, goal_matrix, should_use_hash_set = True):   
        start = Node(start_matrix)
        goal = Node(goal_matrix)

        start.calculate_weight(goal)
        
        prev = None
        list_of_visited = set()
        list_of_states = [start]
        heapq.heapify(list_of_states)
        height = 0
        comp = 0

        
        while len(list_of_states):
            state = heapq.heappop(list_of_states)

            state_height = len(state.moves)
            if height != state_height:
                height = state_height
                print('Weight: ', state.weight, 'Current height: ', height, 'Heap size: ', len(list_of_states))
            comp += 1
            if state == goal:
                print('Comparisons: ', comp)
                print('Final solution length: ', len(state.moves))
                return state.moves
            new_positions = [ state for state in state.possible_movements() if not(state.flatten() in list_of_visited) ]

            for position in new_positions:
                position.calculate_weight(goal)
                heapq.heappush(list_of_states, position)

            if should_use_hash_set:
                list_of_visited.add(state.flatten())
    
        return None

    def bfs(self, start_matrix, goal_matrix, should_use_hash_set = True):
        start = Node(start_matrix)
        goal = Node(goal_matrix)

        prev = None
        list_of_visited = set()
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
            new_positions = [ state for state in state.possible_movements() if not(state.flatten() in list_of_visited) ]
            list_of_states += new_positions
            if should_use_hash_set:
                list_of_visited.add(state.flatten())
    
        return None