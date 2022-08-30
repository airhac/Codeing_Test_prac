# import sys
# input = sys.stdin.readline
# N = int(input())
# dirs = list(input().strip())
# v = [[0] * N for _ in range(N)]
# h = [[0] * N for _ in range(N)]
# x, y = 0, 0
# for i in range(len(dirs)):
#     nx = x
#     ny = y
#     dir = dirs[i]
#     if dir == 'U':
#         nx -= 1
#         if (nx < 0): continue
#         v[nx][ny] = 1
#         v[x][y] = 1
#         x = nx
#     elif dir == 'D':
#         nx += 1
#         if (nx >= N): continue
#         v[nx][ny] = 1
#         v[x][y] = 1
#         x = nx
#     elif dir == 'R':
#         ny += 1
#         if (ny >= N): continue
#         h[nx][ny] = 1
#         h[x][y] = 1
#         y = ny
#     elif dir == 'L':
#         ny -= 1
#         if (ny < 0): continue
#         h[nx][ny] = 1
#         h[x][y] = 1
#         y = ny
        
# for i in range(N):
#     for j in range(N):
#         if v[i][j] + h [i][j] > 1:
#             print('+', end='')
#         else:
#             if v[i][j] == 1:
#                 print('|', end='')
#             elif h[i][j] == 1:
#                 print('-', end='')
#             else:
#                 print('.', end='')
#     if i != N-1:
#         print()
# for dir in dirs:
#     if before:
#         if dir == 'D':
#             if before == 'R' or before == 'L':
#                 graph[x][y] = '+'
#                 x, y = x + dx[2], y + dy[2]
#                 before = dir
#             else:
#                 graph[x][y] = '|'
#                 x, y = x + dx[2], y + dy[2]
#                 before = dir
                
#         elif dir == 'L':
#             if before == 'D' or before == 'U':
#                 graph[x][y] = '+'
#                 x, y = x + dx[1], y + dy[1]
#                 before = dir
#             else:
#                 graph[x][y] = '-'
#                 x, y = x + dx[1], y + dy[1]
#                 before = dir
#         elif dir == 'R':
#             if before == 'D' or before == 'U':
#                 graph[x][y] = '+'
#                 x, y = x + dx[3], y + dy[3]
#                 before = dir
#             else:
#                 graph[x][y] = '-'
#                 x, y = x + dx[3], y + dy[3]
#                 before = dir
#         else:
#             if before == 'R' or before == 'L':
#                 graph[x][y] = '+'
#                 x, y = x + dx[0], y + dy[0]
#                 before = dir
#             else:
#                 graph[x][y] = '|'
#                 x, y = x + dx[0], y + dy[0]
#                 before = dir
#     else:
#         if dir == 'D':
#             graph[x][y] = '|'
#             x, y = x + dx[2], y + dy[2]
#             before = dir
#         elif dir == 'L':
#             graph[x][y] = '-'
#             x, y = x + dx[1], y + dy[1]
#             before = dir
#         elif dir == 'R':
#             graph[x][y] = '-'
#             x, y = x + dx[3], y + dy[3]
#             before = dir
#         else:
#             graph[x][y] = '|'
#             x, y = x + dx[0], y + dy[0]
#             before = dir
#다른사람 풀이
n=int(input())
m=[[0]*n for i in range(n)]
x=y=0
def F():
    m[x][y]|=abs(v)|abs(w)<<1#bit이동 연산자가 우선순위가 있습니다.
for s in input():
    v,w=[(-1,0),(1,0),(0,-1),(0,1)]['UDLR'.index(s)]
    if 0<=x+v<n and 0<=y+w<n:
        F()
        x,y=x+v,y+w
        F()
for i in m:print(''.join('.|-+'[j]for j in i))

##
# N, S = int(input()), input()
# A = [[0 for i in range(N)] for j in range(N)]

# dx, dy, way = [-1, 1, 0, 0], [0, 0, 1, -1], "UDRL"
# x, y = 0, 0

# for w in S:
#     i = way.find(w)
#     xx, yy = x+dx[i], y+dy[i]
#     if 0 <= xx < N and 0 <= yy < N:
#         A[x][y] |= 1 << (i//2)
#         A[xx][yy] |= 1 << (i//2)
#         x, y = xx, yy

# p = ['.', '|', '-', '+']

# for row in A:
#     print("".join(p[i] for i in row))