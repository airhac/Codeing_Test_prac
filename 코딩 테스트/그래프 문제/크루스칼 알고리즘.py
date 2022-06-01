#최소 신장 트리 알고리즘
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

#모든 간선을 담을 리스트와 결과값을 더할 result
edges = []
result = 0

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result +=cost

print(result)



