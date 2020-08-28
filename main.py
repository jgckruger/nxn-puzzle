from classes.graph import GraphBFS
easy = [
    [1,3,4],
    [8,6,2],
    [7,'x',5],
]
medium = [
    [2,8,1],
    ['x',4,3],
    [7,6,5],
]
hard = [
    [2,8,1],
    [4,6,3],
    ['x',7,5],
]
novo = [
    [8,3,5],
    [4,1,6],
    [2,7,'x'],
]
goal = [
    [1, 2, 3],
    [8, 'x', 4],
    [7, 6, 5],
]
# goal_state = [
#     ['x', 2, 3],
#     [4, 5, 6],
#     [7, 8, 1],
# ]

moves = GraphBFS().bfs(hard, goal)
print(moves)
