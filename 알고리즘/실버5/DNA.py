import sys
from collections import Counter
input = sys.stdin.readline
N, M = map(int, input().split())
dna_s = []
for _ in range(N):
    dna_s.append(input().strip())
cnt = 0
dna = ''
for c in zip(*dna_s):
    dic = Counter(c)
    if len(dic) > 1:
        l = sorted([[value, key] for key, value in dic.most_common()], key=lambda x : (-(x[0]), (x[1])))
        dna += l[0][1]
        cnt += len(c) - l[0][0]
    else:
       dna += c[0] 
print(dna)
print(cnt)
##다른 사람 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
ans = ""
r = n * m
for i in range(m):
    d = dict()
    d["A"], d["T"], d["G"], d["C"] = 0, 0, 0, 0
    for j in range(n):
        d[arr[j][i]] += 1
    m = 0
    temp = ""
    for e in d:
        if m < d[e]:
            m = d[e]
            temp = e
        elif m == d[e]:
            if temp > e:
                temp = e
    r -= d[temp]
    ans += temp
print(ans)
print(r)