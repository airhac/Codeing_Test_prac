# N, M, K = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort()
# first = num[N-1]
# second = num[N-2]

# result=0
# while True:
#     for k in range(K):
#         if M == 0:
#             break
#         result += first_num
#         M-=1        
#     if M == 0:
#         break
#     result +=second_num
#     M-=1
    
# print(result)

#수학적 방법으로 해결한 모습
# N, M, K = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort()
# first = num[N-1]
# second = num[N-2]

# result = (first*K + second)*(M//(K+1)) + (M%(K+1))*first

# print(result)

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = [n-1]
second = [n-2]

result = 0
while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-=1
    
        
        