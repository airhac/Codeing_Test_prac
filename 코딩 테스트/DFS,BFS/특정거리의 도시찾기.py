# n, m , k, x = map(int, input().split())
# graph = [[]for i in range(n)]
# for i in range(n):
#     parent, child = map(int, input().split())
#     graph[parent].append(child)
 
    
# city = []
# def find_city(graph,city, k, x):
#     k-=1
#     for i in graph[x]:
#         x = i
#         if k != 0:
#             find_city(graph,city, k, x)
#         else:
#             city.append(x)
#     return city if city else -1        

# for i in find_city(graph,city,k,x):
#     print(i)
# 각 도시까지가는데 최단거리
##pypy3로는 돌아가는데 시간이 많이 걸리나봄
# from collections import deque


# n, m , k, x = map(int, input().split())
# graph = [[]for i in range(n+1)]
# for i in range(m):
#     parent, child = map(int, input().split())
#     graph[parent].append(child)
    
# visited = [False] * (n+1)
# visited[x] = True
# queue = deque([(k,x)])
# city = []
# while queue:
#     dist, now = queue.popleft() #현재 가야하는거리, 위치
#     if dist == 0:
#             city.append(now)
#     elif dist > 0:
#         dist-=1
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append((dist, i))
# if city:
#     city.sort()         
#     for i in city:
#         print(i)
# else:
#     print(-1)
#python3으로 할때 heapq 사용
# import sys
# from heapq import heappop, heappush
# input = sys.stdin.readline
# INF = sys.maxsize

# def bfs(graph, dist, k, x):
#     q = []

#     heappush(q, (0, x)) # 이동회수, 출발도시
#     ans = []
#     dist[x] = 0
#     while q:
#         cnt, x = heappop(q)

#         if cnt == k:
#             heappush(ans, x)
#             continue

#         for next in graph[x]:
#             if dist[next] > cnt + 1:
#                 dist[next] = cnt + 1
#                 heappush(q, (dist[next], next))
    
#     if len(ans) == 0:
#         print(-1)
#     else:
#         while ans:
#             print(heappop(ans))

# def main():
#     N, M, K, X = map(int, input().split())
#     graph = [[] for _ in range(N + 1)]
#     dist = [INF] * (N + 1)

#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)

#     bfs(graph, dist, K, X)

# main()
#다른 방법
# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M, K, X = map(int, input().split())

# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     A, B = map(int, input().split())
#     graph[A].append(B)

# answer = []

# queue = deque([[X]])
# visited = set([])
# depth = 0

# while queue and depth <= K:
#     nodes = queue.popleft()
#     next_level_nodes = []
#     for node in nodes:
#         if node not in visited:
#             visited.add(node)
#             if depth == K:
#                 answer.append(node)
#             else:
#                 next_level_nodes += graph[node]
#     if next_level_nodes:
#         queue += [next_level_nodes]
#     depth += 1

# if answer:
#     answer.sort()
#     for i in answer:
#         print(i)
# else:
#     print(-1)
import heapq
import sys
read = sys.stdin.readline


def solve():
    N, M, K, X = map(int, read().split())
    # 인접 리스트
    adj = [list() for _ in range(N+1)]
    for _ in range(M):
        f, t = map(int, read().split())
        adj[f].append(t)

    # 최단 거리 배열
    min_dists = [300002] * (N+1)

    # 우선순위 큐
    # (해당 노드까지의 최단거리, 노드번호) 튜플을 원소로 가짐
    q = []
    heapq.heappush(q, (0, X))
    min_dists[X] = 0

    ans = []

    # 남은 모든 노드들에 대하여
    while q:
        # 우선순위 큐 안에 있는 최단 거리 노드 선택
        dist, node = heapq.heappop(q)
        # 이미 처리된 노드라면 continue
        if min_dists[node] < dist:
            continue

        # 현재 노드까지의 거리가 K라면 정답 리스트에 저장 후 continue
        if min_dists[node] == K:
            ans.append(str(node))
            continue

        # 연결된 노드들의 최단거리 갱신 후 우선순위 큐에 추가
        for to in adj[node]:
            if min_dists[to] > dist + 1:
                min_dists[to] = dist + 1
                heapq.heappush(q, (dist+1, to))

    return '\n'.join(ans) if ans else -1


print(solve())