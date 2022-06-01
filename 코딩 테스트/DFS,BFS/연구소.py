#조합 사용한풀이
from itertools import combinations
import copy
from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def how_spread(graph):
    result = 0
    #감염체가 이동할 방행
    dx = [-1, 0 , 1, 0]
    dy = [0, -1 ,0, 1]
    #감염체의 위치 파악하기
    disease = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                disease.append((i,j))
    
    queue = deque(disease)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))
        
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                result +=1
                
    return result
def build_wall(graph):
    location = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                location.append((i,j))
    #백트래킹으로 어느한 경우의 수의 벽을 세우면 그에대한 bfs로 감염정도를 확인
    answer = []
    for com_list in combinations(location, 3):
        copy_graph = copy.deepcopy(graph)
        for i,j in com_list:
            copy_graph[i][j] = 1
        answer.append(how_spread(copy_graph))
                
    #안전지대가 최대인경우만 반환 시켜주면 됩니다.
    return max(answer)

print(build_wall(graph))


