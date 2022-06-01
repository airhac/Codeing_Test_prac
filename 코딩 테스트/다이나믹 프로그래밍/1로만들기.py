x = int(input())

d = [0] * 30001
for i in range(2, x+1):
    d[i] = d[i-1] + 1 # 이 연산은 모든 수는 -1가 가능하니깐 -1을 하는 경우를 꼭 넣어준다.
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
    