###dfs

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
######bfs
# from collections import deque
# def solution(info, edges):
#     answer = 0
#     n = len(info)
#     graph = [set() for _ in range(n)]
#     for edge in edges:
#         a, b = edge
#         graph[a].add(b)
        
#     q = deque([[0, 1, 0, set()]])#양의 개수 늑대개수 현재 노드
#     while q:
#         now, sheep, wolf, next_node = q.popleft()
#         answer = max(sheep, answer)
#         next_node |= graph[now]
#         print(next_node)
#         print(type(next_node))
#         for i in next_node:
#             if info[i] == 1:
#                 if sheep != wolf + 1:
#                     q.append((i, sheep, wolf + 1, next_node - {i}))
#             else:
#                 q.append((i, sheep + 1, wolf, next_node - {i}))    
#     return answer
print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))