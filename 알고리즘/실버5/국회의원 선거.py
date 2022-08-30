import sys
input = sys.stdin.readline
N = int(input())
candi = int(input())
try:
    rest = [i for i in int(input())]
    cnt = 0
    while candi > max(rest):
        rest.sort(reverse=True)
        candi += 1
        rest[0] -= 1
        cnt += 1
except:
    print(0)