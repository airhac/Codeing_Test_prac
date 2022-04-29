def dfs(graph, v, visited):
    #현재 있는 노드 방문 처리
    visited[v] = True
    print(v, end='')
    #방문한 노드의 인접한 노드를 다 검사
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, v, visited)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)