N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input())
    graph[a][b] = 1
    graph[b][a] = 1
    
#거쳐갈 노드 x와 최종 목적지인 k를 받아 옵니다.
x, k = map(int, input().split())

for l in range(1, n+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)