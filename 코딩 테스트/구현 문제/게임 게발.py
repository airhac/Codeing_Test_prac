# N, M = map(int, input().split())
# dx, dy, d = map( int, input().split())
# g_map = []
# for n in range(N):
#     row = list(map(int,input().split()))
#     g_map.append(row)

# ver = [-1, 0, 1, 0]
# hor = [0, 1, 0, -1]
# car = [0, 1, 2 , 3]

# result = 0
# while True:
#     cnt = 0
#     result +=1
#     g_map[dx][dy] = 1
    
#     for _ in range(len(car)):
#         if d == -1:
#             d=3
#         xn = dx + hor[d]
#         yn = dy + ver[d]
        
#         if g_map[xn][yn] == 1 or xn <=0 or xn >M or yn <=0 or yn >N:
#             d-=1
#             cnt+=1
#             continue
#         dx = xn
#         dy = yn
        
#         break
    
#     if cnt == 4:
#         break
    
        
# print(result)  
# 현재 시간 복잡도는 n
#N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
#현재 캐릭터의  X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼족으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    #이동한 위치 그다음에는 
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time +=1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 뒤로 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
        
    
    
    
        
        
        
        