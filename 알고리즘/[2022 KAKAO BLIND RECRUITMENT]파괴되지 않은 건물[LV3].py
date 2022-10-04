def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    for k in skill:
        i, x1, y1, x2, y2, cost = k
        if i == 1:
            graph[x1][y1] -= cost
            graph[x2 + 1][y2 + 1] -= cost
            graph[x1][y2 + 1] += cost
            graph[x2 + 1][y1] += cost
        else:
            graph[x1][y1] += cost
            graph[x2 + 1][y2 + 1] += cost
            graph[x1][y2 + 1] -= cost
            graph[x2 + 1][y1] -= cost
    #위 아래로 누적합    
    for i in range(1, n + 1):
        for j in range(m + 1):
            graph[i][j] = graph[i - 1][j] + graph[i][j]
    #옆으로 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            graph[i][j] = graph[i][j - 1] + graph[i][j]        
    
    for i in range(n):
        for j in range(m):
            board[i][j] = board[i][j] + graph[i][j]
            if board[i][j] <= 0:
                answer += 1
                
    return n * m - answer