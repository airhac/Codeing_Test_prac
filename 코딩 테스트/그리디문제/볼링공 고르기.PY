# N, M = map(int, input().split())
# data = list(map(int, input().split()))

# cnt = 0 
# for i  in range(N):
#     for j in range(i+1,N):
#         if data[i] != data[j]:
#             cnt+=1
            
# print(cnt)
#내가 만든 방식은 시간 복잡도가 n^2이다.
n, m  = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(n)