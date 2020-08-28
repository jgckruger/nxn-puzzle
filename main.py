from classes.graph import GraphBFS
moves_16 = [
    [2,3,'x'],
    [1,5,6],
    [4,7,8],
]
goal = [
    [1,2,3],
    [4,5,6],
    [7,8,'x'],
]
# goal_state = [
#     ['x', 2, 3],
#     [4, 5, 6],
#     [7, 8, 1],
# ]

moves = GraphBFS().bfs(moves_16, goal)
print(moves)
