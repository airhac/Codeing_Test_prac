#반복문을 이용한 조합 
# def solution(arr):
#     n = len(arr)
    
#     #현재 5개의 원소중 4개 원소만 뽑아 만들수있는 모든 경우의 수
#     #i는 첫번째 수 
#     for i in range(n):
#         #j는 두번째 올 경우의 수 인데 첫번째 수를 빼줍니다.
#         for j in range(i+1, n):
#             #k 또한 3번쨰에 올 수이며 천번째수 두번째 수를 빼준 나머지 수의 나열이니깐 j+1 부터 시작하면 됩니다.
#             for k in range(j+1, n):
#                 for h in range(k+1, n):
#                     print(i, j, k, h)
            
# solution([0,1,2,3,4])
#for문인 경우 원소가 하나 추가 될떄 마다 for문을 추가해야합니다.
#이러한 경우 재귀로하면 수정할 필요가없어 확장성이 좋아집니다.
#조합은 중복 숫자를 제외한 나머지 숫자로 만드는 경우의수, 순서 상관없음
# def combination(arr, r):
#     result = []
#     if r == 0:
#         return [[]]
#     print("r의 값:", r)
#     for i in range(len(arr)):
#         e = arr[i]
#         print(e)
#         for rest in combination(arr[i+1:], r-1):
#             result.append([e] + rest)
#             print(result)
    
#     return result

# print(combination([0,1,2,3,4], 3))
# def combination(arr, r):
#     result = []
#     if r == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         e = arr[i]
#         for rest in combination(arr[i+1:], r-1):
#             result.append([e] + rest)
# print(combination([0,1,2,3,4], 3))
#순열은 순서 상관있음
# def permutation(arr, r):
#     result = []
#     if r == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         e = arr[i]
#         for rest in permutation(arr[:i] + arr[i+1:], r-1):
#             result.append([e] + rest)
#     return result
# print(permutation([0,1,2,3,4], 3))




