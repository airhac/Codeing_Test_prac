# N = int(input())
# data = list(map(int, input().split()))
# result = 0
# for i in range(N):
#     if N- data[i] >=0 :
#         N -= data[i]
#         result +=1
#     continue

# print(result)
N = int(input())
data = list(map(int, input().split()))
data.sort()
result=0
cnt=0
for i in data:
    cnt+=1
    if cnt >= i:
        result+=1
        cnt = 0

