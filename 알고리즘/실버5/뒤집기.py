import sys
input = sys.stdin.readline
S = input().strip()
if len(set(S)) != 1:
    cnt = 0
    for i in range(len(S) - 1):
        if S[i] != S[i+1]:
            cnt += 1
    print((cnt+ 1)//2)
else:
    print(0)

