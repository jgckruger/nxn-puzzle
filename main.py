from classes.graph import GraphBFS
from utils.read_input import read_input
import time
import sys

try:
    filepath = sys.argv[1]
except:
    filepath = 'samples/sample.txt'

init_matrix, goal_matrix = read_input(filepath)

"""
init_matrix = [
    [2,3,'x'],
    [1,5,6],
    [4,7,8],
]
goal_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,'x'],
]
"""
t = time.time()
moves = GraphBFS().bfs(init_matrix, goal_matrix) 
print("--- %.2f seconds ---" % (time.time() - t))
print(moves)
