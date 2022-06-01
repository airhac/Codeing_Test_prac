from collections import deque
import copy

n = int(input())

graph = [[] for i in range(n+1)]
hour = [0] * (n+1)
indegree = [0] * (n+1)

#graph에 각 노드의 연결 노드를 넣어준다
for i in range(1,n+1):
    row = list(map(int, input().split()))
    hour.append(row[0])
    for r in row[1:-1]:
        graph[r].append(i)#r 에서 i로 이동가능 
        indegree[i] +=1

def topology_sort():
    result = copy.deepcopy(hour)
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            result[i] = max(result[i],result[now] + hour[i])
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)
                