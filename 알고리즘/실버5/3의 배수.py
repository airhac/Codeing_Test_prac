import sys
from functools import reduce
input = sys.stdin.readline
N = input().strip()
cnt = 0
while len(N) != 1:
    cnt+=1
    N = str(reduce(lambda x,y : int(x) + int(y), N))
    # N = str(sum(map(int, list(N))))
print(cnt)
if int(N) % 3 == 0:
    print('YES')
else:
    print('NO')