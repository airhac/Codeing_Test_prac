import sys
input = sys.stdin.readline
N = int(input())
def fac(N):
    if N == 1 or  N == 0:
        return 1
    return N * fac(N - 1)
res = list(str(fac(N)))
res.reverse()
cnt = 0
for i in res:
    if i != '0':
        break
    cnt += 1
print(cnt)
##다름사람풀이
a=int(input())
print(a//5+a//25+a//125)
#5로 나누는 이유
#펙토리얼이 뒤에 0 이 생길 수 있는 조건은 2, 5, 10이다
#10은 이미 2, 5를 포함하고 있으며 5가 포함되어있을때 0이생김 5가 이쓴 개수를 확인하면 0의 개수도 알수있습니다.

