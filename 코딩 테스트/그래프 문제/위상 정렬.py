from collections import deque

v, e = map(int, input().split())

cnt = [0] * (v+1)
graph = [[] for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    cnt[i] += 1

def topology_sort():
    result = []
    q = deque()
    
    #시작 할때 진입 차수가 0인 노드를 queue에 넣어줘야한다.
    for i in range(1,v+1):
        if cnt[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        
        result.append(node)
        
        for j in graph[node]:
            cnt[j] -= 1
            if cnt[j] == 0:
                q.append(j)

    for i in result:
        print(i, end='')
        
topology_sort()
    
        
    
       

    