import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    box = 0
    cnt = 0
    for book in books:
        box += book
        if box > M:
            box = book
            cnt+=1
    print(cnt + 1)