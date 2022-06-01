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
for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
print('각 원소가 속한 집합:', end = '')
for i in range(v+1):
    print(find_parent(parent, i), end='')
    
print()

print('부모 테이블', end='')
for i in range(v+1):
    print(parent[i], end='')
    