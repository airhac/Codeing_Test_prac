N = int(input())
plans = input().split()
x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for plan in plans:
    #이동 좌표 설정
    for i in range(len(dir)):#어느 이동경로인지 하나씩 비교 
        if plan == dir[i]:
            xn = x + dx[i]
            yn = y + dy[i]
    #공간을 벗어나는 경우 무시
    if xn <1 or xn > N or yn < 1 or yn >N:
        continue
    #이동 실행
    x = xn
    y = yn

print("{} {}".format(x,y))
#print(x, y)