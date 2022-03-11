import sys
n = int(input())
l = list(map(int,sys.stdin.readline().split()))
def max(i, f):
    if l[i] > f:
        return l[i]
    return f
def min(i, f):
    if l[i] < f:
        return l[i]
    return f
mx, mn = l[0], l[0]
for i in range(1,len(l)):
    mx = max(i ,mx)
    mn = min(i, mn)

print(mn , mx)
#최대한 파이썬 함수를 사용하지 않고 구현해보려고 했습니다. 