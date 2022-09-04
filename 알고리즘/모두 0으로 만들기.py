from collections import deque
def solution(a, edges):
    answer = -1
    graph = [[] for _ in range(len(a) + 1)]
    visited = [False] * (len(a))
    tree = []
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)
    q = deque([(-1, 0)])
    while q:
        before, now = q.popleft()
        tree.append((before,now))
        visited[now] = True
        for i in graph[now]:
            if not visited[i]:
                q.append((now, i))
                
    print(tree[::-1])            
    for t in tree[::-1]:
        parent, child = t
        weight = a[child]
        if a[child] != 0:
            answer += abs(weight)
            a[child] -= weight
            a[parent] += weight
            
    if a[0] == 0:
        return answer
    else:
        return -1

print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
########
