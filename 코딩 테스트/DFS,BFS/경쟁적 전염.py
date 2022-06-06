# import sys
# from collections import deque
# input = sys.stdin.readline 
# N, K = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# S, X, Y = map(int, input().split())
# q = [(graph[i][j] , i, j) for i in range(N) for j in range(N) if graph[i][j] != 0]

# dx, dy = [-1, 1, 0, 0], [0, 0, -1 , 1]
# def BFS(graph, S, X, Y):
#     queue = deque(q)
#     count = 0
#     while queue:
#         if count == S:
#             break
#         for _ in range(len(queue)):   
#             val , x, y = queue.popleft()
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if graph[nx][ny] == 0:
#                         graph[nx][ny] = val
#                         queue.append((val, nx, ny))
#         count+=1
#     return graph[X-1][Y-1] if graph[X-1][Y-1] != 0 else 0
# q.sort()
# print(BFS(graph, S, X, Y))
#queue를 안쓰고 bfs 방법으로 해결 방법
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    maps = [(list(map(int, input().split()))) for _ in range(n)]
    s, x, y = map(int, input().split())

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x -= 1
    y -= 1
    if maps[x][y] != 0 :
        print(maps[x][y])
        return
    
    q = []
    visited = [(x, y)]
    maps[x][y] = 1001
    for i in range(s):
        temp = []
        while visited:
            x, y = visited.pop()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if nx > -1 and ny > -1 and nx < n and ny < n:
                    if maps[nx][ny] != 0 and maps[nx][ny] != 1001:
                        q.append(maps[nx][ny])
                    elif maps[nx][ny] == 0:
                        temp.append((nx, ny))
                    maps[nx][ny] = 1001
        visited = temp[:]
        if q :
            print(min(q))
            return
    if not q :
        print(0)

solution()
    