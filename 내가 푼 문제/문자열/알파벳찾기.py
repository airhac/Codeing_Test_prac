S = list(input())
l = [-1 for _ in range(0,26)]
for s in range(len(S)):
    n = ord(S[s]) - 97
    if l[n] == -1:
        l[n] = s
for j in l:
    print(j, end=' ')