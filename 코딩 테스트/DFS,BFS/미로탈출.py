from collections import deque
from unittest import result


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    queue = deque((x,y))
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0 or nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
        #큐에 있는 곳 체크하기       
    
    return graph[n-1][m-1]

print(bfs(0,0))
                 
                 
                 