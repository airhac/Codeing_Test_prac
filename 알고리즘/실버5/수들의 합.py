import sys
input = sys.stdin.readline

N = int(input())
tot = 0
cnt = 0
for i in range(1, N + 1):
    tot += i
    if tot > N:
        break
    cnt += 1
    
print(cnt)