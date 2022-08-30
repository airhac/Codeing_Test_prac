# import sys
# import math
# input = sys.stdin.readline
# N = int(input())
# K = int(input())
   
# #소수 찾기
# answer = []
# for num in range(2, N + 1):
#     array = [True] * (num+1)
#     for i in range(2, int(math.sqrt(num)) +1):
#         #소수가 아닌경우
#         if array[i] == True:
#             j = 2
#             while i*j <= num:
#                 array[i*j] = False
#                 j+=1
#     answer.append(max([j for j in list(i for i in range(2, num+1) if array[i] == True) if num % j == 0]))
# cnt = 1
# for a in answer:
#     if a <= K:
#         cnt += 1
# print(cnt)
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
#소인수 구하기
array = [0] * (N + 1)
for i in range(2,N+1):
    if array[i] == 0:
        for t in range(i,N+1,i):
            if t%i == 0:
                array[t] = max(array[t],i)

ans = 0
for i in array:
    if i <= K:
        ans += 1
print(ans-1)