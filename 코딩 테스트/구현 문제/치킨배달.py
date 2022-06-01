# from itertools import combinations

# def min_dis(com_chicken_home, homes):
#     dis = 0
#     for home in homes:
#         before = 100
#         for chicken in com_chicken_home:
#             hx, hy = home
#             cx, cy = chicken
#             before = min(before, abs(hx - cx) + abs(hy - cy))
#             print(abs(hx - cx) + abs(hy - cy))
    
#         dis+=before
        
#     return dis
# n, m  = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# #각 치킨집의 위치 구하기
# chicken_home = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 2:
#             chicken_home.append((i,j))

# com_chicken_homes = list(combinations(chicken_home, m))
# #각 집의 위치 구하기
# homes = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             homes.append((i,j))
# distance = []
# for com_chicken_home in com_chicken_homes:
#     distance.append(min_dis(com_chicken_home, homes))
# print(min(distance))
#다른 사람풀이
import sys
N,M = map(int,sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
  for j in range(N):
    if city[i][j] == 2:
      chicken.append((i,j))
    elif city[i][j] == 1:
      house.append((i,j))

chicken_distance = []
for i in range(len(house)):
  chicken_distance.append([])
  for j in range(len(chicken)):
    chicken_distance[-1].append((abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1]),j))
  chicken_distance[-1].sort(key = lambda x: x[0])

ans = 1000000000
def city_chicken_distance():
  global ans
  a = 0
  for i in chicken_distance:
    for j in i:
      if j[1] in survived:
        a += j[0]
        break
    if a >= ans:
      return
  ans = min(ans,a)

def open(M,n):
  if M == 0:
    city_chicken_distance()
  for i in range(n,len(chicken)):
    if i not in survived:
      survived.add(i)
      open(M-1,i+1)
      survived.remove(i)

survived = set()
open(M,0)

print(ans)
#222222222222222
# from sys import stdin
# from itertools import combinations as comb
# r = stdin.readline

# n,m = map(int, r().strip().split())
# city = [r().strip().split() for i in range(n)]
# ans = 1e9
# houses = []
# chickens = []
# for i in range(n):
#     for j in range(n):
#         if city[i][j] == '1':
#             houses.append((i,j))
#         elif city[i][j] == '2':
#             chickens.append((i,j))

# dists = [list(map(lambda x : abs(x[0]-c[0]) + abs(x[1]-c[1]), houses)) for c in chickens]
# for co in comb((i for i in range(len(chickens))), m):
#     res = sum(map(min, zip(*[dists[i] for i in co])))


#     if res < ans:
#         ans = res
# print(ans)