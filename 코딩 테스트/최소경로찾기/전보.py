import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        #현재 거리의 시간보다 더 짧은 시간의 정보 유지
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                #인접한 노드에 계산한 값을 알려준다.
                distance[i[0]] = cost
                heapq.heappush((cost, i[0]))
                
dijkstra(start)

count = 0
time = 0

for d in distance:
    if d != INF:
        count+=1
        time = max(time, d)
#시작노드 제외
print(count-1, time)
        
         