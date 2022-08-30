# import sys
# input = sys.stdin.readline
# e, s, m, cnt = 1, 1, 1, 1
# E, S, M = map(int, input().strip().split())

# while True:
#     if e == E and s == S and m == M:
#         break
#     e+=1; s+=1; m+=1; cnt+=1
#     if e >= 16: e-=15
#     if s >= 29: s-=28
#     if m >= 20: m-=19

# print(cnt)
#####다른풀이

import sys
input = sys.stdin.readline
e, s, m, cnt = 1, 1, 1, 1
E, S, M = map(int, input().strip().split())

while True:
    if (e - E) % 15 == 0 and (s - S) % 28 == 0 and (m - M) % 19 == 0:
        break
    e+=1; s+=1; m+=1; cnt+=1
    
print(cnt)
