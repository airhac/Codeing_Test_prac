import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
graph= [[0] * 100 for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            graph[i][j] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] > M:
            cnt+=1          
print(cnt)