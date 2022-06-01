#내가 푼 방식
# N, K =  map(int, input().split())
# cnt = 0
# while True:
#     if N == 1:
#         break
#     if N % K !=0:
#         N = N-1
#         cnt+=1
#     else:
#         N = N//K
#         cnt+=1

# print(cnt)
# 정답 풀이 방식
# 왜 이런식으로 푸는가 여러번 반복이 아닌 한번의 계산으로 한꺼번에 처리하기 위해서
# 뺼거는 빼고 나눠 질수 있는 부분만 반복 시킨다.
N, K =  map(int, input().split())
result = 0
while True:
    target = (N//K)*K
    result += (N - target)
    N = target
    if N < K:
        break
    #K로 나누기
    result+=1
    N //= K

result += (N-1)
print(result)

# import time
# start_time = time.time()

# end_time = time.time()

# print("time : ", end_time - start_time) #수행시간 출력
    
# N, K = map(int, input().split())
# result = 0
# while True:
#     target = (N//K) * K
#     result += (N- target)
#     N = target
#     if N < K:
#         break
#     result +=1
#     N //= K

# result += (N-1)
# print(result)
