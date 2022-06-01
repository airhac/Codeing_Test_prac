def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]

def union_team(parent, x, y):
    a = find_team(parent, x)
    b = find_team(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    c , a, b = map(int, input().split())
    if c == 0:
        union_team(parent, a, b)
    elif c == 1:
        if find_team(parent, a) == find_team(parent, b):
            print('YES')
        else:
            print('NO')