def sum(a, b):
    return a+b

while True:
    A , B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(sum(A,B))