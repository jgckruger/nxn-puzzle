from classes.graph import GraphBFS
moves_16 = [
    [2,3,1],
    [8,'x',4],
    [7,6,5],
]
goal = [
    [1,2,3],
    [8,'x',4],
    [7,6,5],
]
# goal_state = [
#     ['x', 2, 3],
#     [4, 5, 6],
#     [7, 8, 1],
# ]

moves = GraphBFS().bfs(moves_16, goal)
print(moves)
