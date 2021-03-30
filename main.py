from classes.graph import Graph
from utils.read_input import read_input
import time
import sys

# Usage: python3 main.py path_to_file should_use_hash_set?
# path to file: ./samples/6moves.txt
# should_use_hash_set: True or False, defaults to True

try:
    filepath = sys.argv[1]
except:
    filepath = 'samples/sample.txt'
try:
    should_use_hash_set = sys.argv[2] != 'False'
except:
    should_use_hash_set = True

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
moves = Graph().bfs(init_matrix, goal_matrix, should_use_hash_set) 
print("--- %.2f seconds ---" % (time.time() - t))
print(moves)
