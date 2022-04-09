import time
start_time = time.time()
N, M = map(int, input().split())
result = 0
for n in range(N):
    data = list(map(int, input().split()))
    min_value = 10001
    for d in data:
        if min_value > d:
            min_value = d
    result = max(result,min_value)
               
result = max(data)
print(result)       
end_time = time.time()

print("time : ", end_time - start_time) #수행시간 출력



# N, M = map(int, input().split())
# result = 0
# for n in range(N):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(min_value, result)
    
# print(result)