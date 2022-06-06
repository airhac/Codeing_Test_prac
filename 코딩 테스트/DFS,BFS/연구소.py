# #조합 사용한풀이
# from itertools import combinations
# import copy
# from collections import deque
# N, M = map(int, input().split())
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))

# def how_spread(graph):
#     result = 0
#     #감염체가 이동할 방행
#     dx = [-1, 0 , 1, 0]
#     dy = [0, -1 ,0, 1]
#     #감염체의 위치 파악하기
#     disease = []
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 2:
#                 disease.append((i,j))
    
#     queue = deque(disease)
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[nx][ny] == 0:
#                 graph[nx][ny] = 2
#                 queue.append((nx,ny))
        
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 result +=1
                
#     return result
# def build_wall(graph):
#     location = []
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 location.append((i,j))
#     #백트래킹으로 어느한 경우의 수의 벽을 세우면 그에대한 bfs로 감염정도를 확인
#     answer = []
#     for com_list in combinations(location, 3):
#         copy_graph = copy.deepcopy(graph)
#         for i,j in com_list:
#             copy_graph[i][j] = 1
#         answer.append(how_spread(copy_graph))
                
#     #안전지대가 최대인경우만 반환 시켜주면 됩니다.
#     return max(answer)

# print(build_wall(graph))
#이경우는 조합을 재귀함수로 짜는 방법인데 python3에서는 처리속도가 오래걸려 제시간안에 통과를 못한다0
# import copy
# N, M = map(int, input().split())
# graph = []
# answer = 0
# for i in range(N):
#     graph.append(list(map(int, input().split())))
# def disease(graph, x, y):
#     answer = 0
#     dx, dy = [-1, 0 ,1, 0], [0,-1, 0, 1]
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if nx >= 0 and ny >= 0 and nx < N and ny < M :
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = 2
#                 disease(graph, nx, ny)
                
# def get_score(graph):
#     score = 0
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 score +=1
#     return score     
# def build_wall(graph, count):
#     global answer
#     if count == 3:
#         copy_graph = copy.deepcopy(graph)
        
#         for i in range(N):
#             for j in range(M):
#                 if copy_graph[i][j] == 2:
#                     disease(copy_graph , i, j)
      
#         answer = max(answer, get_score(copy_graph))
#         return 
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 build_wall(graph,count + 1)
#                 #새로운 벽을 만들기 위해 초기화
#                 graph[i][j] = 0
                
# cnt = 0
# build_wall(graph, cnt)
# print(answer)
#이 경우는 dfs방식을 사용하여 만든 코드입니다. 조합방식도 재귀함수 형태로 만들어서 어느 한 경우일때 모든 일처리를 합니다.
#그전 코드는 일단 모든 경우를 구해놓고 그다음에 각 경우의 일처리를 하는데 이경우는 한 경우가 생길때 바로바로 처리합니다
#이방법은 dfs와 브루트 포스를 이용한 방법
#모든 경우를 하나씩 다 확인 합니다.
import copy
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
answer = 0
# for i in range(N):
#     graph.append(list(map(int, input().split())))
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1,0,1,0], [0, -1, 0, 1]
def disease(graph, x, y):#질병퍼트리기
    
    for i in range(4):
        nx, ny = x + dx[i],y + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < M :
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                disease(graph, nx, ny)
    
def build_wall(graph,start,cnt):
    global answer
    if cnt == 3:
        copy_graph = copy.deepcopy(graph)
        for i in range(N):
            for j in range(M):
                if copy_graph[i][j] == 2:
                    disease(copy_graph, i, j)
        
        safe_region = sum( _.count(0) for _ in copy_graph)
        answer = max(answer, safe_region)
        return
    for i in range(start, N*M):
        v = i // M
        h = i % M   
        if graph[v][h] == 0:
            graph[v][h] = 1
            build_wall(graph, i, cnt +1)
            graph[v][h] = 0
    
cnt = 0
start = 0
build_wall(graph,start,cnt)
print(answer)