from collections import deque

def change_dir(dir_c,dir):
    if dir == 'L':
        dir_c = (dir_c - 1)%4
    else:
        dir_c = (dir_c + 1)%4
    return dir_c




N = int(input())
graph = [[0] *N for _ in range(N)]
K = int(input())

#사과의 위치를 입력받음
#사과가 있는 곳을 1로 둔다.
for k in range(K):
    x, y = input().split(' ')
    graph[int(x)-1][int(y)-1] = 2

L =int(input())
s_rot = {}
for l in range(L):
    time, dir = input().split(' ')
    s_rot[int(time)] = dir

#위치 변경
#오른쪽, 아래, 왼쪽, 위쪽
dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph[0][0] = 1
#현재 방향의 인덱스
dir_c = 0
x = 0
y = 0
q = []
queue = deque(q)
queue.appendleft((0,0))
cnt = 1
while True:
    x = x + dx[dir_c]
    y = y + dy[dir_c]
    #벽을 만나면,자기 자신을 만났을때 종료합니다.
    if x < 0 or y < 0 or x >= N or y>=N or graph[x][y] == 1:
        break
    else:
        #사과가 있을떄는 길이를 늘려주고 없을때는 줄입니다.
        if graph[x][y] != 2:
            qx,qy = queue.pop()
            graph[qx][qy] = 0
        graph[x][y] = 1
        queue.appendleft((x,y))
        if cnt in s_rot.keys():
            dir_c = change_dir(dir_c,s_rot[cnt])
        cnt+=1
print(cnt)
#다른 사람 풀이
# import sys
# n = int(sys.stdin.readline())
# apple = set([tuple(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))])
# cmd = [list(sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]
# snake = [[-2]*n for _ in range(n)]
# snake[0][0] = 0
# x,y,d = 0,0,0
# l = 1
# t = 0
# idx = 0
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# # print((2,5) in apple)

# while True:
#     t += 1
#     l += 1
#     x += dx[d]
#     y += dy[d]
#     if x < 0 or x >= n or y < 0 or y >= n:
#         break
#     if snake[x][y] >= t-l+1:
#         break
#     if (x+1,y+1) in apple:
#         apple.remove((x+1,y+1))
#     else:
#         l -= 1
#     snake[x][y]=t

#     if idx < len(cmd) and int(cmd[idx][0]) == t:
#         if cmd[idx][1] == 'D':
#             d = (d+1) % 4
#         else:
#             d = (d+3) % 4
#         idx += 1
# print(t)
