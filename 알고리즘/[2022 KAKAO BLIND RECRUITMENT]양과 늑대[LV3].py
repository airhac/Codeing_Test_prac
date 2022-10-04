def solution(info, edges):
    n = len(info)
    graph = [set() for _ in range(n)]
    for edge in edges:
        a, b = edge
        graph[a].add(b)
    def dfs(answer, sheep, wolf, next_nodes):
        if sheep <= wolf:
            return answer
        else:
            answer = max(answer, sheep)
            for i in next_nodes:
                child = graph[i]
                next_nodes |= child
                next_nodes -= set([i])
                if info[i] == 0:
                    sheep += 1
                else:
                    wolf += 1
                answer = dfs(answer, sheep, wolf, next_nodes)
                next_nodes |= set([i])
                next_nodes -= child
                if info[i] == 0:
                    sheep -= 1
                else:
                    wolf -= 1
        return answer   
                
    answer = dfs(0, 1, 0, graph[0])
    return answer