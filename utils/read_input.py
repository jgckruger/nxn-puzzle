import copy

def read_input(filepath):
    
    with open(filepath) as fp:
        line = fp.readline()
        N = int(line[0])
        init_matrix = [[None for x in range(N)] for y in range(N)] 
        goal_matrix = copy.deepcopy(init_matrix)
        i = 0
        while True:
            line = fp.readline()
            if not line:
                break
            line = line[:-1] if line[-1] == '\n' else line
            numbers = line.split(',')
            if numbers[0] == '-':
                continue
            assert len(numbers) == N            

            for j in range(N):
                goal_matrix[i][j] = i*N+j+1
                init_matrix[i][j] = numbers[j] if numbers[j] == 0 else int(numbers[j])
            goal_matrix[N-1][N-1] = 0
            i+=1
            

    return init_matrix, goal_matrix