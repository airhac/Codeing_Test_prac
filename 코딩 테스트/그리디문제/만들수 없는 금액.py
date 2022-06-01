# N = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# s=0
# for i in data:
#     s+=i

# for i in range(1,s+1):
#     result = i
#     for j in data:
#         if result - j == 0:
#             result = result - j
#             break
#         elif result - j < 0:
#             continue
#         elif result - j > 0:
#             result-=j
#     if result > 0:
#         result = i
#         break

# print(result)
N = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1
for x in data:
    if target < x:
        break
    target+=x

print(target)