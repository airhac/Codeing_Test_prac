# import sys
# input = sys.stdin.readline
# N = int(input())
# tree = [[] for _ in range(N + 1)]
# for _ in range(N):
#     p, l_c, r_c = map(int, input().split())
#     tree[p].extend([l_c, r_c])
    
# def dfs(tree, node, answer):
#     for i in tree[node]:
#         if i == N:
#             print(answer)
#             exit(0)
#         if i != -1:
#             answer += 1
#             answer = dfs(tree, i, answer)
#             answer += 1
#     return answer
# answer = 1
# node = 1
# print(dfs(tree, node, answer))
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

# def get_depth(node):
#     if tree[node][1] != -1:
#         return 1 + get_depth(tree[node][1])
#     return 1


# n = int(input())
# tree = [0] * (n + 1)

# for _ in range(n):
#     parent, left_child, right_child = map(int, input().split())
#     tree[parent] = (left_child, right_child)
# print(get_depth(1))
# print(2 * n - get_depth(1) - 1)
###class를 이용한 방법
# import sys
# sys.setrecursionlimit(10**7)
# n = int(sys.stdin.readline())
# array = {}

# for i in range(n) :
# 	num, left, right = map(int,sys.stdin.readline().split())
# 	array[num] = [left,right]

# count = 0
# visited = [False] * (n+1)
# check = [False] * (n+1)

# def dfs(num, what_check, baby) :
# 	visited[num] = True
# 	check[num] = what_check
# 	if baby[0]!= -1 :
# 		new_check = what_check or True
# 		dfs(baby[0], new_check, array[baby[0]])
# 	if baby[1]!= -1 :
# 		new_check = what_check or False
# 		dfs(baby[1], new_check, array[baby[1]])

# for i in range(1,n+1) :
# 	if visited[i] == False :
# 		dfs(i,False, array[i])
# 	if i != 1 :
# 		if check[i]:
# 			count += 2
# 		else :
# 			count += 1
# print(count)
# ######################
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# n = int(input())
# left = [0] * (n+1)
# right = [0] * (n+1)
# visitCount = 0
# for _ in range(n):
#     i, l, r = map(int, input().split())
#     left[i] = l
#     right[i] = r
# ans = 0

# def traverse(cur):
#     global ans, visitCount
#     if left[cur] != -1:
#         ans += 1
#         traverse(left[cur])
#         ans += 1
#     visitCount += 1
#     if right[cur] != -1:
#         ans += 1
#         traverse(right[cur])
#         if visitCount == n: return
#         ans += 1
# traverse(1)
# print(ans)
#######
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
array = {}

for i in range(N):
    n, left, right = map(int, input().split())
    array[n] = [left, right]

visited = [False] * (N + 1)
check = [False] * (N + 1)
def dfs(now, what_check, child):
    visited[now] = True
    check[now] = what_check
    if child[0] != -1:
        new_check = what_check or True
        dfs(child[0], new_check, array[child[0]])
    if child[1] != -1:
        new_check = what_check or False
        dfs(child[1], new_check, array[child[1]])
answer = 0
for i in range(1,N + 1):
    if visited[i] == False:
        dfs(i, False, array[i])
    if i != 1:
        if check[i]:
            answer += 2
        else:
            answer += 1

print(answer)