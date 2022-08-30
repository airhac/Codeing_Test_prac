# def solution(n, wires):
#     INF = int(1e9)
#     answer = INF
#     graph = [[] for _ in range(n + 1)]
#     for a, b in wires:
#         graph[a].append(b)
#         graph[b].append(a)
#     for wire in wires:
#         visited = [0] * (n + 1)
#         visited[wire[0]] = 1
#         visited[wire[1]] = 1
#         res = []
#         for i in range(2):
#             q = [wire[i]]
#             cost = 0
#             while q:
#                 now = q.pop()
#                 for i in graph[now]:
#                     if visited[i] != 1:
#                         cost += 1
#                         visited[i] = 1
#                         q.append(i)
#             res.append(cost)
            
#         answer = min(answer, abs(res[1] - res[0]))
#     return answer
# from collections import defaultdict
# def solution(n, wires):
#     answer = 0
    
#     def find_parent(parent, a):
#         if parent[a] != a:
#             parent[a] = find_parent(parent, parent[a])
#         return parent[a]
    
#     def union_parent(parent, a, b):
#         a = find_parent(parent, a)
#         b = find_parent(parent, b)
        
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b
            
            
#     INF = int(1e9)
#     answer = INF   
#     for idx in range(n - 1):
#         parent = [0] * (n + 1)
#         for i in range(1, n + 1):
#             parent[i] = i
#         for serial, wire in enumerate(wires):
#             if serial == idx:
#                 continue
#             a, b = wire
#             if find_parent(parent, a) != find_parent(parent, b):
#                 union_parent(parent, a, b)
                
#         print(parent)
#         tops = defaultdict(int)
#         tops1 = defaultdict(int)
#         for i in range(1, n + 1):
#             tops[parent[i]] += 1
#             tops1[find_parent(parent, i)] += 1
#         print(tops)
#         print(tops1)
#         top = list(tops.values())
#         answer = min(answer, abs(top[0] - top[1]))
#     return answer
# print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))
# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans
print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))